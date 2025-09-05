x, y = map(lambda x: int(x) + 1, input().split(" "))
cut = [[False] * y, [False] * x]
cut[0][-1] = cut[1][-1] = True

for loop in range(0, int(input())):
    is_y, cut_num = map(int, input().split())
    cut[is_y][cut_num] = True

x_len_list = [0]
x_last_cut = 0
for i in range(1, x):
    if not cut[1][i]:
        continue
    x_len_list.append(i - x_last_cut)
    x_last_cut = i

y_len_list = [0]
y_last_cut = 0
for i in range(1, y):
    if not cut[0][i]:
        continue
    y_len_list.append(i - y_last_cut)
    y_last_cut = i

print(max(i * j for i in x_len_list for j in y_len_list))