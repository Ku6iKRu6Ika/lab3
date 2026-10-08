import matplotlib.pyplot as plt
import PIL.Image
import numpy as np
from random import shuffle


class Image:
    def __init__(self, path):
        self._image = PIL.Image.open(path)
        self._image = np.array(self._image.convert("RGB"))
        self._height, self._width, self._channels = self._image.shape
        self._indices = np.arange(
            0, self._width * self._height
        )

    def _to_coords(self, i):
        return (i // self._width, i % self._width)

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

    @property
    def indices(self):
        return self._indices

    def shuffle(self):
        shuffle(self.indices)
        coords = np.array([(i, j) for i in range(self.height) for j in range(self.width)])[self.indices]
        self._image = np.array([self._image[tuple(i)] for i in map(tuple, coords)]).reshape(self.height, self.width, 3)

    def swap(self, i, j):
        self._indices[i], self._indices[j] = self._indices[j], self._indices[i]
        temp = self._image[self._to_coords(i)].copy()
        self._image[self._to_coords(i)] = self._image[self._to_coords(j)]
        self._image[self._to_coords(j)] = temp