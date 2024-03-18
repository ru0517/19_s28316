from square_generator_package.square_generator import CubicGenerator

cubic_gen = CubicGenerator()
start = 1
end = 5
try:
    cubes = cubic_gen.generate_squares(start, end)
    print("Cubes:", cubes)
except ValueError as e:
    print(e)
