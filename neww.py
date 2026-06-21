def primeornot(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
        except ValueError:
            print("Enter an integer")
            sys.exit(1)
        print(f"{num} is prime" if primeornot(num) else f"{num} is not prime")
    else:
        print("Usage: python neww.py <number>")
