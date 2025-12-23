import numpy as np
import matplotlib.pyplot as plt
from pid import PID
from system import MassSpringDamper

# =====================================================
# Physical parameters of the mass-spring-damper system
# =====================================================
m = 1.0     # Mass (kg)
c = 1.5     # Damping coefficient (Ns/m)
k = 20.0    # Spring stiffness (N/m)

# =====================================================
# PID controller gains
# =====================================================
kp = 20.0   # Proportional gain
ki = 15.0   # Integral gain
kd = 10.0    # Derivative gain (set to zero here)

# =====================================================
# Simulation time parameters
# =====================================================
dt = 0.001          # Time step (seconds)
t_final = 20.0       # Total simulation time (seconds)
time = np.arange(0, t_final, dt)

# =====================================================
# Initialize system and controller
# =====================================================
system = MassSpringDamper(m, c, k)  # Physical system model
pid = PID(kp, ki, kd)               # PID controller

# Initial state: [position, velocity]
state = np.array([0.0, 0.0])

# Desired position (step input)
reference = 1.0

# =====================================================
# Data storage for plotting
# =====================================================
x_history = []   # Position history
u_history = []   # Control force history

p_history = []
i_history = []
d_history = []


# =====================================================
# Main simulation loop (Euler integration)
# =====================================================
for t in time:
    error = reference - state[0]
    velocity = state[1]

    # Get PID output AND components
    u, p, i, d = pid.compute(error, velocity, dt)

    state_dot = system.dynamics(state, u)
    state = state + state_dot * dt

    # Store data
    x_history.append(state[0])
    u_history.append(u)
    p_history.append(p)
    i_history.append(i)
    d_history.append(d)


# =====================================================
# Plot simulation results
# =====================================================
plt.figure(figsize=(10, 8))

# -----------------------------
# Position response
# -----------------------------
plt.subplot(3, 1, 1)
plt.plot(time, x_history, label="Position")
plt.axhline(reference, linestyle="--", label="Reference")
plt.ylabel("Position (m)")
plt.legend()
plt.grid()

# -----------------------------
# Control force
# -----------------------------
plt.subplot(3, 1, 2)
plt.plot(time, u_history, label="Total Control Force")
plt.ylabel("Force (N)")
plt.legend()
plt.grid()

# -----------------------------
# PID components
# -----------------------------
plt.subplot(3, 1, 3)
plt.plot(time, p_history, label="P term")
plt.plot(time, i_history, label="I term")
plt.plot(time, d_history, label="D term")
plt.ylabel("PID Contribution (N)")
plt.xlabel("Time (s)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
