# Tasks

## Task 1

Model steady-state and full-developed axial flow of incompressible Newtonian fluid in cylindrical pipe assuming axisymmetric flow with no radial velocity.

- Formulate the PDE by simplifying the Navier Strokes equations for cylindrical coordinates.
- Convert the PDE into difference equation using Eq 15 and Eq 16.

## Task 2

Write a Python program to solve the system of linear equations obtained from difference equations to solve for $u_z$ as a function of $r$,
and plot the $u_z$ as a function of $r$ to visualize the velocity profile in the pipe for the given [Boundary condition](#boundary-conditions) and [Parameters](#parameters).

## Task 3

Write a Python program to model flow in pipe, where viscosity of the fluid is temperature dependent given by Eq 17, and the temperature varies with radius as given by Eq 18.

$$\mu(T) = \mu_0 (1 + \alpha (T - T_0))(17)$$

$$T(r) = T_0 + \beta r^2 (18)$$

## Task 4

Consider the model for the flow of an incompressible Newtonian fluid in a pipe where the velocity profile $u_z$ varies with both radial ($r$) and axial ($z$) coordinates, according to Eq 19.

- Write Python program to solve the system of linear equations obtained by converting the Eq 19 into difference equation.
- Plot the velocity profile as a function of radial ($r$) coordinate at $z = L/2$, $z = 0$ and $z = L$.
- Plot the velocity as function of axial ($z$) coordinate at $r = 0$ $r = R/2$ and $r = R$.

$$
\mu \left( \frac{\partial^2 u_z}{\partial r^2} + \frac{1}{r} \frac{\partial u_z}{\partial r} \right) + \gamma \frac{\partial^2 u_z}{\partial z^2} = \frac{\partial p}{\partial z}
(19)
$$

## Boundary Conditions

- At $r = 0$, $\frac{\partial u_z}{\partial r} = 0$
- At $r = R$, $u_z = 0$
- At $z = 0$, $u_z = 15$
- At $z = L$, $u_z = 15$

## Parameters

- Pipe Diameter $D = 0.1$ m
- Pipe Length $L = 1$ m
- Viscosity $\mu = 0.01$ kg/m.s
- Constant pressure gradient $\frac{\partial p}{\partial z} = -100$ Pa/m
- Choose $N = 100$ (or more) grid points
- Base viscosity $\mu_0 = 0.05$ kg/m.s
- Temperature expansion coefficient $\alpha = 0.08$ 1/K
- Reference temperature $T_0 = 273$ K
- $\beta$ = $5$ K/m$^2$
- $\gamma$ = 0.25

## Deliverable

1. `solution.py` Python script containing the implementation of the task 2, task 3, and task 4 solutions.
2. Report describing your approach, understanding of continuous dynamics modelling, and your observations.

## Evaluation Criteria

- Correct implementation of the finite difference equation.
- Successful solving of the system of linear equations.
- Interpretation of the results.
- Quality of report.
