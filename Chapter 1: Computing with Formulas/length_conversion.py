#Exercise 1.2 Convert from meters to British length units.
#Author: Samuel Giglio IV

inch = 0.0254
foot = inch * 12
yard = foot * 3
mile = yard * 1760

meters = input(
        "Enter distance in meters to be converted into imperial units.\n")
meters = float(meters)
inches = meters / inch
feet = meters / foot
yards = meters / yard
miles = meters / mile

print("{m:g} meters is equivalent to {i:g} inches, {f:g} feet, {y:g} yards,\
        {mi:g} miles." .format(m=meters, i=inches, f=feet, y=yards, mi=miles))


"""
Sample run:
python3 length_conversion.py
Enter distance in meters to be converted into impreial units.
640
640 meters is equivalent to 25196.9 inches, 2099.74 feet, 699.913 yards, 0.397678 miles.
"""
