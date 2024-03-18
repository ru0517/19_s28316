#task1
squares_list = [x**2 for x in range(1, 11)]
print(squares_list)

#task2
def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]

start = 3
end = 7
squares = generate_squares(start, end)
print(squares)

#task3
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]

square_gen = SquareGenerator()
start = 2
end = 9
squares = square_gen.generate_squares(start, end)
print(squares)

#task4
import math
class SquareGenerator:
    def generate_squares(self, start, end):
        squares = [x ** 2 for x in range(start, end + 1)]
        return [math.sqrt(square) for square in squares]

square_gen = SquareGenerator()
start = 1
end = 10
squares = square_gen.generate_squares(start, end)
print(squares)


#task5
class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to the start.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return [math.sqrt(square) for square in squares]

square_gen = SquareGenerator()
start = 5
end = 4
try:
    squares = square_gen.generate_squares(start, end)
    print(squares)
except ValueError as e:
    print(e)


#task10
from square_generator_package.square_generator import CubicGenerator

cubic_gen = CubicGenerator()
start = 1
end = 5
try:
    cubes = cubic_gen.generate_squares(start, end)
    print("Cubes:", cubes)
except ValueError as e:
    print(e)


