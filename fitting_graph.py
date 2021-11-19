import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
#Define inverse proportional function
def f_1(x,U):
  return U/x 
x0 = [5,10,15,20,25,30,35,40,45,50]
y0 = [586,291,198,143,101,98,72,68,59,55]
plt.title("test") 
plt.xlabel('R/Ω')
plt.ylabel('I/mA')
plt.scatter(x0[:], y0[:], 5, "red",linewidth=3)   #Generate scatter diagram
plt.plot(x0, y0, "blue")    #Generate graph
U1 = optimize.curve_fit(f_1, x0, y0)[0] 
x1 = np.arange(5, 50.01, 0.01)
y1 = U1/x1
plt.plot(x1, y1, "orange")   #Generate fitting graph
plt.show()
print("U=",U1)