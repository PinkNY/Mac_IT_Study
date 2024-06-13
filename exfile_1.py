num = int(input('Enter an integer: '))
print()
if num <= 0:
    print(f"{num} is neither a multipule of 3 nor a multiple of 4.")
elif num % 3 == 0 and num % 4 == 0:
    print(f"{num} is a multipule of 3 and a multipule of 4.")
elif num % 4 == 0:
    print(f"{num} is a multipule of 4.")
elif num % 3 == 0:
    print(f"{num} is a multipule of 3.")
else:
    print(f"{num} is neither a multipule of 3 nor a multiple of 4.")
print()

