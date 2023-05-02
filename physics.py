# function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# test f_to_c function with a value of 100 Fahrenheit
f100_in_celsius = f_to_c(100)

# function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * 9/5 + 32
    return f_temp

# test c_to_f function with a value of 0 Celsius
c0_in_fahrenheit = c_to_f(0)

# function to calculate force from mass and acceleration
def get_force(mass, acceleration):
    force = mass * acceleration
    return force

# test get_force function with train_mass and train_acceleration
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# function to calculate energy from mass and c (speed of light)
def get_energy(mass, c=3*10**8):
    energy = mass * c**2
    return energy

# test get_energy function with bomb_mass
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# function to calculate work from mass, acceleration, and distance
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

# test get_work function with train_mass, train_acceleration, and train_distance
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

