#创建名为cars的变量并把cars的值设为100
cars = 100
#创建名为space_in_a_car的变量并把space_in_a_car的值设为4.0
space_in_a_car = 4.0
#创建名为drivers的变量并把drivers的值设为30
drivers = 30
#创建名为passengers的变量并把passengers的值设为90
passengers = 90
#创建cars_not_driven变量并把cars_not_driven的值设为cars减drivers
cars_not_driven = cars - drivers
#创建cars_driven变量并把driversd的值付给它
cars_driven = drivers
#创建carpool_capacity变量并把carpool_capacity的值设为cars_driven和space_in_a_car的乘积
carpool_capacity = cars_driven * space_in_a_car
#创建average_passengers_per_car变量并把average_passengers_per_car的值设为passengers除以cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are",cars,"cars available")
print("There are only", drivers,"drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity ,"people today")
print("We have", passengers,"to carpool today")
print("We need to put about",average_passengers_per_car,"in each car.")
