numbers = []
for i in range(3):
    num = int(input("Insira um numero: "))
    numbers.append(num)
numbers.sort(reverse=True)
print(numbers)