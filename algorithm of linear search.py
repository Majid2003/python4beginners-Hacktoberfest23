def linear_search(array, target):
  """Returns the index of the target element in the array, or -1 if not found."""

  for i in range(len(array)):
    if array[i] == target:
      return i
  return -1

# Example usage:

array = [1, 3, 5, 7, 9]
target = 5

index = linear_search(array, target)

if index != -1:
  print("The target element was found at index {}.".format(index))
else:
  print("The target element was not found.")
