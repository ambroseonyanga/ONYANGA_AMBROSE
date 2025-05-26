class Animal:
    def speak(self):
        print("This animal makes sound")
class Cat(Animal):
    def sound(self):
        print("The cat meows")
cat1 = Cat()
cat1.sound()
cat1.speak()