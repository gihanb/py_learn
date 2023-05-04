num_list = []
i = 5

while i > 0:
    n = int(input(f"Enter {i} number? "))
    i -= 1
    num_list.append(n)


print(num_list)
num_list.sort()
print(num_list)
print(len(num_list))
print(num_list[len(num_list) - 2])

