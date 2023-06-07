import math


def calculate_distance_off_target(distance_to_target: float, degree_off: float):
    x = distance_to_target * math.sin(math.radians(degree_off))
    y = distance_to_target * math.cos(math.radians(degree_off))
    ay = distance_to_target - y
    return math.sqrt(x ** 2 + ay ** 2)


print(calculate_distance_off_target(33, 21))
