from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT

class BlockPi(object):
    def __init__(self):
        self.sense_hat = SenseHat()
        self.set_player_location(0,0)
        return

    def __iter__(self):
        return self
    
    def __next__(self):
        return self

    def get_screen(self):
        return self.sense_hat.get_pixels()

    def set_screen(self):
        screen = [[0,0,0]] * 64
        player = [255, 255, 255]

        self.sense_hat.set_pixels(screen)
        self.sense_hat.set_pixel(self.player_x, self.player_y, player)

    def set_player_location(self, x, y):
        self.player_x = x
        self.player_y = y
        self.set_screen()

    def move_player_right(self):
        new_x = min(7, self.player_x + 1)
        self.set_player_location(new_x, self.player_y)

    def move_player_left(self):
        new_x = max(0, self.player_x - 1)
        self.set_player_location(new_x, self.player_y)

    def move_player_up(self):
        new_y = max(0, self.player_y - 1)
        self.set_player_location(self.player_x, new_y)

    def move_player_down(self):
        new_y = min(7, self.player_y + 1)
        self.set_player_location(self.player_x, new_y)

    def clear_screen(self):
        self.sense_hat.set_pixels([[0,0,0]] * 64)

    def run_game(self):
        for i in self:
            event = self.sense_hat.stick.wait_for_event()
            if event.action != ACTION_RELEASED:
                if event.direction == DIRECTION_UP:
                    self.move_player_up()
                elif event.direction == DIRECTION_DOWN:
                    self.move_player_down()
                elif event.direction == DIRECTION_RIGHT:
                    self.move_player_right()
                elif event.direction == DIRECTION_LEFT:
                    self.move_player_left()

#game = BlockPi()
#game.run_game()
