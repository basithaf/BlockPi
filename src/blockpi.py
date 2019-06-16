from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT

class BlockPi(object):
    def __init__(self):
        self.sense_hat = SenseHat()
        self.set_player_location(0,0)
        return

    def get_screen(self):
        return self.sense_hat.get_pixels()

    def set_screen(self):
        screen = ([[0,0,0]] * 56) + ([[0, 100, 0]] * 8)

        self.sense_hat.set_pixels(screen)

    def set_level(self, level_array):
        pass

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

    def handle_event(self, event):
        if event.direction == DIRECTION_UP:
            self.move_player_up()
        elif event.direction == DIRECTION_DOWN:
            self.move_player_down()
        elif event.direction == DIRECTION_RIGHT:
            self.move_player_right()
        elif event.direction == DIRECTION_LEFT:
            self.move_player_left()

    def run_game(self):
        game_finished = False
        
        while not game_finished:
            events = self.sense_hat.stick.get_events()
            if events:
                for event in events: 
                    if event.action != ACTION_RELEASED:
                        self.handle_event(event)
        
        self.sense_hat.show_message("CONGRATULATIONS")

    
