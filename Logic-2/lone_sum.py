def lone_sum(a, b, c):
    if a == b and b == c:
        return 0
    elif a == b:
        return c
    elif b == c:
        return a
    elif c == a:
        return b
    else:
        return a + b + c        
# sample
#def lone_sum(a, b, c):
#  sum = 0
#  if a != b and a != c: sum += a
#  if b != a and b != c: sum += b
#  if c != a and c != b: sum += c
#  
#  return sum