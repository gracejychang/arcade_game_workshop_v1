import arcade
import random

class Flower(arcade.Sprite):
    def __init__(self):
        super().__init__()

    @classmethod
    def setup(cls, flowers_list, bottom_obstacles_list, top_obstacles_list):
        number_of_flowers = random.randrange(1, 3)
        for i in range(number_of_flowers):
            # TODO: make sure the flower is not being placed on top of obstacles, then append the flower to
            # list of flowers

        return flowers_list
