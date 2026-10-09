import PIL.Image
import numpy as np


class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coords(self):
        return (self.x, self.y)


class PixelSwapper:
    def __init__(self, source):
        pillow_image = PIL.Image.open(source)

        self._image = np.array(pillow_image.convert("RGB"))
        self._height, self._width, _ = self._image.shape

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def channels(self):
        return self._channels

    @property
    def image(self):
        return self._image

    def swap(self, pixel1, pixel2):
        temp = self._image[pixel1.coords()].copy()
        self._image[pixel1.coords()] = self._image[pixel2.coords()]
        self._image[pixel2.coords()] = temp

    def swap_by_number(self, numbers):
        flat_image = self._image.reshape(-1, 3)
        shuffled_flat = flat_image[numbers]

        self._image = shuffled_flat.reshape(
            self.height, self.width, 3
        )
