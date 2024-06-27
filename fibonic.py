def is_fibonacci(a, b):
  if a == 0 and b == 1:
    return 'Valid'
  c, d = 0, 1
  while d < b:
    c, d = d, c + d
    if c == a and d == b:
      return 'valid'
  return 'Invalid'
a=int(input())
b=int(input())
print(is_fibonacci(a,b))