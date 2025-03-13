#Msc Python Project (2021)

#Name: Prathamesh k Deshmukh

#Que 4 Plot of Mandelbrot set (fractal)

#prg might take some time for loading

import numpy as np
import matplotlib.pyplot as plt

li1=[]

#fuction defination and loop

def fun(a):

 global z
 z=0
 for ind in range(25): #recommended value 10 to 25 (you can increase it depending on your computational power)

  z=z*z+a
 return z
 print(z)

#float range
start =- 2.5 #recc -2.5
stop = 2.5 #recc -2.5
step = 0.005 #recc 0.005

float_range_array = np.arange(start, stop, step)


def point():

 for x in  list(float_range_array) :
  for y in  list(float_range_array) :

    global c
    c = complex(x,y)

    if abs(fun(c))<=2:
     li1.append(c)


#function calling

point()
arr0=np.array(li1)


#Ploting the graph

plt.scatter(arr0.real,arr0.imag,s=5,color="black")
plt.xlim([-3, 3])
plt.ylim([-3, 3])

plt.xlabel("Real axis")
plt.ylabel("imaginary axis ")
plt.title("plot of Mandelbrot set ")
plt.savefig('IMG_Mandelbrot1.png')

plt.show()