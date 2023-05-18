import sys

def adding(x, y):
    return x + y

def main():
    if len(sys.argv) != 3:
        print("Please provide two numbers as command-line arguments.")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        result = adding(x, y)
        print(f"Sum of {x} and {y} is {result}")

if __name__ == "__main__":
    main()
