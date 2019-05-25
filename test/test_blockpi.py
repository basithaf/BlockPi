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

def test_set_player_location(game):
    game.set_player_location(1, 1)
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[9] = player_dot

    assert screen == expected_screen

def test_player_moves_right(game):
    game.set_player_location(3,3)
    game.move_player_right()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[28] = player_dot

    assert screen == expected_screen

def test_player_moves_left(game):
    game.set_player_location(3,3)
    game.move_player_left()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[26] = player_dot

    assert screen == expected_screen

def test_player_moves_up(game):
    game.set_player_location(3,3)
    game.move_player_up()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[19] = player_dot

    assert screen == expected_screen

def test_player_moves_down(game):
    game.set_player_location(3,3)
    game.move_player_down()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[35] = player_dot

    assert screen == expected_screen

def test_screen_left_bound(game):
    game.set_player_location(0,3)
    game.move_player_left()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[24] = player_dot

    assert screen == expected_screen

def test_screen_right_bound(game):
    game.set_player_location(7,3)
    game.move_player_right()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[31] = player_dot

    assert screen == expected_screen

def test_screen_upper_bound(game):
    game.set_player_location(3,0)
    game.move_player_up()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[3] = player_dot

    assert screen == expected_screen

def test_screen_lower_bound(game):
    game.set_player_location(3,7)
    game.move_player_down()
    screen = game.get_screen()

    player_dot = [248, 252, 248]
    empty = [0, 0, 0]
    expected_screen = [empty] * 64
    expected_screen[59] = player_dot

    assert screen == expected_screen
