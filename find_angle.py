# Exercise: Find Angle MBC
# URL: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# Description: Using math library to find the value of an angle

import math

AB = int(input())
BC = int(input())

angle_rad = math.atan(AB / BC)
angle_deg = round(math.degrees(angle_rad))

print(f"{angle_deg}{chr(176)}")
