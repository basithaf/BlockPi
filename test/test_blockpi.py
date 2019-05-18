from src.blockpi import BlockPi
import pytest

@pytest.fixture()
def game():
    game = BlockPi()
    game.clear_screen()
    return game

def test_get_empty_screen(game):    
    screen = game.get_screen()

    empty = [0, 0, 0]
    empty_screen = [empty] * 64

    assert screen == empty_screen

def test_init_player_at_4_4(game):
    game.init_player()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    start_screen = [empty] * 64
    start_screen[36] = player_dot

    assert screen == start_screen

def test_get_player_location(game):
    assert game.get_player_location() == (0, 0)

def test_set_player_location(game):
    game.set_player_location(1, 1)
    assert game.get_player_location() == (1, 1)

def test_player_moves_right(game):
    game.set_player_location(4,4)
    game.move_player_right()
    assert game.get_player_location() == (5, 4)

def test_player_moves_left(game):
    game.set_player_location(4,4)
    game.move_player_left()
    assert game.get_player_location() == (3, 4)

def test_player_moves_up(game):
    game.set_player_location(4,4)
    game.move_player_up()
    assert game.get_player_location() == (4, 3)

def test_player_moves_down(game):
    game.set_player_location(4,4)
    game.move_player_down()
    assert game.get_player_location() == (4, 5)
