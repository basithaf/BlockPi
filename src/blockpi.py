from sense_emu import SenseHat

class BlockPi(object):
    def __init__(self):
        self.sense_hat = SenseHat()

    def get_screen(self):
        return self.sense_hat.get_pixels()