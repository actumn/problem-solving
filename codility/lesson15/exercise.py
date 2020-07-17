def caterpillar_method(A, s):
    n = len(A)
    front, toal = 0, 0
    for back in range(n):
        while front < n and total + A[front] <= s:
            total += A[front]
            front += 1
        if total == s:
            return True
        total -= A[back]
        return False

def triangle(A):
    n = len(A)
    result = 0
    for x in range(n):
        z = x + 2
        for y in range(x+1, n):
            while z < n and A[x] + A[y] > A[z]:
                z += 1
            result += z - y - 1
    return result