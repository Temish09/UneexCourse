def det3x3(matrix):
    result = 0
    result += matrix[0][0] * matrix[1][1] * matrix[2][2]
    result += matrix[0][1] * matrix[1][2] * matrix[2][0]
    result += matrix[0][2] * matrix[1][0] * matrix[2][1]
    result -= matrix[0][2] * matrix[1][1] * matrix[2][0]
    result -= matrix[0][1] * matrix[1][0] * matrix[2][2]
    result -= matrix[0][0] * matrix[1][2] * matrix[2][1]
    return result


matrix = eval(input())


result = 0

result += matrix[0][0] * det3x3((matrix[1][1:], matrix[2][1:], matrix[3][1:],))
A = ([matrix[1][0], *matrix[1][2:]], [matrix[2][0], *matrix[2][2:]], [matrix[3][0], *matrix[3][2:]],)
result -= matrix[0][1] * det3x3(A)
B = ([*matrix[1][0:2], matrix[1][-1]], [*matrix[2][0:2], matrix[2][-1]], [*matrix[3][0:2], matrix[3][-1]],)
result += matrix[0][2] * det3x3(B)
result -= matrix[0][3] * det3x3((matrix[1][:3], matrix[2][:3], matrix[3][:3],))

print(result)
