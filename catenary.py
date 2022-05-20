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

y1 = np.linspace(0,z_w,1000)
x1 = a*np.arccosh(1 + y1/a)# + s_b0

s_c = scope(T0, w, L_c)


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
H1 = 5.75e6

L_c1 = length(z_w, H1, w)
s_b1 = L_t - L_c1
V1 = V(L_c1, w)
T1 = T(V1, H1)
a1 = H1/w

s_c1 = scope(T1, w, L_c1)

y4 = np.linspace(0,100,1000)
x4 = a1*np.arccosh(1 + y4/a1) + s_b1

x5 = np.linspace(0, s_b1, 500)
y5 = x5*0


#new load case
H2 = 4.25e6

L_c2 = length(z_w, H2, w)
s_b2 = L_t - L_c2
V2 = V(L_c2, w)
T2 = T(V2, H2)
a2 = H2/w

s_c2 = scope(T2, w, L_c2)

y6 = np.linspace(0,100,1000)
x6 = a2*np.arccosh(1 + y6/a2) + s_b2

x7 = np.linspace(0, s_b2, 500)
y7 = x7*0
print(L_c, s_c, max(x1))
'''
print(s_c, L_c, T0)
print(L_c, L_t, s_c + s_b0)
print(L_c1, L_t, s_c1 + s_b1)
print(L_c2, L_t, s_c2 + s_b2)
print(min(x2-x2[1]))
'''
'''
s_0 = s_c + s_b0
s_1 = s_c1 + s_b1
s_2 = s_c2 + s_b2
print(2*s_0, s_1 + s_2/2 + s_0/2)
'''
plt.plot(x1,y1)
'''
plt.plot(x2-x2[1],-y2+y2[1])
plt.plot(x3,y3)
plt.plot(x4,y4)
plt.plot(x5,y5)
plt.plot(x6,y6)
plt.plot(x7,y7)
'''
plt.xlabel('Distance from touchdown point')
plt.ylabel('Height of water level from seabed')
plt.minorticks_on()
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.show()

