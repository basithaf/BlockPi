from src.blockpi import BlockPi
import pytest

@pytest.fixture()
def game():
    game = BlockPi()
    game.clear_screen()
    return game

@pytest.fixture()
def test_level():
    test_level = ([[0,0,0]] * 56) + ([[0, 100, 0]] * 8)
    return test_level

def test_set_screen_with_land(game, test_level):    
    expected = test_level.copy()
    
    game.set_level(expected)
    game.set_screen()
    screen = game.get_screen()

    assert expected == screen


def test_set_player_location(game, test_level):
    expected = test_level.copy()
    expected[50] = [248, 252, 248]

    game.set_level(test_level)
    game.set_player_location(2, 6)
    game.set_screen()

    screen = game.get_screen()

    assert expected == screen

def test_player_moves_right(game, test_level):
    expected = test_level.copy()
    expected[51] = [248, 252, 248]

    game.set_level(test_level)
    game.set_player_location(2, 6)
    game.move_player_right()
    game.set_screen()

    screen = game.get_screen()

    assert expected == screen

def test_player_moves_left(game, test_level):
    expected = test_level.copy()
    expected[49] = [248, 252, 248]

    game.set_level(test_level)
    game.set_player_location(2, 6)
    game.move_player_left()
    game.set_screen()

    screen = game.get_screen()

    assert expected == screen

def test_player_jumps_up_from_ground(game, test_level):
    expected = test_level.copy()
    expected[26] = [248, 252, 248]

    game.set_level(test_level)
    game.set_player_location(2, 6)
    game.move_player_jump_up()
    game.set_screen()

    screen = game.get_screen()

    assert expected == screen

def test_player_does_not_jump_up_in_air(game, test_level):
    expected = test_level.copy()
    expected[42] = [248, 252, 248]

    game.set_level(test_level)
    game.set_player_location(2, 5)
    game.move_player_jump_up()
    game.set_screen()

    screen = game.get_screen()

    assert expected == screen

def test_screen_left_bound(game, test_level):
    expected = test_level.copy()
    expected[48] = [248, 252, 248]

    game.set_level(test_level)
    game.set_player_location(1, 6)
    game.move_player_left()
    game.move_player_left()
    game.set_screen()

    screen = game.get_screen()

    assert expected == screen

def test_screen_right_bound(game, test_level):
    expected = test_level.copy()
    expected[55] = [248, 252, 248]

    game.set_level(test_level)
    game.set_player_location(6, 6)
    game.move_player_right()
    game.move_player_right()
    game.set_screen()

    screen = game.get_screen()

    assert expected == screen

def test_screen_upper_bound(game, test_level):
    test_level[16] = [0, 100, 0]
    expected = test_level.copy()
    expected[0] = [248, 252, 248]

    game.set_level(test_level)
    game.set_player_location(0, 1)
    game.move_player_jump_up()
    game.set_screen()

    screen = game.get_screen()

    assert expected == screen

