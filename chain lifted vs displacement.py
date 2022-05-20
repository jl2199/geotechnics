import numpy as np
import matplotlib.pyplot as plt

def length(z_w, H0, w):
    L = z_w * np.sqrt(((2*H0)/(w*z_w)) +1 )
    return L

def V(L_c, w):
    return L_c*w

def T(V0, H0):
    T = np.sqrt(V0**2 + H0**2)
    return T

def scope(T0, w, L_c):
    a = T0/w
    sc = a*np.arcsinh(L_c/a)
    return sc

# values for the suspended chain
D = 125 # rotor diameter
H0 = 5e6 #+750e3 # horizontal restraining force
z_w = 100 # depth of water
d = 142 # mm diameter of chain
w = 404*9.81 # kg/m of chain times gravity      to be optimised
s_b0 = 100 # m of on ground chain



L_c = length(z_w, H0, w)
V0 = V(L_c, w)
T0 = T(V0, H0)

a = H0/w

L_t = s_b0 + L_c # total length of chains (fixed)

y1 = np.linspace(0,100,1000)
x1 = a*np.arccosh(1 + y1/a) + s_b0

s_c0 = scope(T0, w, L_c)


#values for the embedded chain
Nc_chain = 9 # estimated
Nc_anchor = 12.57 # estimated
z_a = 13 #m depth of embedded anchor
mu1 = 8/(5*Nc_chain) # mu for chain interaction
mu2 = 8/(5*Nc_anchor) # mu for anchor interaction
Ab_anchor = 25 # m^2 for anchor

Q_ec = (2.5e-3*d*Nc_chain)*(z_a+7)*1000 # average bearing force for embedded chain
F_ec = mu1 * Q_ec # friction for embedded chain
Ta = Ab_anchor * Nc_anchor * (2*z_a + 7)*1000
theta_a = np.sqrt((2*z_a*Q_ec)/Ta) # angle of the anchor in rads

y2 = np.linspace(0, z_a,100)
x2 = -(z_a/theta_a)* np.log(y2/z_a)


x3 = np.linspace(0, s_b0, 500)
y3 = x3*0



#new load case
H = np.linspace(4.25e6, 5.75e6, 1000)
s_t = []
chain_lifted = []

for i in H:
    L_ci = length(z_w, i, w)
    s_bi = L_t - L_ci
    Vi = V(L_ci, w)
    Ti = T(Vi, i)
    ai = i/w

    s_ci = scope(Ti, w, L_ci)
    s_t.append(s_bi + s_ci)
    chain_lifted.append(s_b0 - s_bi)

s = np.array(s_t) - s_b0 - s_c0


plt.plot(s,chain_lifted)
plt.xlabel('Displacement (m)')
plt.ylabel('Length of chain lifted (m)')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.show()

