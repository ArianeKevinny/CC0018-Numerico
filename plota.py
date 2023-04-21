import numpy as np
import matplotlib.pyplot as plt
# Criando um gráfico com os eixos coordenados

def plota(f,a,b):
  fig, ax = plt.subplots()
  ax.set_ylabel('f(x)')
  ax.set_xlabel('x')
  ax.grid()
  
  #https://stackoverflow.com/questions/25689238/,→show-origin-axis-x-y-in-matplotlib-plot
  # set the x-spine (see below for more info on `set_position`)
  
  plt.axhline(0, color='black', linewidth=1)
  
  x = np.linspace(a,b,100)
  
  y = f(x)
  ax.plot(x,y)
  plt.xlim([a, b])
  plt.ylim([y.min(), y.max()])
  plt.show()
  
def f(x):
  return - 3 * np.tan(2*x) + x

plota(f, -3, 3)

