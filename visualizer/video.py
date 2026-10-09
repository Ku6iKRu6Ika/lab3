import numpy as np
import cv2


class VideoBuilder:
    def __init__(self, source, width, height, fps, maxFramesSkipped):
        self._fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self._video = cv2.VideoWriter(
            source,
            self._fourcc,
            fps,
            (
                width,
                height
            )
        )

        self._framesSkipped = 0
        self._maxFramesSkipped = maxFramesSkipped

    def write_frame(self, frame, forced=False):
        if(self._framesSkipped > self._maxFramesSkipped or forced):
            rgb_frame = np.array(frame)
            bgr_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

            self._video.write(bgr_frame)
            self._framesSkipped = -1

        self._framesSkipped += 1

    def pause(self, frame, numbers_of_frames):
        for _ in range(numbers_of_frames):
            self.write_frame(frame, True)

    def release(self):
        self._video.release()
        