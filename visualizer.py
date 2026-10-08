from image import Image
import numpy as np
import cv2


class Visualizer:
    def __init__(self, input, output, sorter, fps, maxFramesSkipped):
        self._sorter = sorter
        self._image = Image(input)

        self.framesSkipped = 0
        self.maxFramesSkipped = maxFramesSkipped

        # init video
        self._fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self._video = cv2.VideoWriter(
            output,
            self._fourcc,
            fps,
            (
                self._image.width,
                self._image.height
            )
        )

    def shuffle(self):
        self._image.shuffle()

    def _swap(self, i, j):
        self._image.swap(i, j)
        self._write_frame()

    def _write_frame(self, forced = False):
        if(self.framesSkipped > self.maxFramesSkipped or forced):
            rgb_frame = np.array(self._image.image)
            bgr_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

            self._video.write(bgr_frame)
            self.framesSkipped = -1

        self.framesSkipped += 1

    def render(self):
        self._sorter(self._image.indices, self._swap)
        self._write_frame(forced = True)
        self._video.release()
