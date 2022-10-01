"""Create a vehicle that comprises different parts that can be 
selected to be added to the vehicle. Each vehicle has its own 
serial number and name. Each vehicle can only have up to three 
wheels. For all parts, keep a note of the type of part, its serial 
number and an age of the part. For wheels, store their diameter 
and material. For normal parts, they can be determined to be old 
if they are over two years old. For wheels, if the wheel is above 
1m in diameter, it is old after a year, otherwise it is old after three years."""



class Vehicle:
  def __init__(self, serial_number, name, parts, wheels):
    self.serial_number = serial_number
    self.name = name
    self.parts = parts
    self.wheels = wheels

  # Display object information 
  def print_info(self):
    print(f"Serial Number = {self.serial_number}, Name = {self.name}, Parts = {self.parts}, Wheels = {self.wheels}")

  # Add wheels and add parts methods to
  def add_wheels(self, w):
    if len(self.wheels) == 3:
        self.wheels.pop(0)
      
    self.wheels.append(w)

  def add_parts(self, p):
    self.wheels.append(p)

class Parts:
  def __init__(self, type, serial_number, age):
    self.type = type
    self.serial_number = serial_number
    self.age = age

  def is_old(self):
    return self.age > 2

class Wheels(Parts):
  def __init__(self, diameter, material):
    self.diameter = diameter
    self.material = material

  # Override is_old method
  def is_old(self):
    return self.diameter > 1
    
    
