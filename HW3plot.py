import matplotlib.pyplot as plt
import numpy as np
"""
#Problem 5
figure, axes = plt.subplots()
circle_1 = plt.Circle((1, 0), 3, fill=False )
circle_2 = plt.Circle((2, 0), 3, fill=False ) 
circle_3 = plt.Circle((5, 0), 4, fill=False ) 

axes.add_artist(circle_1)
axes.add_artist(circle_2)
axes.add_artist(circle_3)

x = np.array([1.33687, 1.33687, 5.32626])
y = np.array([2.22974, -2.22974, 0])
plt.scatter(x, y, marker="o", c="black")


plt.axis('equal')
plt.xlim(-4, 10)
plt.ylim(-8, 8)
plt.title('Gershgorin disks for A')
plt.xlabel('eigenvalue real part')
plt.ylabel('eigenvalue imaginary part')
plt.show()
plt.close()
"""

#Problem 6a
figure, axes = plt.subplots()
circle_1 = plt.Circle((3, 0), 1, fill=False )
circle_2 = plt.Circle((-4, 0), 2, fill=False ) 

axes.add_artist(circle_1)
axes.add_artist(circle_2)

plt.axis('equal')
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.title('Gershgorin disks for A')
plt.xlabel('eigenvalue real part')
plt.ylabel('eigenvalue imaginary part')
plt.show()
plt.close()