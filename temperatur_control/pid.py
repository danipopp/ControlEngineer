class PIDController:
    def __init__(self, kp, ki, kd, output_limits=(0, 100)):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.min_output, self.max_output = output_limits
        self.integral = 0.0
        self.prev_error = 0.0

        self.initilizeController = True

    def compute(self, setpoint, measurement, dt):
        error = setpoint - measurement

        self.integral += error * dt

        if self.initilizeController:
            derivative = 0

            self.initilizeController = False # Initilization done
        else:
            derivative = (error - self.prev_error) / dt

        p_part = self.kp * error
        i_part = self.ki * self.integral
        d_part = self.kd * derivative

        output = (p_part + i_part + d_part)

        # Clamp output
        output = max(self.min_output, min(self.max_output, output))

        self.prev_error = error
        return output, p_part, i_part, d_part
