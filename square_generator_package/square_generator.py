from abc import ABC, abstractmethod
import math


class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to the start.")

        cubes = [x ** 3 for x in range(start, end + 1)]
        return cubes

