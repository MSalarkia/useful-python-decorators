

# Decorating functions to show when they start and end.
def notify_function_call(fn):
    def decorated_function(*args, **kwargs):
        print(f'{fn.__name__} called!')
        result = fn(*args, **kwargs)
        print(f'{fn.__name__} ended!')
        return result

    return decorated_function


if __name__ == '__main__':
    @notify_function_call
    def sum_(*args):
        return sum(args)

    
    sum_(1,2,3,4,5,6,)