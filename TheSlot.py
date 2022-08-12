import random


class TheSlot:
    image_list = ['🦥', '🐹', '🐢', '🦄']

    def __init__(self):
        self.image = ''

    def __str__(self):
        return self.image

    def __repr__(self):
        return self.image

    def set_random_image(self):
        random_image = random.choice(TheSlot.image_list)
        self.image = random_image
