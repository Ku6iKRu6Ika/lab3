import sorting
from visualizer import Visualizer

INPUT = ''
OUTPUT = 'video.mp4'
FPS = 30

if __name__ == '__main__':
    v = Visualizer(
        INPUT,
        OUTPUT,
        sorting.bubble_sort,
        FPS
    )
    v.shuffle()
    v.render()
