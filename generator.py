import types


def flat_generator(list_of_lists):
  i = 0
  j = 0
  while i < len(list_of_lists):
    while j < len(list_of_lists[i]):
       yield list_of_lists[i][j]
       j += 1
    j = 0
    i += 1


list_of_lists_1 = [
         ['a', 'b', 'c'],
         ['d', 'e', 'f', 'h', False],
         [1, 2, None]
     ]