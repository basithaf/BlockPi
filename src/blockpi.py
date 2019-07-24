from sense_emu import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT

class BlockPi(object):
    def __init__(self):
        self.sense_hat = SenseHat()
        self.player_dead = False
        self.goal_reached = False
        self.set_player_location(-1,-1)
        return

    def clear_screen(self):
        self.sense_hat.set_pixels([[0,0,0]] * 64)

    def get_screen(self):
        return self.sense_hat.get_pixels()

    def set_screen(self):
        self.sense_hat.set_pixels(self.current_screen)

        if (self.player_x >= 0 and self.player_y >= 0):
            if (self.sense_hat.get_pixel(self.player_x, self.player_y) == [0, 252, 0]):
                self.goal_reached = True
            self.sense_hat.set_pixel(self.player_x, self.player_y, 255, 255, 255)

    def set_level(self, level_array):
        self.current_screen = level_array.copy()


    def set_player_location(self, x, y):
        self.player_x = x
        self.player_y = y

    def move_player_right(self):
        new_x = min(7, self.player_x + 1)
        self.set_player_location(new_x, self.player_y)

    def move_player_left(self):
        new_x = max(0, self.player_x - 1)
        self.set_player_location(new_x, self.player_y)

    def move_player_jump_up(self):
        pixel_below_player = self.get_pixel_below_player()
        if(pixel_below_player != [0, 0, 0]):
            new_y = max(0, self.player_y - 3)
            self.set_player_location(self.player_x, new_y)

    def move_player_gravity(self):
        pixel_below_player = self.get_pixel_below_player()
        if(pixel_below_player == [0, 0, 0]):
            new_y = min(7, self.player_y + 1)
            self.set_player_location(self.player_x, new_y)

    def get_pixel_below_player(self):
        pixel_index = (self.player_y + 1) * 8 + self.player_x
        if self.player_y == 7:
            self.player_dead = True
            pixel_index = self.player_y * 8 + self.player_x
        return self.current_screen[pixel_index]


    def handle_event(self, event):
        if event.direction == DIRECTION_UP:
            self.move_player_jump_up()
        elif event.direction == DIRECTION_RIGHT:
            self.move_player_right()
        elif event.direction == DIRECTION_LEFT:
            self.move_player_left()

    def run_game(self):   
        while not (self.player_dead and self.goal_reached):
            events = self.sense_hat.stick.get_events()
            if events:
                for event in events: 
                    if event.action != ACTION_RELEASED:
                        self.handle_event(event)
        
        if (self.goal_reached == True):
            self.sense_hat.show_message("CONGRATULATIONS")
        else:
            self.sense_hat.show_message("YOU DED")

    
