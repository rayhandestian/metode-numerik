def gauss_jordan(m, eps=1.0/(10**10)):
    (h, w) = (len(m), len(m[0]))
    for y in range(0,h):
        maxrow = y
        for y2 in range(y+1, h): # cari max di kolom
            if abs(m[y2][y]) > abs(m[maxrow][y]):
                maxrow = y2
        (m[y], m[maxrow]) = (m[maxrow], m[y])
        if abs(m[y][y]) <= eps: # singular?
            return False
        for y2 in range(y+1, h): # eliminasi ke bawah
            c = m[y2][y] / m[y][y]
            for x in range(y, w):
                m[y2][x] -= m[y][x] * c
    for y in range(h-1, 0-1, -1): # backsubstitute
        c = m[y][y]
        for y2 in range(0,y):
            for x in range(w-1, y-1, -1):
                m[y2][x] -=  m[y][x] * m[y2][y] / c
        m[y][y] /= c
        for x in range(h, w): # normalisasi row y
            m[y][x] /= c
    return True

# Sistem persamaan:
# 2x1 + 3x2 - x3 = 5
# 4x1 + 4x2 - 3x3 = 3
# -2x1 + 3x2 - x3 = 1

matrix = [
    [2, 3, -1, 5], 
    [4, 4, -3, 3], 
    [-2, 3, -1, 1]
]

if gauss_jordan(matrix):
    print(matrix[0][-1])
    print(matrix[1][-1])
    print(matrix[2][-1])
else:
    print("Sistem persamaan tidak dapat diselesaikan.")
