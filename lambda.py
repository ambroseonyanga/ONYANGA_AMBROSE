class Person:
    def __init__(self,name, age, height, weight=10):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def show_name(self):
        return "My name is " + self.name
    
    def age_in_20(self):
        return f"I will be { self.age + 20 } in 20 years"
    
    def show_weight(self):
        print("I am {}kgs fat".format(self.weight))
        
    def compare_height_with_limit(self, limit):
        if self.height > limit:
            return f"My height is above {limit}"
        if self.height < limit:
            return f"My height is below {limit}"
        
        
person1 = Person("John", 23, 176, 30)

print(person1.show_name())
print(person1.age_in_20())
print(person1.show_weight())
print(person1.compare_height_with_limit(150))
    