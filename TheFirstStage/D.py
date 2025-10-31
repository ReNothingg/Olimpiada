def is_upper_A_to_Y(ch):
    return 'A' <= ch <= 'Y'

def is_lower_a_to_y(ch):
    return 'a' <= ch <= 'y'

def to_second_from_first(s):
    parts = s.split('-')
    out = []
    for i, p in enumerate(parts):
        if i == 0:
            out.append(p.lower())
        else:
            out.append(p[0].upper() + p[1:].lower() if len(p) > 0 else '')
    return ''.join(out)

def to_first_from_second(s):
    words = []
    i = 0
    n = len(s)

    j = i
    while j < n and is_lower_a_to_y(s[j]):
        j += 1
    words.append(s[i:j].upper())
    i = j
    while i < n:
        j = i + 1
        while j < n and is_lower_a_to_y(s[j]):
            j += 1
        words.append(s[i:j].upper())
        i = j
    return '-'.join(words)

import sys

n_line = sys.stdin.readline().strip()
if not n_line:
    print("Error!")
    sys.exit(0)
try:
    n = int(n_line)
except:
    print("Error!")
    sys.exit(0)

s = sys.stdin.readline().strip()
if len(s) != n:
    print("Error!")
    sys.exit(0)

is_first = True
if s[0] == '-' or s[-1] == '-':
    is_first = False
else:
    prev_dash = False
    for ch in s:
        if ch == '-':
            if prev_dash:
                is_first = False
                break
            prev_dash = True
        else:
            prev_dash = False
            if not is_upper_A_to_Y(ch):
                is_first = False
                break

is_second = True
if '-' in s:
    is_second = False
else:
    if n == 0:
        is_second = False
    else:
        if not is_lower_a_to_y(s[0]):
            is_second = False
        else:
            i = 1
            while i < n:
                ch = s[i]
                if is_upper_A_to_Y(ch):
                    i += 1
                    if i < n and not (is_lower_a_to_y(s[i]) or is_upper_A_to_Y(s[i])):
                        is_second = False
                        break
                elif is_lower_a_to_y(ch):
                    i += 1
                else:
                    is_second = False
                    break

if not is_first and not is_second:
    print("Error!")
    sys.exit(0)

if is_first:
    parts = s.split('-')
    valid = all(len(p) > 0 for p in parts)
    if not valid:
        print("Error!")
    else:
        print(to_second_from_first(s))
else:
    print(to_first_from_second(s))
