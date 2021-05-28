"""Python serial number generator."""


from warnings import resetwarnings


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start
        self.changed = start-1

    def generate(self):
        self.changed = self.changed+1
        return self.changed

    def reset(self):
        self.changed = self.start-1
