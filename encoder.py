# Class to monitor a rotary encoder and update a value.  You can either read the value when you need it, by calling getValue(), or
# you can configure a callback which will be called whenever the value changes.

from gpiozero import RotaryEncoder


class Encoder:

    def __init__(self, leftPin, rightPin, callback=None):
        # NOTE: left, right is different from GPIO, to keep it "legacy"
        # swap values
        self.rotor = RotaryEncoder(rightPin, leftPin)
        self.rotor.when_rotated_clockwise = self.rotated_right
        self.rotor.when_rotated_counter_clockwise = self.rotated_left
        self.value = 0
        self.callback = callback
    def rotated_left(self):
        self.value = self.value - 1
        if self.callback is not None:
            self.callback(self.value)
    def rotated_right(self):
        self.value = self.value + 1
        if self.callback is not None:
            self.callback(self.value)

    def getValue(self):
        return self.value
