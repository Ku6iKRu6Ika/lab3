import matplotlib.pyplot as plt
import numpy as np


class Image:
    def __init__(self, path):
        self._image = plt.imread(path)
        self._height, self._width, self._channels = self._image.shape
        self._indices = np.arange(
            0, self._width * self._height
        )

    def _to_coords(self, i):
        return i // self._width, i % self._width

    @property
    def witdh(self):
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
        rng = np.random.default_rng()
        rng.shuffle(self.indices)

        flat_image = self._image.reshape(-1, self.channels)
        shuffled_flat = flat_image[self.indices]

        self._image = shuffled_flat.reshape(
            self.height, self.witdh, self.channels
        )

    def swap(self, i, j):
        pass