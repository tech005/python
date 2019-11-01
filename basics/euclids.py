# find greatest common denominator 
# of 2 numbers with Euclid's algorithm


def algorithm(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a

def getnumber():
    number = int(input("enter number: "))
    return number


def main():
    print("Enter 2 numbers and i will return lowest common denominator")
    a = getnumber()
    b = getnumber()
    print(algorithm(a, b))

main()