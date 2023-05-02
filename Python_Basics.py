# Step 1: Create variables
name = "Syed Mustafa"
age = 21
degree_program = "Cyber Security"
remaining_age = 1

# Step 2: Take user input
name = input("Syed Mustafa: ")
age = int(input("21: "))
degree_program = input("Cyber Security: ")

# Step 3: Calculate remaining age
remaining_age = (age * 3) % 2

# Step 4: Print message
print("Hi, my name is " + name + ". My remaining age after dividing my age by 2 is " + str(remaining_age) + " and I am currently enrolled in the " + degree_program + " degree program.")

