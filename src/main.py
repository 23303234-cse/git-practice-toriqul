from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Toriqul Islam")
print("Today's Date:", date.today())


print("Addition:", add(20, 5))
print("Subtraction:", subtract(20, 5))
print("Multiplication:", multiply(20, 5))

print("Division:", divide(20, 2))
print("Error Test:", divide(20, 0))