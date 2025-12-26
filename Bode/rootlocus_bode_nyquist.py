import control as ctrl
import matplotlib.pyplot as plt

# Define transfer function: G(s) = 1 / (s^2 + 3s + 2)
num = [1]
den = [1, 3, 2]
G = ctrl.TransferFunction(num, den)

# Root locus (plots automatically)
ctrl.root_locus(G)
plt.title("Root Locus of G(s)")
plt.show()

# Example PID: Kp = 5, Ki = 1, Kd = 0.1
Kp, Ki, Kd = 5, 1, 0.1
PID = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Compensated system
T = PID * G

# Bode plot (modern syntax)
ctrl.bode(T, dB=True)  # Do NOT unpack
plt.show()

# Compute stability margins
gm, pm, wg, wp = ctrl.margin(T)
print(f"Gain Margin: {gm:.2f}")
print(f"Phase Margin: {pm:.2f} degrees")
print(f"Gain Crossover Frequency: {wg:.2f} rad/s")
print(f"Phase Crossover Frequency: {wp:.2f} rad/s")
