"""
Fourth-order Runge-Kutta (RK4) solver for
first-order ordinary differential equations.

This module implements the classical
fourth-order Runge-Kutta method for solving
initial-value problems of the form

    y' = f(t, y)

with a given initial condition

    y(t0) = y0.

The solver computes the numerical solution
on a uniform time grid and returns the
discrete time values together with the
corresponding numerical solution.

Author: Maryam Asghari
Version: 1.0
Date: June 2026
"""

import numpy as np


def rk4_step(f, t, y, h):

    
    """
    Perform a single fourth-order
    Runge-Kutta (RK4) integration step.

 
    Parameters
    ----------
    f : callable
        Right-hand side of the ODE y' = f(t,y).
    t : float
        Current time.
    y : float
        Current solution value.
    h : float
        Time-step size.

    Returns
    -------
    float
        Solution after one RK4 step.
    """    

    k1 = f(t, y)

    k2 = f(
        t + h/2,
        y + h*k1/2
    )

    k3 = f(
        t + h/2,
        y + h*k2/2
    )

    k4 = f(
        t + h,
        y + h*k3
    )

    y_new = y + h*(k1 + 2*k2 + 2*k3 + k4)/6

    return y_new

def rk4_solver(f, t0, y0, t_end, h):


    """
    Solve a first-order ordinary differential
    equation using the classical RK4 methodon a uniform time grid. .

    Parameters
    ----------
    f : callable
        Right-hand side of the ODE y' = f(t, y).
    t0 : float
        Initial time.
    y0 : float
        Initial value y(t0).
    t_end : float
        Final time.
    h : float
        Time-step size.

    Returns
    -------
    t_values : ndarray
        Discrete time grid.
    y_values : ndarray
        Numerical solution at each time point.
    """ 
    y0 = np.atleast_1d(y0)

    m = y0.size 


    N = int((t_end - t0) / h)

    t_values = np.zeros(N + 1)
    y_values = np.zeros((N + 1, m))

    t_values[0] = t0
    y_values[0] = y0

    t = t0
    y = y0

   

    for i in range(N):
         y = rk4_step(f, t, y, h)
         t = t + h

         t_values[i + 1] = t
         y_values[i + 1] = y

    return t_values, y_values 
    
