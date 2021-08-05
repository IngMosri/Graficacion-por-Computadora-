#Liberias necesarias para la graficacion 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

class Bresenham:
#definicion de los valores 
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
#comprobacion de los valores
	def sign(self,a):
		if a>0:
			ret = 1
		elif a<0:
			ret = -1
		else:
			ret = 0
		return ret

	def main_bresenham(self):
		x1 = self.x1
		y1 = self.y1
		x2 = self.x2 
		y2 = self.y2
		print("\n#############")

		x = x1
		y = y1
		dx = abs(x2-x)
		dy = abs(y2-y)
		s1 = self.sign(x2-x1)
		s2 = self.sign(y2-y1)

		if dy>dx:
			dx, dy = dy, dx
			interchange = 1
		else:
			interchange = 0
#parametro de revision de la ecuacion 
		print("dx : ",dx,"\ndy : ",dy)
		e = 2*dy - dx
		print("e : ",e)
		print("interchange :", interchange,"\n")
		#display list
		x_list = []
		y_list = []
		x_ = []
		y_ = []
		e_ = []
#Insertado de los valores en la lista 
		for i in range(dx):
				x_list.append(x)
				y_list.append(y)
				while(e>=0):
					if interchange==1:
						x = x +s1
						
					else:
						y = y + s2
						
					e = e - 2*dx
				if interchange==1:
					y = y + s2
					
				else:
					x = x + s1
					

				e = e + 2*dy
				e_.append(e)

		pd.set_option('display.max_colwidth', None)
		print(pd.DataFrame({"X":x_list, "Y":y_list,"e":e_}))

		plt.scatter(x_list, y_list, color='red')
		plt.plot(x_list, y_list)
		plt.show()