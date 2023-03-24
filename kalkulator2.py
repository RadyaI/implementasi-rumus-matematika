num1 = 0
operator = '+'

while True:
    if operator == '+': 
        num2 = float(input("Masukkan angka: "))
        result = num1 + num2
    elif operator == '-':
        num2 = float(input("Masukkan angka: "))
        result = num1 - num2
    elif operator == '*':
        num2 = float(input("Masukkan angka: "))
        result = num1 * num2
    elif operator == '/':
        num2 = float(input("Masukkan angka: "))
        result = num1 / num2
    else:
        print("Operator tidak valid")
        break

    print(f"Hasil {operator} {num2} = {result}")
    num1 = result

    choice = input("Lanjut (y/n)? ")
    if choice.lower() == 'n':
        break

    operator = input("Masukkan operator (+, -, *, /): ")
