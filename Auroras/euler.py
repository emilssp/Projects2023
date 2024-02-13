from utils import *
#========================================================================================#
#Plot the magnetic field of earth in the xz plane

n = 100
vec=np.linspace(-LIM,LIM,n)

x,z = np.meshgrid(vec,vec)

r = np.sqrt(x**2+z**2)

Bx = (1/r**3)*(3*(mx*x + mz*z)*x/r**2 - mx)
Bz = (1/r**3)*(3*(mx*x + mz*z)*z/r**2 - mz)

fig, ax = plt.subplots()
fig.suptitle("Magnetic field of Earth in the xz-axis")
color = np.log(np.hypot(Bx, Bz))
cmap = plt.get_cmap('cividis')

h = ax.streamplot(x, z , Bx, Bz, linewidth=1,
              density=2,arrowstyle='->', color=color, arrowsize=1.5, cmap = cmap)
cbar = fig.colorbar(h.lines, ax=ax)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('B-field strength logarithmic scale', rotation=270)

# Add a filled circle for the Earth; make sure it's on top of the streamlines.
ax.add_patch(Circle((0,0), RE, color='b', zorder=100))
ax.axvline(x=0, linestyle='--', color = 'r')
ax.axhline(y=0, linestyle='--', color = 'r')
ax.arrow(-2*RE*np.sin(alpha),-2*RE*np.cos(alpha),4*RE*np.sin(alpha),4*RE*np.cos(alpha),color='k',head_width=0.25*RE,zorder = 99)
ax.set_xlabel('$x$ [Mm]')
ax.set_ylabel('$z$ [Mm]')
ax.set_xlim(-LIM, LIM)
ax.set_ylim(-LIM, LIM)
ax.set_aspect('equal')
fig.savefig('plots/mfieldxz.pdf')

#========================================================================================#
#Plot the magnetic field of earth in the xy plane

x,y = np.meshgrid(vec,vec)
r = np.sqrt(x**2+y**2)

Bx = (1/r**3)*(3*(mx*x + mz*z)*x/r**2 - mx)
By = (1/r**5)*(3*(mx*x + mz*z)*y)

fig, ax = plt.subplots()
fig.suptitle("Magnetic field of Earth in the xy-axis")
color = 2 * np.log(np.hypot(Bx, By))
cmap = plt.get_cmap('cividis')

h = ax.streamplot(x, y , Bx, By, linewidth=1,
              density=2,arrowstyle='->', color=color, arrowsize=1.5, cmap = cmap)
cbar = fig.colorbar(h.lines, ax=ax)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('B-field strength logarthimic scale', rotation=270)

# Add a filled circle for the Earth; make sure it's on top of the streamlines.
ax.add_patch(Circle((0,0), RE, color='b', zorder=100))
ax.axvline(x=0, linestyle='--', color = 'r')
ax.axhline(y=0, linestyle='--', color = 'r')
a = np.linspace(-3,3,10)
ax.set_xlabel('$x$ [Mm]')
ax.set_ylabel('$y$ [Mm]')
ax.set_xlim(-LIM, LIM)
ax.set_ylim(-LIM, LIM)
ax.set_aspect('equal')
fig.savefig('plots/mfieldxy.pdf')

#========================================================================================#
#calculating the particles movement given the initial conditions
s,v,err = particles_movement(v0_arr,s0_arr,p, t_end,dt)

#========================================================================================#
#Writing the results in text files

errf = open('textfiles/error.txt', 'w')
for i in range(s.shape[2]-1):
    errf.write(f"{err[0][i]},{err[1][i]},{err[2][i]}\n")
errf.close()

posf = open('textfiles/positions.txt', 'w')
velf = open('textfiles/velocities.txt', 'w')
for i in range(s.shape[0]):
    for line in range(s.shape[2]-1):
        posf.write(f"{s[i][0][line]},{s[i][1][line]},{s[i][2][line]}\n")
        velf.write(f"{v[i][0][line]},{v[i][1][line]},{v[i][2][line]}\n")
    posf.write(f"{s[i][0][s.shape[2]-1]},{s[i][1][s.shape[2]-1]},{s[i][2][s.shape[2]-1]}\n")
    velf.write(f"{v[i][0][s.shape[2]-1]},{v[i][1][s.shape[2]-1]},{v[i][2][s.shape[2]-1]}\n")

posf.close()
velf.close()

#========================================================================================#
#Reading the positions from positions.txt and plotting the results

contents = readtxt('positions.txt')
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

fig.savefig('plots/traj.pdf')