

matrix1= [[0,5,1],
          [4,9,0],
          [0,6,0]]

matrix2= [[5,5,1],
          [5,8,1],
          [9,2,6]]


def add(m1,m2):
    new_matrix = []
    for row in range(len(m1)):
        rows=[]
        for cln in range(len(m1)):
            rows.append(m1[row][cln]+m2[row][cln])
        new_matrix.append(rows)
    print(new_matrix)
add(matrix1,matrix2)