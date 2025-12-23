import numpy as np
import matplotlib.pyplot as plt

from system import ThermalSystem
from pid import PIDController

# Simulation parameters
dt = 0.1
total_time = 100
time = np.arange(0, total_time, dt)

# Create system and controller
system = ThermalSystem(
    ambient_temp=25.0,
    time_constant=15.0,
    heater_gain=0.5
)

kp = 0.3
ki = 0.02
kd = 0.0

pid = PIDController(
    kp=kp,
    ki=ki,
    kd=kd,
    output_limits=(0, 100)
)

# Setpoint
setpoint = 60.0

# Data storage
temperature_history = []
control_history = []

p_history = []
i_history = []
d_history = []

# Simulation loop
for t in time:
    current_temp = system.temperature
    control_signal, p, i, d = pid.compute(setpoint, current_temp, dt)
    system.update(control_signal, dt)

    temperature_history.append(system.temperature)
    control_history.append(control_signal)
    p_history.append(p)
    i_history.append(i)
    d_history.append(d)

# Plot results
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(time, temperature_history, label="Temperature")
plt.axhline(setpoint, color="r", linestyle="--", label="Setpoint")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(time, control_history, label="Heater Power")
plt.ylabel("Power (%)")
plt.xlabel("Time (s)")
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
