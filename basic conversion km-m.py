# 1) Complete the code to return the result of the conversion
def convert_distance(km):
	m = km * 1000  # exactly 1000 meters in 1 kilometer
	return m


# Do not indent any of the following lines of code as they are
# meant to be located outside of the function above


my_trip_kilometers = 55


# 2) Convert my_trip_kilometers to meters by calling the function above
my_trip_meters = convert_distance(my_trip_kilometers)


# 3) Fill in the blank to print the result of converting my_trip_kilometers
print("The distance in meters is " + str(my_trip_meters))


