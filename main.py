import os
import datetime
from generator import flat_generator

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            with open(path, "a", encoding='utf-8') as f:
                name = old_function.__name__
                date = datetime.datetime.now()
                result = old_function(*args, **kwargs)
                f.write(str(date))
                f.write(', ' + str(name))
                f.write(', ' + str(args) + str(kwargs))
                f.write(', ' + str(result) + '\n')
            return result

        return new_function

    return __logger

list_of_lists_1 = [
         ['a', 'b', 'c'],
         ['d', 'e', 'f', 'h', False],
         [1, 2, None]
     ]
@logger('log_1.log')
def flat_generator(list_of_lists):
    return flat_generator

flat_generator(list_of_lists_1)