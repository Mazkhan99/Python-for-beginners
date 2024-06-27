def is_fibonacci(n1, n2):
  if n1 == 0 and n2 == 1:
    return "Both numbers are in fibonacci series"
  if n1 < 0 or n2 < 0:
    return "Both numbers are not in fibonacci series"
  # Check if one of the given numbers is the sum of the other number and the number two places before it in the series
  if n1 == n2 + (n2 - n1) or n2 == n1 + (n1 - n2):
    return True
  # If none of the above conditions are met, the numbers are not part of the Fibonacci series
  else:
    return False

# Test the function with some examples
print(is_fibonacci(0, 1))  # True
print(is_fibonacci(3, 5))  # True
print(is_fibonacci(7, 13))  # True
print(is_fibonacci(8, 13))  # False
print(is_fibonacci(9, 15))  # False
