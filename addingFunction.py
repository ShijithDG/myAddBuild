def add(num1, num2):
    return num1 + num2

def main():
    one = input(int('enter first number : '))
    two = input(int('enter second number : '))
    print(f'result = {add(one, two)}')

if __name__ == "__main__":
    main()