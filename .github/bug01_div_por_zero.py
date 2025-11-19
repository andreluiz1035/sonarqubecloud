# exemplo_bug.py

def divide_numbers(a, b):
    # BUG: não trata divisão por zero
    return a / b

def main():
    x = 10
    y = 0  # Isso vai causar ZeroDivisionError
    result = divide_numbers(x, y)
    print(f"Resultado: {result}")

if __name__ == "__main__":
    main()
