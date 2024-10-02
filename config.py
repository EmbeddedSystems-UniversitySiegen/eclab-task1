"""
Paramters for the Simulation
"""
# Pipe parameters
D = 0.1         # Pipe diameter in meters
L = 1.0         # Pipe length in meters
R = D / 2       # Radius of the pipe

# Fluid properties
mu = 0.01       # Dynamic viscosity in kg/m.s
mu_0 = 0.05     # Base viscosity in kg/m.s
alpha = 0.08    # Temperature expansion coefficient in 1/K
dpdz = -100     # Pressure gradient in Pa/m


# Temperature model parameters
beta = 5        # Temperature parameter in K/m^2
gamma = 0.25    # Gamma parameter
T0 = 273        # Reference temperature in K

# Numerical parameters
N = 100         # Number of grid points

# Boundary conditions
# Dirichlet boundary condition for z = 0
duz_dr = 0  # velocity gradient at r = 0
u_z_R = 0  # velocity at z = R
u_z_0 = 15  # Velocity at z = 0, inlet
u_z_L = 15  # Velocity at z = L, outlet
