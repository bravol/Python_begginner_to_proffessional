class Animal:
    def __init__(self):
        self.mum_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

# class inheritance
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("moving in water.")

nemo = Fish()
# nemo.swim()
# inherited method called
nemo.breathe()