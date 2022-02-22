cars = 100
spaceAcar = 4.0
drivers = 30
passengers = 90
carsNotdrive = cars - drivers
carsDriven = drivers
carCapacity = carsDriven * spaceAcar
averPassenger = passengers / carsDriven
print("there are", cars, "cars available")
print("There are only", drivers, "available")
print("There will be", carsNotdrive, "empty today")
print("We can transport", carCapacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", averPassenger, "in a car")
# since in py3, we can get a float result in an int-int calculation, the output of the last sentence is 3.0, but
# not 3 in the textbook
