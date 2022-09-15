LIST = [15, 21, 13, 10, 5, 3]

def present(L, e):
    for i in range(len(L)):
        if e == L[i]:
            return True
    return False

print(present(LIST, 6))

def test_present(present:callable):
    pass