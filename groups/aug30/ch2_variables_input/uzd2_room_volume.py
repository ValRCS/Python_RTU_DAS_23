# ---- VOLUME OF A ROOM ----
PRECISION = 3
# Ask the user for the dimensions of the room
width = float(input("\nEnter the WIDTH of the room in meters: "))
length = float(input("Enter the LENGHT of the room in meters: "))
height = float(input("Enter the HEIGHT of the room in meters: "))
 
# Calculate the volume of the room
volume = width * length * height
 
# Display the result
print(f"The volume of the room is {volume:.2f} cubic meters(m³).")
# alternative would be round it up to some precision
rounded_vol = round(volume, PRECISION)
print(f"The volume of the room is {rounded_vol} cubic meters(m³).")