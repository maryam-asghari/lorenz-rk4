"""
Lorenz attractor simulation using the classical fourth-order Runge-Kutta (RK4) method.

This script demonstrates:

1. Solving the Lorenz system
2. Numerical integration using RK4
3. Time evolution of x, y, and z
4. Phase-space projections
5. Three-dimensional Lorenz attractor visualization

Author: Maryam Asghari
Version: 1.0
Date: June 2026
"""
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   #noqa: F401
import matplotlib as mpl


from rk4_solver import rk4_solver

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = PROJECT_ROOT / "figures"

FIGURES_DIR.mkdir(exist_ok=True)


SIGMA = 10.0
RHO = 28.0
BETA = 8.0 / 3.0

# ----------------------------------
# Configure Matplotlib
# ----------------------------------

mpl.rcParams["figure.dpi"] = 150
mpl.rcParams["savefig.dpi"] = 300
mpl.rcParams["font.size"] = 12
mpl.rcParams["axes.titlesize"] = 14
mpl.rcParams["axes.labelsize"] = 12


def lorenz(t, state):
    """
    Dimensionless Lorenz system.

    The governing equations are

        x' = sigma (y - x)
        y' = x (rho - z) - y
        z' = xy - beta z

    Parameters
    ----------
    t : float
       Time.

    state : ndarray
        State vector [x, y, z].
        

    Note
    ----
    The variable t is included only to match
    the solver interface.

    Returns
    -------
    ndarray
        Time derivatives.
    """ 

    x = state[0]
    y = state[1]
    z = state[2]


    return np.array([
        SIGMA*(y-x),
        x*(RHO-z)-y,
        x*y-BETA*z
    ])


def print_summary(t, x, y, z):
    """
    Print a summary of the Lorenz simulation.

    Parameters
    ----------
    t : ndarray
        Time array.

    x : ndarray
        x-component of the Lorenz solution.

    y : ndarray
        y-component of the Lorenz solution.

    z : ndarray
        z-component of the Lorenz solution.
    """
    print("Lorenz Attractor Simulation")
    print(f"Number of time steps = {len(t)}")
    print()

    print("Parameters:")
    print("-" * 20)
    print(f"sigma = {SIGMA}")
    print(f"rho   = {RHO}")
    print(f"beta  = {BETA:.6f}")
    print()

    print("Integration:")
    print("-" * 20)
    print(f"Time interval = [{t[0]:.1f}, {t[-1]:.1f}]")
    print(f"Step size     = {t[1]-t[0]:.3f}")
    print()

    print("Initial state:")
    print("-" * 20) 
    print(f"x(0) = {x[0]:.6f}")
    print(f"y(0) = {y[0]:.6f}")
    print(f"z(0) = {z[0]:.6f}")
    print()

    print("Final state:")
    print("-" * 20)
    print(f"x(T) = {x[-1]:.6f}")
    print(f"y(T) = {y[-1]:.6f}")
    print(f"z(T) = {z[-1]:.6f}")
    

# ----------------------------------
# Plot x(t)
# ----------------------------------

def plot_x(t, x):
    """
    Plot x versus time.

    Parameters
    ----------
    t : ndarray
        Time array.

    x : ndarray
        x-component of the Lorenz solution.
    """
    plt.figure()

    plt.plot(t, x)

    plt.xlabel(r"$t$")
    plt.ylabel(r"$x$")
    plt.title("Time Evolution of x")
    plt.grid(True)

    plt.savefig(
        str(FIGURES_DIR / "time_evolution_x.png"),
        dpi=300,
        bbox_inches="tight"
    )
    
    plt.close()
    
# ----------------------------------
# Plot y(t)
# ----------------------------------

def plot_y(t, y):
    """
    Plot y versus time.

    Parameters
    ----------
    t : ndarray
        Time array.

    y : ndarray
        y-component of the Lorenz solution.
    """
    plt.figure()

    plt.plot(t, y)

    plt.xlabel(r"$t$")
    plt.ylabel(r"$y$")
    plt.title("Time Evolution of y")
    plt.grid(True)

    plt.savefig(
        str(FIGURES_DIR / "time_evolution_y.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
   
# ----------------------------------
# Plot z(t)
# ----------------------------------

def plot_z(t, z):
    """
    Plot z versus time.

    Parameters
    ----------
    t : ndarray
        Time array.

    z : ndarray
        z-component of the Lorenz solution.
    """
    plt.figure()

    plt.plot(t, z)

    plt.xlabel(r"$t$")
    plt.ylabel(r"$z$")
    plt.title("Time Evolution of z")
    plt.grid(True)

    plt.savefig(
        str(FIGURES_DIR / "time_evolution_z.png"),
        dpi=300,
        bbox_inches="tight"
    )
    
    plt.close()
    
# ----------------------------------
# Plot x-y Projection
# ----------------------------------

def plot_xy(x, y):
    """
    Plot x versus y.

    Parameters
    ----------
    x : ndarray
        x-component of the Lorenz solution.
        
    y : ndarray
        y-component of the Lorenz solution.    
    """
    plt.figure()

    plt.plot(x, y)

    plt.xlabel(r"$x$")
    plt.ylabel(r"$y$")
    plt.title("Lorenz Attractor Projection onto the x-y Plane")
    plt.grid(True)

    plt.savefig(
        str(FIGURES_DIR / "projection_xy.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
    
# ----------------------------------
# Plot x-z Projection
# ----------------------------------

def plot_xz(x, z):
    """
    Plot x versus z.

    Parameters
    ----------
    x : ndarray
        x-component of the Lorenz solution.
        
    z : ndarray
        z-component of the Lorenz solution.    
    """ 
    plt.figure()

    plt.plot(x, z)

    plt.xlabel(r"$x$")
    plt.ylabel(r"$z$")
    plt.title("Lorenz Attractor Projection onto the x-z Plane")
    plt.grid(True)

    plt.savefig(
        str(FIGURES_DIR / "projection_xz.png"),
        dpi=300,
        bbox_inches="tight"
    )
    
    plt.close()
    
# ----------------------------------
# Plot y-z Projection
# ----------------------------------

def plot_yz(y, z):
    """
    Plot y versus z.

    Parameters
    ----------
    y : ndarray
        y-component of the Lorenz solution.
        
    z : ndarray
        z-component of the Lorenz solution.    
    """
    
    plt.figure()

    plt.plot(y, z)

    plt.xlabel(r"$y$")
    plt.ylabel(r"$z$")
    plt.title("Lorenz Attractor Projection onto the y-z Plane")
    plt.grid(True)

    plt.savefig(
        str(FIGURES_DIR / "projection_yz.png"),
        dpi=300,
        bbox_inches="tight"
    )
    
    plt.close()
    
# ----------------------------------
# Plot 3D Lorenz Attractor
# ----------------------------------

def plot_3d(x, y, z):
    """
    Plot the three-dimensional Lorenz attractor.

    Parameters
    ----------
    x : ndarray
        x-component of the Lorenz solution.

    y : ndarray
        y-component of the Lorenz solution.

    z : ndarray
        z-component of the Lorenz solution.

    Notes
    -----
    The trajectory is visualized in the three-dimensional phase space
    (x, y, z), where the characteristic butterfly-shaped strange
    attractor of the Lorenz system can be observed.
    """ 
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")

    # Plot Lorenz attractor
    ax.plot(x, y, z, color="C0", lw=0.4, alpha=0.85)

    # Configure axes
    ax.set_xlabel("x", labelpad=12)
    ax.set_ylabel("y", labelpad=12)
    ax.set_zlabel("z", labelpad=12)
    ax.set_title("Lorenz Attractor (Lorenz system)", pad=20)

    # Set axis limits
    ax.set_xlim(-20, 20)
    ax.set_ylim(-30, 30)
    ax.set_zlim(0, 50)

    # View angle (this one shows the "butterfly" best)
    ax.view_init(elev=24, azim=-60)

    # Configure grid and pane appearance 
    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.6)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0))

    # Ticks
    ax.tick_params(pad=5)
    ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(6))
    ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(6))
    ax.zaxis.set_major_locator(mpl.ticker.MaxNLocator(6))

    plt.tight_layout()

    plt.savefig(
        str(FIGURES_DIR / "lorenz_attractor_3d.png"),
        dpi=300,
        bbox_inches="tight"
    )
    
    plt.close(fig)

    
def main():
    """
    Run the complete Lorenz attractor simulation.

    This function

    1. Solves the Lorenz equations using the RK4 solver.
    2. Prints a summary of the simulation.
    3. Generates and saves all figures.
    """
    t, state = rk4_solver(
        lorenz,
        t0=0.0,
        y0=np.array([1.0, 1.0, 1.0]),
        t_end=40,
        h=0.01
    )
    
    # Extract solution components
    x = state[:, 0]
    y = state[:, 1]
    z = state[:, 2]

    print_summary(t, x, y, z)

    plot_x(t, x)
    plot_y(t, y)
    plot_z(t, z)

    plot_xy(x, y)
    plot_xz(x, z)
    plot_yz(y, z)

    plot_3d(x, y, z)

    
if __name__ == "__main__":
    main()
