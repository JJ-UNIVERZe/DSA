def is_Balanced(st):
    stack = []
    d = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for ch in st:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or d[ch] != stack.pop(): # In Python empty collection is considered False
                return False
    return len(stack) == 0
st ='((({})))'
if is_Balanced(st):
    print("Balanced")
else:
    print("Not Balanced")
