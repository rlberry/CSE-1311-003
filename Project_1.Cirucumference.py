# ATTN: Calculate the area and circumference of a circle from its radius
# Step 1: prompt for radii
# Step 2: apply the are formula
# Step 3: print results

# module
import math

# this is the input
radiusString = raw_input("Enter the radius of your circle:")
radiusInteger=int(radiusString)

# this is the calculation
circumference=2*math.pi * radiusInteger
area=math.pi * (radiusInteger ** 2)

# this is the result/ output
print "The circumference is :", circumference , \
      ", and the area is: ", area