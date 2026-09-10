# class definition for Cookie
class Cookie:
    
    # constructor method to initialize the color attribute
    def __init__(self, color):
        self.color = color
    
    # method to get the color of the cookie
    def get_color(self):
        return self.color
    
    # method to set the color of the cookie
    def set_color(self, color):
        self.color = color

# Example usage of the Cookie class
cookie_one = Cookie("brown")
cookie_two = Cookie("white")

# Demonstrating the use of get_color and set_color methods
print('Cookie one is:', cookie_one.get_color())  # Output: brown
print('Cookie two is:', cookie_two.get_color())  # Output: white

# Changing the color of cookie_one
cookie_one.set_color("dark brown")

print('Cookie one is now:', cookie_one.get_color())  # Output: dark brown
print('Cookie two is still:', cookie_two.get_color())  # Output: white