from image import Image
import cv2


class Visualizer:
    def __init__(self, input, output, sorter, fps):
        self._sorter = sorter
        self._image = Image(input)

        # init video
        self._fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self._video = cv2.VideoWriter(
            output,
            self._fourcc,
            fps,
            (
                self._image.witdh,
                self._image.height
            )
        )

    def shuffle(self):
        self._image.shuffle()

    def _swap(self, i, j):
        self._image.swap(i, j)
        self._write_frame()

    # Можно сделать поддержку jpg, а можно jpg и png (нужно учитывать количество каналов). Делай как хочешь
    def _write_frame(self):
        pass

    def render(self):
        self._sorter(self._image.indices, self._swap)
        self._video.release()
