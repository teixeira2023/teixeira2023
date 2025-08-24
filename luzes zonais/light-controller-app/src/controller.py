class LightController:
    def __init__(self):
        self.lights = {
            'light1': 0,
            'light2': 0,
            'light3': 0,
            'light4': 0
        }

    def set_intensity(self, light_name, intensity):
        if light_name in self.lights and 0 <= intensity <= 3:
            self.lights[light_name] = intensity
        else:
            raise ValueError("Invalid light name or intensity level")

    def get_state(self):
        return self.lights