"""
Pi calculation vith using Monte_Carlo method
with grapgic illustration of presision of Pi
and whe stohastick point located

I will use a geometric interpretation of Pi as a square of a round with r = 1

uniform(a, b) method of random.Random instance
    Get a random number in the range [a, b) or [a, b] depending on rounding.
"""
import random as r
import math 
import matplotlib.pyplot as plt
import numpy as np

p = print
h = help
d = dir
Pi =math.pi

def inside(*point):
    """
    Function which get two argument as a float point of location of random
    point.
    And this fuction answer a question is point inside the round or not
    """
    x,y = point
    if x**2+y**2<=1:
        return True
    else:
        return False

number_inside = 0       #useful constant
amount_of_random = 701
mas_for_plot_x = []
mas_for_plot_y = []

#Core of Monte-Carlo method
for i in range(0,amount_of_random):
    p_x = r.uniform(-1.0,1.0)
    p_y = r.uniform(-1.0,1.0)
    if inside(p_x,p_y):         
        number_inside +=1
        try:                                        
            #for i=0 except work! место способное породить исключение , удобно
            mas_for_plot_y.append(4*number_inside/i) #for plot
        except ZeroDivisionError:
            mas_for_plot_y.append(0.0)
        mas_for_plot_x.append(1.0*i/amount_of_random)

mas_Pi = Pi * np.ones_like(mas_for_plot_x) #introduced later for the same size of the array

p('oridginal Pi value =%.3f and numerical ex\
periment value = %.3f fot %d point'
    %(Pi,4*number_inside/amount_of_random,amount_of_random))

#some plot for illustration

plt.plot(mas_for_plot_x,mas_for_plot_y)
plt.plot(mas_for_plot_x,mas_Pi)
plt.title('Зависимость результата численного моделирования \nот числа точек',
          family='verdana')
plt.xlabel('доля точек',family='verdana')
plt.ylabel('Pi оригинал и эксперимент',family='verdana')
plt.legend(['Pi experemental',
            'Pi from math mjdule'],    # список легенды
            loc='upper right')    # положение легенды

plt.show()







