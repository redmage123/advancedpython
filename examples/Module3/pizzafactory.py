#!/usr/bin/python
from types import TypeType

# This shows another example of the factory design pattern.
class Pizza(object):
    @staticmethod
    def containsIngredient(ingredient):
        return False
    def getPrice(self):
        return 0

class PizzaPepperoniandSausage(Pizza):
    @staticmethod
    def containsIngredients(ingredient):
        return ingredient in ['sausage','pepperoni']
    def getPrice(self):
        return 9.75

class PizzaHamAndMushroom(Pizza):
    @staticmethod
    def containsIngredient(ingredient):
        return ingredient in ["ham", "mushroom"]

    def getPrice(self):
        return 8.50

class PizzaHawaiian(Pizza):
    @staticmethod
    def containsIngredient(ingredient):
        return ingredient in ["pineapple", "curry"]
    
    def getPrice(self):
        return 11.50

class PizzaFactory(object):
    @staticmethod
    def newPizza(ingredient):

# Find all the Pizza classes in the global namespace
        pizzaClasses = [j for (i,j) in globals().iteritems() if isinstance(j, TypeType) and issubclass(j, Pizza)]

# Walk through the classes and build one based on the ingredients passed to it. 
        for pizzaClass in pizzaClasses:
            if pizzaClass.containsIngredient(ingredient):
                return pizzaClass()

# if research was unsuccessful, raise an error
        raise ValueError('No pizza containing "%s".' % ingredient)

def main():
    try:
        myPizza = PizzaFactory().newPizza("ham")
        print("%.2f" % myPizza.getPrice())
        myPizza2 = PizzaFactory().newPizza("curry")
        print("%.2f" % myPizza2.getPrice())
        myPizza3 = PizzaFactory().newPizza("pepperoni")
        print("%.2f" % myPizza3.getPrice())
    except ValueError,e:
        print e

if __name__ == "__main__":
    main()
