#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Point:
    # Constructor for the Point class
    def __init__(self, x=0, y=0):
        # Initializing x and y coordinates of the point
        self.x = x
        self.y = y

class Segment:
    # Constructor for the Segment class
    def __init__(self, point1, point2):
        # Initializing the two points that define the segment
        self.point1 = point1
        self.point2 = point2
    
    # Method to calculate the length of the segment
    def length(self):
        # Using the distance formula to compute the length
        return ((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)**0.5
    
    # Method to calculate the slope of the segment
    def slope(self):
        # Checking for vertical line to avoid division by zero
        if (self.point2.x - self.point1.x) == 0:
            return None
        # Using the slope formula to compute the slope
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)

# Creating two Point objects
p1 = Point(3, 4)  # Point with coordinates (3, 4)
p2 = Point()      # Point with default coordinates (0, 0)

# Creating a Segment object using the two points
s = Segment(p1, p2)

# Calculating and storing the length and slope of the segment
result_of_length = s.length()
result_of_slope = s.slope()

result_of_length, result_of_slope

