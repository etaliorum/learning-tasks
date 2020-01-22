n = int(input())
n_count = n

if n_count >= 100:
    n_count = n_count % 100
if n_count > 20:
    n_count = n_count % 10

if n_count == 0 or 5 <= n_count <= 20:
    print(n, "программистов")
if n_count == 1:
    print(n, "программист")
if 2 <= n_count <= 4:
    print(n, "программиста")
