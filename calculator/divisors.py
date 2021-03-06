"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number."""


def main():
    num = int(input("Enter a number: "))

    divisors = Divisors(num)
    divisors.print_divisors()


class Divisors:
    def __init__(self, num):
        self.num = num
        self.divisors = []
        self.divisors.append(1)
        self.divisors.append(self.num)
        for i in range(2, self.num):
            if self.num % i == 0:
                self.divisors.append(i)

    def print_divisors(self):
        self.divisors.sort()
        print("The divisors of", self.num, "are", self.divisors)


if __name__ == "__main__":
    main()
