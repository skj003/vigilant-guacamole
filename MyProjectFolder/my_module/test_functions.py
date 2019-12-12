""" Test Code for two of my original functions"""

from my_module.functions import *

def test_story_1(test_mode=False):
    assert story_1(test_mode=True) == "door"
    
def test_story_3(test_mode2=False):
    assert story_3(test_mode2=True) == "sword"