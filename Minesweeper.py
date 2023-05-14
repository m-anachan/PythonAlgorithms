def solution(matrix):
    answer = list()
    answer2 = list()

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if 0 < x < len(matrix[y]) - 1 and 0 < y < len(matrix) - 1:
                answer.append(int(matrix[y][x + 1]) + int(matrix[y][x - 1])
                              + int(matrix[y - 1][x - 1]) + int(matrix[y - 1][x]) + int(matrix[y - 1][x + 1])
                              + int(matrix[y + 1][x - 1]) + int(matrix[y + 1][x]) + int(matrix[y + 1][x + 1]))
            elif x == 0 and y == 0:
                answer.append(int(matrix[y][x + 1]) + int(matrix[y + 1][x]) + int(matrix[y + 1][x + 1]))  # left top
            elif x == 0 and y == len(matrix) - 1:
                answer.append(int(matrix[y][x + 1]) + int(matrix[y - 1][x]) + int(matrix[y - 1][x + 1]))  # left bottom
            elif x == len(matrix[y]) - 1 and y == 0:
                answer.append(int(matrix[y][x - 1]) + int(matrix[y + 1][x]) + int(matrix[y + 1][x - 1]))  # right top
            elif x == len(matrix[y]) - 1 and y == len(matrix) - 1:
                answer.append(int(matrix[y][x - 1]) + int(matrix[y - 1][x]) + int(matrix[y - 1][x - 1]))  # right bottom
            elif x == 0 and 0 < y < len(matrix) - 1:
                answer.append(int(matrix[y][x + 1]) + int(matrix[y + 1][x]) + int(matrix[y + 1][x + 1])  # left border
                              + int(matrix[y - 1][x] + int(matrix[y - 1][x + 1])))
            elif x == len(matrix[y]) - 1 and 0 < y < len(matrix) - 1:
                answer.append(int(matrix[y][x - 1]) + int(matrix[y + 1][x]) + int(matrix[y + 1][x - 1])  # right border
                              + int(matrix[y - 1][x] + int(matrix[y - 1][x - 1])))
            elif len(matrix[y]) - 1 > x > 0 == y:
                answer.append(int(matrix[y][x + 1]) + int(matrix[y][x - 1]) + int(matrix[y + 1][x - 1])  # upper border
                              + int(matrix[y + 1][x]) + int(matrix[y + 1][x + 1]))
            elif 0 < x < len(matrix[y]) - 1 and y == len(matrix) - 1:
                answer.append(int(matrix[y][x + 1]) + int(matrix[y][x - 1]) + int(matrix[y - 1][x - 1])  # lower border
                              + int(matrix[y - 1][x]) + int(matrix[y - 1][x + 1]))
        answer2.append(answer)
        answer = list()

    return answer2