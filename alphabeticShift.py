def solution(inputstring):
    ans = [ord(x) for x in inputstring]
    ans3 = ""
    return ans3.join([chr(x-25) if x == 122 else chr(x+1) for x in ans])