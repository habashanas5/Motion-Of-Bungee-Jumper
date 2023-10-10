from matplotlib import pyplot as plt
from math import exp
mass = 80
k = 6
acceleration_due_to_gravity = -9.81
weight = mass * acceleration_due_to_gravity
weight_displacement = -weight / k
unweighted_length = 30
initial = 0.3
dt = 0.02
duration = 100
length = 0
v = 0
V = []
P = []
S = []
time = []
iteration = int(duration/dt)
speed = abs(v)

for i in range(iteration):
    t = i * dt + 1
    if abs(length)> abs(unweighted_length) :
        restoring_spring_force = -k * (length - (unweighted_length))
    else:
        restoring_spring_force = 0
    air_friction = -0.65 * 0.1 * v * speed
    TF=weight + restoring_spring_force + air_friction
    a=TF/mass
    change_in_velocity = a
    change_in_position = v
    speed = abs(v)
    v+= change_in_velocity * dt
    change_in_position= v * dt
    length+= change_in_position
    speed = abs(v)
    time.append(i*dt)
    S.append(length)
    V.append(v)
    P.append(TF)

plt.plot(time , S)
plt.xlabel("(time)")
plt.ylabel("(length)")
plt.title("Motion Of Bungee Jumper")
plt.show()