# class Animal:
#     def speak(self):
#         print("This animal makes sound")
# class Cat(Animal):
#     def sound(self):
#         print("The cat meows")
# cat1 = Cat()
# cat1.sound()
# cat1.speak()


class Bird:
    def fly(self):
        print("Birds can fly!")

class Eagle(Bird):
    def fly(self):
        print("An eagle can fly at an high altitude!")
class Hen(Bird):
    def fly(self):
        print("A hen can fly at a low altitude!")
def specific(bird):
    bird.fly()

bird = Bird()
bird1 = Hen()
bird2 = Eagle()

specific(bird)
specific(bird2)
specific(bird1)