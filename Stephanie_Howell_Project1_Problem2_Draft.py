# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:06:09 2022

@author: Steph
"""
import math

# we are given a rod of given length y1 to y2
# let's attribute an arbitrary value for the length
L = 15

# we'll set a lower y-value and use our given length to calculate our upper y-value
y_1 = -5
y_2 = y_1 + L

# subtracting these two values will give us the total length of the rod, L
# we want to find a delta L
delta_L = L / 100
# assign some arbitrary value to lamb_0
lamb_0 = .5 * 10**-6

# we can define our distance from delta_q to the point of interest to be r
# our point of interest can be
P_x = 4
P_y = 6

# we'll set some initial values to begin our for loop iteration
summation = 0
y = 0
# therefore, r will be
for y in range(L):
    # distance formula to find r for each point along the rod
    r = math.sqrt((P_x)**2 + (P_y - y)**2)
    # our summation to find the integral numerically
    summation = summation + delta_L / r
    y = y + delta_L

# use the formula to calculate the electric potential
v = (lamb_0 / (4 * math.pi * (8.8 * 10**-12))) * summation
print(v)
