def solution(name):
    if 47 < ord(name[0]) < 58:
        return False

    for x in range(len(name)):
        if ord(name[x]) < 48 or (57 < ord(name[x]) < 65) or (90 < ord(name[x]) < 95) or  ord(name[x]) == 96 or ord(name[x]) > 122:
            return False
    return True