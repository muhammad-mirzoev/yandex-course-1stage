import math


radian_angle = float(input())

degree_angle = (radian_angle * 180) / math.pi
degree_angle = degree_angle % 360

print(degree_angle)
