# Create the subjects list
subjects = ["physics", "calculus", "poetry", "history"]

# Create the grades list
grades = [98, 97, 85, 88]

# Create the gradebook list
gradebook = [[subjects[0], grades[0]], [subjects[1], grades[1]], [subjects[2], grades[2]], [subjects[3], grades[3]]]

# Print the gradebook
print("Gradebook before modifications:")
print(gradebook)

# Add computer science to the gradebook
gradebook.append(["computer science", 100])

# Add visual arts to the gradebook
gradebook.append(["visual arts", 93])

# Modify the grade for visual arts
gradebook[4][1] += 5

# Remove the grade for poetry and add a pass
gradebook.remove(["poetry", 85])
gradebook.append(["poetry", "Pass"])

# Create the last semester gradebook list
last_semester_gradebook = [["Spanish", 90], ["Chemistry", 82], ["Art", 95], ["Physical Education", "Pass"]]

# Combine the two gradebooks into one
full_gradebook = last_semester_gradebook + gradebook

# Print the full gradebook
print("Full gradebook:")
print(full_gradebook)

