# Take input from user: list of 5 fruits
fruits = []

print("Enter 5 fruits:")
for i in range(5):
    fruit = input(f"Fruit {i+1}: ")
    fruits.append(fruit)

# Print 2nd and 4th items
print("2nd fruit:", fruits[1])
print("4th fruit:", fruits[3])

# Replace last item with 'mango'
fruits[-1] = "mango"

# Print updated list
print("Updated list of fruits:", fruits)
