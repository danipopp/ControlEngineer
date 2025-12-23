class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0

    def compute(self, error, velocity, dt):
        # Integral term
        self.integral += error * dt

        # Individual PID components
        p_term = self.kp * error
        i_term = self.ki * self.integral
        d_term = -self.kd * velocity   # derivative on measurement

        # Total control output
        pid_value = p_term + i_term + d_term

        return pid_value, p_term, i_term, d_term
