"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

     Attributes:
        start (int): The starting number of the serial generator.
        current (int): The current number generated by the generator.

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
        """
        Initializes the SerialGenerator with a starting number.

        Args:
            start (int): The starting number for the generator. Default is 0.
        """

        self.start = int(start)
        self.current = int(start)

    def __repr__(self):
        """Show representation."""

        return f"<SerialGenerator start={self.start} current={self.current}>"

    def generate(self):
        """
        Generates the next sequential number.

        Returns:
            int: The next sequential number.
        """

        current_value = self.current
        self.current += 1
        return current_value

    def reset(self):
        """
        Resets the generator to the original starting number.
        """
        self.current = self.start