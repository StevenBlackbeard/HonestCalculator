group_1 = abs(int(input()))
group_2 = abs(int(input()))
group_3 = abs(int(input()))

desks_1 = group_1 // 2 + group_1 % 2
desks_2 = group_2 // 2 + group_2 % 2
desks_3 = group_3 // 2 + group_3 % 2

print(desks_1 + desks_2 + desks_3)

