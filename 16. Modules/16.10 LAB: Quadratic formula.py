# TODO: Import math module
import cmath

def quadratic_formula(a, b, c):
    # TODO: Compute the quadratic formula results in variables x1 and x2
    d = (b**2) - (4*a*c)

# find two solutions
    x1 = (-b-cmath.sqrt(d))/(2*a)
    x2 = (-b+cmath.sqrt(d))/(2*a)  
    return (x2.real, x1.real)
    

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print("{}{:.0f}".format(prefix_str, number))
    else:
        print("{}{:.2f}".format(prefix_str, number))
    

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])
    solution = quadratic_formula(a, b, c)
    print("Solutions to {:.0f}x^2 + {:.0f}x + {:.0f} = 0".format(a, b, c))
    print_number(solution[0], "x1 = ")
    print_number(solution[1], "x2 = ")
