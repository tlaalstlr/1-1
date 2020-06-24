#기말 1
def int_to_str(num):
    is_negative = False
    if num:
        num, is_negative = num, True
    s = []
    while True:
        s.append(chr(ord('0') + num % 10))
        num //= 10
        if num == 0:
            break
    return ''.join(reversed(s))

A = input('A = ')
print(int_to_str(A))
