import numpy as np
import matplotlib.pyplot as plt


#exponential growth of the prey population
def plot_expon_system(x_init, y_init, t_start, t_stop, _a,_b,_d,_g, dt):

	# initialize lists
	t_list = [t_start]; x_list = [x_init]; y_list = [y_init];

	t = t_start
	x = x_init
	y = y_init

	while t < t_stop:
			# calc new values for t, x, y
			t += dt
			x += (_a*x - _b*x*y)*dt
			y += (_d*x*y - _g*y)*dt

			# store new values in lists
			t_list.append(t)
			x_list.append(x)
			y_list.append(y)

	return [t_list,x_list,y_list]


#logistic growth of the prey population
def plot_log_system(x_init, y_init, t_start, t_stop, _a,_b,_d,_g,_K, dt):
	
	# initialize lists
	t_list = [t_start]; x_list = [x_init]; y_list = [y_init];

	t = t_start
	x = x_init
	y = y_init	

	while t < t_stop:
			# calc new values for t, x, y
			t += dt
			x += ( (_a*x*(_K - x) / _K) - _b*x*y)*dt
			y += (_d*x*y - _g*y)*dt

			# store new values in lists
			t_list.append(t)
			x_list.append(x)
			y_list.append(y)

	return [t_list,x_list,y_list]





def exp_dxdy(x,y):
	dx = (_a*x - _b*x*y)
	dy = (_d*x*y - _g*y)
	return ([dx,dy])
 
def log_dxdy(x,y):
	dx = ((_a*x*(_K - x)/_K)-_b*x*y)
	dy = (_d*x*y - _g*y)
	return ([dx,dy])


def vector_field(mode, x_max, y_max):

	X1 , Y1 = np.meshgrid(np.linspace(0, x_max,25),np.linspace(0,y_max,25))
	
	if mode =="exp":
		DXDY = exp_dxdy(X1, Y1)
	elif mode == "log":
		DXDY = log_dxdy(X1,Y1)

	DX=DXDY[0]
	DY=DXDY[1]

	M = (np.hypot(DX, DY))
	M[ M == 0] = 1.

	DX /= M
	DY /= M
	
	return ([DX,DY])


###################
### DRIVER CODE ###
###################
if __name__ == "__main__":

	x_init = 5
	y_init = 6
	t_start = 0 
	t_stop = 100
	_a = 1
	_b = 1
	_d = 1 
	_g = 1
	_K = 10
	dt = 0.01

	E = plot_expon_system(x_init, y_init, t_start, t_stop, _a, _b, _d, _g, dt)
	L = plot_log_system(x_init, y_init, t_start, t_stop, _a, _b, _d, _g, _K, dt)

	E_x_max = np.max(E[1])
	E_y_max = np.max(E[2])

	L_x_max = np.max(L[1])
	L_y_max = np.max(L[2])

	exp_v = vector_field("exp", E_x_max, E_y_max)	
	log_v = vector_field("log", L_x_max, L_y_max)
	
	EX1 , EY1 = np.meshgrid(np.linspace(0, E_x_max ,25),np.linspace(0, E_y_max, 25))
	LX1 , LY1 = np.meshgrid(np.linspace(0, L_x_max ,25),np.linspace(0, L_y_max, 25))

	fig, axs = plt.subplots(nrows=2,ncols=2)

	axs[0,0].set_title("Exponential Growth of the Predator-Prey population")
	axs[0,1].set_title("Logistic Growth of the Predator-Prey population")

	axs[0,0].set_ylabel("Species Population")
	axs[0,1].set_ylabel("Species Population")
	axs[0,0].set_xlabel("Time t")
	axs[0,1].set_xlabel("Time t")

	axs[1,0].set_ylabel("Predator Population")
	axs[1,1].set_ylabel("Predator Population")
	axs[1,0].set_xlabel("Prey Population")
	axs[1,1].set_xlabel("Prey Population")

	axs[0,0].plot(E[0],E[1], 'g', label="prey", linewidth=2)
	axs[0,0].plot(E[0],E[2], 'r', label="pred", linewidth=2)

	axs[0,1].plot(L[0],L[1], 'g', label="prey", linewidth=2)
	axs[0,1].plot(L[0],L[2], 'r', label="pred",linewidth=2)

	axs[1,0].plot(E[1],E[2], 'b', label="exp", linewidth=2)
	axs[1,0].quiver(EX1, EY1, exp_v[0], exp_v[1], pivot='mid', cmap=plt.cm.plasma)
	
	axs[1,1].plot(L[1],L[2], 'b', label="log", linewidth=2)
	axs[1,1].quiver(LX1, LY1, log_v[0], log_v[1], pivot='mid', cmap=plt.cm.plasma)
	
	axs[0,0].legend(loc="upper right")
	axs[0,1].legend(loc="upper right")
	axs[1,0].legend(loc="upper right")
	axs[1,1].legend(loc="upper right")


	plt.show()
	plt.close()
