import numpy as np
import matplotlib.pyplot as plt

x0 = [5,10,15,20,25,30,35,40,45,50]
y0 = [586,291,198,143,101,98,72,68,59,55]
plt.title("test") 
plt.xlabel('R/Ω')
plt.ylabel('I/mA')
plt.scatter(x0[:], y0[:], 5, "red",linewidth=3)   #Generate scatter diagram
plt.show()