"""
Paramters for the Simulation

Pipe Parameters:

D: Diameter of the pipe, determining the width of the pipe in meters.
L: Length of the pipe, defining the longitudinal distance of the pipe in meters.
R: Radius of the pipe, calculated as half the diameter.

Fluid Properties:

mu: Dynamic viscosity of the fluid, representing the internal friction within the fluid.
mu_0: Base viscosity, which serves as a reference viscosity for the fluid at a specific condition.
alpha: Temperature expansion coefficient, quantifying the rate at which fluid properties change with temperature.
dpdz: Pressure gradient along the length of the pipe, indicating the change in pressure per unit length.

Temperature Model Parameters:

beta: Temperature-dependent parameter, influencing how temperature changes affect the flow dynamics.
gamma: Additional temperature model parameter affecting temperature expansion behavior.
T0: Reference temperature used as a baseline for calculating temperature-related effects.
Numerical Parameters:

N: Number of grid points, defining the resolution of the numerical grid used for computations.

Boundary Conditions:

duz_dr: Velocity gradient at the pipe centerline (r = 0), representing symmetry conditions.
u_z_R: Velocity at the pipe wall (r = R), set to zero for no-slip boundary conditions.
u_z_0: Velocity at the pipe inlet (z = 0), representing the entry speed of the fluid.
u_z_L: Velocity at the pipe outlet (z = L), representing the exit speed of the fluid.

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
duz_dr = 0  # velocity gradient at r = 0
u_z_R = 0  # velocity at z = R
u_z_0 = 15  # Velocity at z = 0, inlet
u_z_L = 15  # Velocity at z = L, outlet
