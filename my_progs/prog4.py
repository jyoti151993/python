# Kilometere to miles
# take kilometers from the user

kilometers=float(input('Enter the value in kilometers: '))

# conversion factor
conv_factor=0.621371

# calculate miles
miles =kilometers*conv_factor

print('%0.2f kilometers is equal to %0.2f miles'%(kilometers,miles))
