numbers = []

for i in range(3):
    i = int(input("Insira o número: "))
    numbers.append(i)

print(f"O maior número entre os 3 inseridos é: {max(numbers)}")
print(f"E o menor número entre os 3 inseridos é: {min(numbers)}")