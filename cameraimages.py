from time import time


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        #self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]
        self.path = 'images';

    def get_frame(self):
        self.frame = open(self.path + '/current.jpg', 'rb').read()
        return self.frame