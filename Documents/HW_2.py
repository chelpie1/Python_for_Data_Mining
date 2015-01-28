# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 16:49:29 2015

@author: chelpie
"""

'''
A two-dimensional random walk simulator and animator.
'''

# The turtle package is part of Python's standard library. It provides some
# very primitive graphics capabilities. For more details see
#
#   https://docs.python.org/3/library/turtle.html
#
import turtle

import numpy as np


## TASK 1: ###################################################################
#def random_walk(n):
#    ''' Simulate a two-dimensional random walk.
#
#    Args:
#        n           number of steps
#
#    Returns:
#        Two Numpy arrays containing the x and y coordinates, respectively, at
#        each step (including the initial position).
#    '''
#        
#    x_coords = np.zeros((n+1))
#    y_coords = np.zeros((n+1))
#    p = 0.5
#    
#    for move in range(1,n+1):
#        axis = np.random.binomial(1, p, 1)
#        # randomly selects the axis we'll move along
#        sign = np.random.binomial(1, p, 1)
#        # randomly selects the sign of the move
#        sign[sign==0] = -1
#        # makes sign either -1 or 1
#        if axis == 0:
#            x_coords[move] = sign
#        else:
#            y_coords[move] = sign
#        
#    x = x_coords.cumsum()
#    y = y_coords.cumsum()
#
#    return x, y

## TASK 2 ###################################################################
#def random_walk(n, x_start = 0, y_start = 0):
#    
#    x_coords = np.zeros((n+1))
#    y_coords = np.zeros((n+1))
#    p = 0.5
#    
#    x_coords[0] = x_start
#    y_coords[0] = y_start
#    
#    for move in range(1,n+1):
#        axis = np.random.binomial(1, p, 1)
#        # randomly selects the axis we'll move along
#        sign = np.random.binomial(1, p, 1)
#        # randomly selects the sign of the move
#        sign[sign==0] = -1
#        # makes sign either -1 or 1
#        if axis == 0:
#            x_coords[move] = sign
#        else:
#            y_coords[move] = sign
#        
#    x = x_coords.cumsum()
#    y = y_coords.cumsum()
#
#    return x, y

## TASK 3 ###################################################################
#from numpy.random import random_sample
#
#def random_walk(n, x_start = 0, y_start = 0, p = 0.25*np.ones(4)):
#    
#    x_coords = np.zeros((n+1))
#    y_coords = np.zeros((n+1))
#    
#    x_coords[0] = x_start
#    y_coords[0] = y_start
#    
#    for move in range(1,n+1):
#        rs = random_sample(1)
#        bins = p.cumsum() # splits the [0,1] interval up into bins corr. to
#                          # the given probabilities
#        res = np.digitize(rs,bins)
#        if res == 0:
#            # move up
#            y_coords[move] = 1
#        elif res == 1:
#            # move down
#            y_coords[move] = -1
#        elif res == 2:
#            # move left
#            x_coords[move] = 1
#        else:
#            # move right
#            x_coords[move] = -1
#        
#    x = x_coords.cumsum()
#    y = y_coords.cumsum()
#
#    return x, y

## BONUS TASK ###############################################################
from numpy.random import random_sample

def random_walk(n, x_start = 0, y_start = 0, p = 0.25*np.ones(4)):
    
    if len(p) != 4:
        raise ValueError('p does not have length 4!')
    if sum(p) != 1:
        raise ValueError('p does not sum to 1!')
    
    x_coords = np.zeros((n+1))
    y_coords = np.zeros((n+1))
    
    x_coords[0] = x_start
    y_coords[0] = y_start
    
    for move in range(1,n+1):
        rs = random_sample(1)
        bins = p.cumsum() # splits the [0,1] interval up into bins corr. to
                          # the given probabilities
        res = np.digitize(rs,bins)
        if res == 0:
            # move up
            y_coords[move] = 1
        elif res == 1:
            # move down
            y_coords[move] = -1
        elif res == 2:
            # move left
            x_coords[move] = 1
        else:
            # move right
            x_coords[move] = -1
        
    x = x_coords.cumsum()
    y = y_coords.cumsum()

    return x, y

# Notice that the documentation automatically shows up when you use ?
def draw_walk(x, y, speed = 'slowest', scale = 20):
    ''' Animate a two-dimensional random walk.

    Args:
        x       x positions
        y       y positions
        speed   speed of the animation
        scale   scale of the drawing
    '''
    # Reset the turtle.
    turtle.reset()
    turtle.speed(speed)

    # Combine the x and y coordinates.
    walk = zip(x * scale, y * scale)
    start = next(walk)

    # Move the turtle to the starting point.
    turtle.penup()
    turtle.goto(*start)

    # Draw the random walk.
    turtle.pendown()
    for _x, _y in walk:
        turtle.goto(_x, _y)
#
