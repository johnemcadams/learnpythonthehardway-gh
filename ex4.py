# declare cars
cars = 100

# declare passenger space in a care
space_in_a_car = 4

# declare drivers
drivers = 30

# declare passengers
passengers = 90

# find how many unused cars there are by subtracting the cars from the drivers
cars_not_driven = cars - drivers

# declare a new variable for the cars being driven
cars_driven = drivers

# Calculate the passenger capacity of the car pool
carpool_capacity = cars_driven * space_in_a_car

# Calculate average of passengers per car
average_passengers_per_car = passengers / cars_driven

# Print some stats about the car pool
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."