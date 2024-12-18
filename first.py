print('Hello py')

rows = 11  # Size of the face (odd number works best)

for i in range(rows):
    for j in range(rows):
        # Distance from the center to approximate a circle
        center = rows // 2
        distance = ((i - center)**2 + (j - center)**2)**0.5

        # Draw the outer circle
        if 4.5 <= distance <= 5.5:
            print("#", end="")
        # Draw the eyes
        elif (i == center - 2 and j == center - 2) or (i == center - 2 and j == center + 2):
            print("o", end="")
        # Draw the mouth
        elif i == center + 2 and center - 2 <= j <= center + 2:
            print("-", end="")
        # Fill the inside with spaces
        else:
            print(" ", end="")
    print()  # Move to the next row
