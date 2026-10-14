import sys
import numpy as np

from visualizer.config_loader import config
from visualizer.image import Pixel, PixelSwapper
from visualizer.video import VideoBuilder


def main():
    if len(sys.argv) != 3:
        exit('Wrong arg count')

    PATH_TXT = "sequence.txt" #no reasone to change that
    PATH_IMAGE = sys.argv[1]
    PATH_VIDEO = sys.argv[2]

    image = PixelSwapper(PATH_IMAGE)
    video = VideoBuilder(
        PATH_VIDEO,
        image.width,
        image.height,
        config.fps,
        config.maxFramesSkipped
    )

    video.pause(image.image, config.introAndOutroLength)

    with open(PATH_TXT, 'rb') as fp:
        intSize = int.from_bytes(fp.read(1), byteorder='little')
        wth = int.from_bytes(fp.read(intSize), byteorder='little')
        hgt = int.from_bytes(fp.read(intSize), byteorder='little')
        rawNums = fp.read(wth*hgt*intSize)
        numbers = [int.from_bytes(rawNums[i:i+intSize], byteorder='little') for i in range(0, len(rawNums), intSize)]
        image.swap_by_number(numbers)

        while True:
            rawNums = fp.read(4*intSize)
            if(len(rawNums)<4): break
            x1, y1, x2, y2 = [int.from_bytes(rawNums[i:i+intSize], byteorder='little') for i in range(0, len(rawNums), intSize)]
            p1 = Pixel(x1, y1)
            p2 = Pixel(x2, y2)

            image.swap(p1, p2)
            video.write_frame(image.image)

    video.pause(image.image, config.introAndOutroLength)
    video.release()


if __name__ == '__main__':
    main()
