from src.blockpi import BlockPi
import pytest

@pytest.fixture()
def game():
    game = BlockPi()
    game.clear_screen()
    return game

def test_set_screen_with_land(game):    
    expected = ([[0,0,0]] * 56) + ([[0, 100, 0]] * 8) 
    
    game.set_level(expected)
    game.set_screen()
    screen = game.get_screen()

    assert expected == screen


def test_set_player_location(game):
    pass

def test_player_moves_right(game):
    pass

def test_player_moves_left(game):
    pass

def test_player_moves_up(game):
    pass

def test_screen_left_bound(game):
    pass

def test_screen_right_bound(game):
    pass

def test_screen_upper_bound(game):
    pass

