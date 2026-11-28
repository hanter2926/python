import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 10, 7)
x 
y = x**2
y
array =([0. , 1 , 4. , 9. , 16. , 25. , 36. ,])

plt.plot(x,y)
plt.title("Square Graph")
plt.xlabel("x Values")
plt.ylabel("y Values")

plt.grid()
plt.show()