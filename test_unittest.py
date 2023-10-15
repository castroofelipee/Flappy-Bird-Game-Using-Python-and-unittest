import unittest
import pygame 
from Flappy import create_pipes 

class TestBirdMovement(unittest. TestCase):
    def test_bird_movement_update(self):
        bird_movement = 0 
        gravity = 0.17 

        for i in range(10):
            bird_movement += gravity 

        self.assertEqual(bird_movement, 1.7)

if __name__ == '__main__':
    unittest.main()