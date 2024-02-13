from utils import *

#========================================================================================#
#calculating the particles movement given the initial conditions

s,v,err = particles_movement(v0_arr,s0_arr,p, t_end,dt,method='heun')

#========================================================================================#
#Writing the results in text files

errf = open('textfiles/error_heun.txt', 'w')
for i in range(s.shape[2]-1):
    errf.write(f"{err[0][i]},{err[1][i]},{err[2][i]}\n")
errf.close()

posf = open('textfiles/positions_heun.txt', 'w')
velf = open('textfiles/velocities_heun.txt', 'w')
for i in range(s.shape[0]):
    for line in range(s.shape[2]-1):
        posf.write(f"{s[i][0][line]},{s[i][1][line]},{s[i][2][line]}\n")
        velf.write(f"{v[i][0][line]},{v[i][1][line]},{v[i][2][line]}\n")
    posf.write(f"{s[i][0][s.shape[2]-1]},{s[i][1][s.shape[2]-1]},{s[i][2][s.shape[2]-1]}\n")
    velf.write(f"{v[i][0][s.shape[2]-1]},{v[i][1][s.shape[2]-1]},{v[i][2][s.shape[2]-1]}\n")

posf.close()
velf.close()


contents = readtxt('positions_heun.txt')

fig=plt.figure()
fig.suptitle(' Individual Particle Trajectiories')
ax = fig.add_subplot(111)
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)

ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax.set_xlabel('x [mM]')
ax.set_ylabel('z/y [mM]')

ax1.set_xlim(-LIM, LIM)
ax1.set_ylim(-LIM, LIM)
ax1.add_patch(Circle((0,0), RE, color='b', zorder=100))


ax2.set_xlim(-LIM, LIM)
ax2.set_ylim(-LIM, LIM)
ax2.add_patch(Circle((0,0), RE, color='b', zorder=100))


ax3.set_xlim(-LIM, LIM)
ax3.set_ylim(-LIM, LIM)
ax3.add_patch(Circle((0,0), RE, color='b', zorder=100))


ax4.set_xlim(-LIM, LIM)
ax4.set_ylim(-LIM, LIM)
ax4.add_patch(Circle((0,0), RE, color='b', zorder=100))
ax4.arrow(-2*RE*np.sin(alpha),-2*RE*np.cos(alpha),4*RE*np.sin(alpha),4*RE*np.cos(alpha),color='k',head_width=0.25*RE,zorder = 99)


ax5.set_xlim(-LIM, LIM)
ax5.set_ylim(-LIM, LIM)
ax5.add_patch(Circle((0,0), RE, color='b', zorder=100))
ax5.arrow(-2*RE*np.sin(alpha),-2*RE*np.cos(alpha),4*RE*np.sin(alpha),4*RE*np.cos(alpha),color='k',head_width=0.25*RE,zorder = 99)


ax6.set_xlim(-LIM, LIM)
ax6.set_ylim(-LIM, LIM)
ax6.add_patch(Circle((0,0), RE, color='b', zorder=100))
ax6.arrow(-2*RE*np.sin(alpha),-2*RE*np.cos(alpha),4*RE*np.sin(alpha),4*RE*np.cos(alpha),color='k',head_width=0.25*RE,zorder = 99)

ax1.plot(contents[0,0,:],contents[0,1,:], color = 'red')
ax1.set_ylabel('View of the xy plane')
ax2.plot(contents[1,0,:],contents[1,1,:], color = 'green')
ax3.plot(contents[2,0,:],contents[2,1,:], color = 'orange')
ax4.plot(contents[0,0,:],contents[0,2,:], color = 'red')
ax4.set_ylabel('View of the xz plane')
ax5.plot(contents[1,0,:],contents[1,2,:], color = 'green')
ax6.plot(contents[2,0,:],contents[2,2,:], color = 'orange')

fig.savefig('plots/trajheun.pdf')
