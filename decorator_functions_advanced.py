
def logging(function):
    def wrapper_function(*args):
        print(f"You called : {function.__name__}{args}")
        return function(*args)
    return wrapper_function


a=1
b=9
c=3
@logging
def logger_function(*args):
    print(sum(args))

logger_function(a,b,c)
