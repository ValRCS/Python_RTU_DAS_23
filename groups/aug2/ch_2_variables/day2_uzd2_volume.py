# volume of room
# 2. uzdevums
 
width = float(input("Lūdzu, ievadi telpas platumu (metros): "))
length = float(input("Lūdzu, ievadi telpas garumu (metros): "))
height = float(input("Lūdzu, ievadi telpas augstumu (metros): "))
 
volume = height * length * width
 
print(f"Telpas tilpums ir: {volume:.4f} kubikmetri (m³).")
# alternatively I could round the volume to say 3 digits
rounded_volume = round(volume, 3)
# so 12 means I want 12 spaces for this number total including .
# 4f is I want 4 digits after comma(.)
print(f"Telpas tilpums ir: {rounded_volume:12.4f} kubikmetri (m³).")