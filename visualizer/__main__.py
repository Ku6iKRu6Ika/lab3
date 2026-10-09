import sys
import numpy as np

from visualizer.config_loader import config
from visualizer.image import Pixel, PixelSwapper
from visualizer.video import VideoBuilder


def main():
    if len(sys.argv) < 4:
        exit('You are not entering enough arguments.')

    PATH_TXT = sys.argv[1]
    PATH_IMAGE = sys.argv[2]
    PATH_VIDEO = sys.argv[3]

    image = PixelSwapper(PATH_IMAGE)
    video = VideoBuilder(
        PATH_VIDEO,
        image.width,
        image.height,
        config.fps,
        config.maxFramesSkipped
    )

    video.pause(image.image, config.introAndOutroLength)

    with open(PATH_TXT, 'r', encoding='utf-8') as fp:
        numbers = np.array(list(map(int, fp.readline().split(' '))))
        image.swap_by_number(numbers)

        for line in fp.readlines():
            x1, y1, x2, y2 = map(int, line.split(' '))
            p1 = Pixel(x1, y1)
            p2 = Pixel(x2, y2)

            image.swap(p1, p2)
            video.write_frame(image.image)

    video.pause(image.image, config.introAndOutroLength)
    video.release()


if __name__ == '__main__':
    main()
