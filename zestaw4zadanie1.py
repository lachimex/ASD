t = [[0] * 5 for _ in range(5)]
n = len(t)
size = n - 1
y, x, counter = 0, 0, 0
ruchy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while size > 0:
    for ruch in ruchy:
        a, b = ruch
        for i in range(size):
            counter += 1
            t[y][x] = counter
            x = x + a
            y = y + b
    size -= 2
    x += 1
    y += 1
if size == 0:
    t[y][x] = counter + 1
print(t)