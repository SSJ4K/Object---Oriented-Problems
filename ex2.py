"""
Create a Vehicle class with max_speed, mileage and capacity instance
attributes.Create a Bus child class that inherits from the Vehicle class. 
The default fare charge of any vehicle is seating capacity * 100. If Vehicle 
is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
"""

class Vehicle:
    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
        
    def fare(self):
        return self.capacity * 100
        
    
class Bus(Vehicle):
    
    def fare(self):
        bus_fare = super().fare()
        return bus_fare + bus_fare * 10/100
        


        