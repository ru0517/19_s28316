from square_generator_package.square_generator import SquareGenerator

square_gen = SquareGenerator()
start = 1
end = 10
try:
    squares = square_gen.generate_squares(start, end)
    print(squares)
except ValueError as e:
    print(e)
