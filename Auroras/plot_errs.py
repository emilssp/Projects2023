from utils import *

err_euler = readerr('error.txt')
err_heun = readerr('error_heun.txt')
steps = np.arange(0, t_end/dt)

fig = plt.figure()
fig.suptitle('Relative error as function of step number')
ax = fig.add_subplot(111)
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)
ax.set_ylabel('Error [%]')
ax.set_xlabel('Step')
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot(steps,err_euler[:,0],color = 'red')
ax1.plot(steps,err_euler[:,1],color = 'green')
ax1.plot(steps,err_euler[:,2],color = 'orange')
ax1.set_ylabel('Error for Euler\'s method')

ax2.plot(steps,err_heun[:,0],color = 'red')
ax2.plot(steps,err_heun[:,1],color = 'green')
ax2.plot(steps,err_heun[:,2],color = 'orange')
ax2.set_ylabel('Error for Heun\'s method')

fig.savefig('plots/err.pdf')