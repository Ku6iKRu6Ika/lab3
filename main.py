import sorting
from visualizer import Visualizer
import sys

INPUT = sys.argv[1]
OUTPUT = sys.argv[2]
FPS = 30

if __name__ == '__main__':
    v = Visualizer(
        INPUT,
        OUTPUT,
        sorting.mergeSort,
        FPS
    )
    for _ in range(50):
        v._write_frame(forced = True)
    v.shuffle()
    for _ in range(50):
        v._write_frame(forced = True)
    v.render()
