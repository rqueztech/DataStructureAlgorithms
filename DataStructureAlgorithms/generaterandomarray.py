import random

def generate_random_array(size, minimum, maximum):
    return random.sample(range(minimum, maximum), size)
