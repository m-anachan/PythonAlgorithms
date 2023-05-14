def solution(inputArray):
    path = 0
    for x in range(1, max(inputArray)+2):
        while path <= max(inputArray):
            path += x
            if path in inputArray:
                break
            elif path > max(inputArray):
                return x
        path = 0