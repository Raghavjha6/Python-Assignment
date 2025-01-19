'''Q. The distance between two cities (in km.) is input through the keyboard. Write a program to 
convert and print this distance in meters, feet, inches and centimeters.'''

distance_km = float(input("Enter distance in kilometers: "))
distance_meters = distance_km * 1000
distance_feet = distance_km * 3280.84
distance_inches = distance_km * 39370.1
distance_centimeters = distance_km * 100000
print("Distance in meters:",distance_meters,"m")
print("Distance in feet:",distance_feet,"ft")
print("Distance in inches:",distance_inches,"in")
print("Distance in centimeters:",distance_centimeters,"cm")
