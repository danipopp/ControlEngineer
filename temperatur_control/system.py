class ThermalSystem:
    def __init__(self, ambient_temp=25.0, time_constant=15.0, heater_gain=0.5):
        self.T_env = ambient_temp
        self.tau = time_constant
        self.K = heater_gain
        self.temperature = ambient_temp

    def update(self, heater_power, dt):
        """
        heater_power: control signal (0–100)
        dt: time step
        """
        dT = (self.T_env - self.temperature) / self.tau + self.K * heater_power
        self.temperature += dT * dt
        return self.temperature
