from sense_emu import SenseHat

class BlockPi(object):
    def __init__(self):
        self.sense_hat = SenseHat()
        self.player_x = 0
        self.player_y = 0
        return

    def get_screen(self):
        return self.sense_hat.get_pixels()

    def get_player_location(self):
        return (self.player_x, self.player_y)

    def set_player_location(self, x, y):
        self.player_x = x
        self.player_y = y

    def move_player_right(self):
        self.player_x += 1

    def move_player_left(self):
        self.player_x -= 1

    def move_player_up(self):
        self.player_y -= 1

    def move_player_down(self):
        self.player_y += 1

    def clear_screen(self):
        self.sense_hat.set_pixels([[0,0,0]] * 64)
        return

    def init_player(self):
        self.sense_hat.set_pixel(4, 4, 255, 255, 255)
        return