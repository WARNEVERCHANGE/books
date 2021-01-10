data = []
f = open('./../ege2021kp/18data/18-0.csv')
for row in f:
    data.append(list(map(int, row.strip().split(';'))))
for i in range(len(data)):
    print(*data[i])