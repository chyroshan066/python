import random


class Dice:
    def roll(self):
        print(f"( {random.randint(1, 6)}, {random.randint(1, 6)} )")


d1 = Dice()
d1.roll()