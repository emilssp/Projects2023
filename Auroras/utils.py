import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle

m_p = 1.65e-27              #[kg] proton mass
q = 1.6e-19                 #[C] proton charge 
B0 = 45e-6                  #[T] Mean magnitude of the Earth's magnetic field 
RE = 6.378                  #[Mm](1e6 meter) Radius of Earth
alpha = np.radians(-9.6)    #tilt of the magnetic pole
m = -B0 * RE**3             #magnetic dipole moment
mz =  np.cos(alpha)         #magnetic dipole moment z component
mx =  np.sin(alpha)         #magnetic dipole moment x component
LIM = 7*RE

def acc (v, s): 
    x=s[0]
    y=s[1]
    z=s[2]
    r = np.sqrt(x**2+y**2+z**2)
    
    Bx = (m/r**3)*(3*(mx*x+mz*z)*x/r**2 - mx)
    By = (m/r**3)*(3*(mx*x+mz*z)*y/r**2)
    Bz = (m/r**3)*(3*(mx*x+mz*z)*z/r**2 - mz)
    
    v = np.array(v)
    v = (q * v)/m_p #factor qv/m together for simplicity
    
    ax = (v[1]*Bz - v[2]*By)
    ay = (v[2]*Bx - v[0]*Bz)
    az = (v[0]*By - v[1]*Bx)
    
    return np.array([ax,ay,az])

def solve_ode(v0,s0,t,dt):
    s = []
    v = []

    s.append(s0)
    v.append(v0)
    for i in range(0, len(t)):
        s.append(s[-1] + dt*v[-1])
        v.append(v[-1] + dt*acc(v[-1],s[-1]))

    return np.array(v).T,np.array(s).T

def solve_Heun(v0,s0,t,dt):
    s = []
    v = []

    s.append(s0)
    v.append(v0)
    for i in range(0, len(t)):
        k1v = acc(v[-1], s[-1])
        k1s = v[-1]
        k2v = acc(v[-1]+ dt * k1v, s[-1] + dt * k1s)
        k2s = v[i]+ dt * k1v
        s.append(s[-1] + 0.5*dt*(k1s+k2s))
        v.append(v[-1] + 0.5*dt*(k1v+k2v))

    return np.array(v).T,np.array(s).T

def particles_movement(v0,s0,p, t_end=10,dt=0.001, method = 'euler'):
    t = np.arange(0,t_end,dt)
    v = []
    s = []
    err = []

    if method == 'euler':
        for i in range(p):
            err_temp = []
            v_temp, s_temp = solve_ode(v0[i], s0[i], t,dt)
            v.append(v_temp)
            s.append(s_temp)
            for j in range(t.size):
                err_temp.append(((np.abs(np.linalg.norm(v_temp[:,j])) - np.abs(np.linalg.norm(v_temp[:,0])))/np.abs(np.linalg.norm(v_temp[:,0])))*100)
            err.append(err_temp)
    if method == 'heun':
        for i in range(p):
            err_temp = []
            v_temp, s_temp = solve_Heun(v0[i], s0[i], t,dt)
            v.append(v_temp)
            s.append(s_temp)
            for j in range(t.size):
                err_temp.append(((np.abs(np.linalg.norm(v_temp[:,j])) - np.abs(np.linalg.norm(v_temp[:,0])))/np.abs(np.linalg.norm(v_temp[:,0])))*100)
            err.append(err_temp)
        
    return np.array(s), np.array(v), np.array(err)

def readtxt (filename):
    filename = f"textfiles/{filename}"
    with open(filename) as f:
        contents = f.read().strip()
    contents=contents.split('\n')
    for i in range(len(contents)):
        contents[i]=np.array(contents[i].split(','),dtype='float')
    return np.array(np.split(np.array(contents),p)).transpose(0,2,1)

def readerr (filename):
    filename = f"textfiles/{filename}"
    with open(filename) as f:
        contents = f.read().strip()
    contents=contents.split('\n')
    for i in range(len(contents)):
        contents[i]=np.array(contents[i].split(','),dtype='float')
    return np.array(contents)

#========================================================================================#
v0 = 24         #[Mm/min] initial speed
p = 3           #number of protons
t_end = 100     #[min] 
dt = 0.0001     #[min] timestep

s1 = [-5*RE,0,RE]
s2 = [-4*RE,RE,RE]
s3 = [-4.5*RE,RE,0]
s0_arr = np.array([s1,s2,s3])

v1 = [v0*np.cos(np.pi/8),0,np.sin(np.pi/8)]
v2 = [v0*np.cos(np.pi/6),v0*np.sin(np.pi/6),0]
v3 = [v0*np.cos(np.pi/7)*np.cos(np.pi/4),v0*np.cos(np.pi/7)*np.sin(np.pi/4),np.sin(np.pi/7)]
v0_arr = np.array([v1,v2,v3])
