from DataPoint import DataPoint
import pygame
from Colors import *


# store and array of data so it can be easily drawn on screen
class Data:

    # Populates the array of data with random data points
    def populate_list(self):
        for i in range(0, self.size):
            self.my_list.append(DataPoint(self.min, self.max))

    # min: minimum number a data point can be
    # max: maximum number a data point can be
    # size: how many data points the list will contain
    def __init__(self, min, max, size):
        self.min = min
        self.max = max
        self.size = size
        self.my_list = []
        self.populate_list()

    # min: minimum number a data point can be
    # max: maximum number a data point can be
    # size: how many data points the list will contain
    # clears the data list and repopulates with new data
    def randomize(self, min, max, size):
        self.min = min
        self.max = max
        self.size = size
        self.my_list.clear()
        self.populate_list()

    # draws all data on the screen
    def draw(self, screen):
        for i in range(0, self.size):
            self.my_list[i].draw(screen, i)

