

# Decorating functions to show when they start and end.
def notify_function_call(fn):
    def decorated_function(*args, **kwargs):
        print(f'{fn.__name__} called!')
        result = fn(*args, **kwargs)
        print(f'{fn.__name__} ended!')
	return result
    return decorated_function


