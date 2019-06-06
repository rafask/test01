def add(x,y):
    """add function"""
    return x+y


def subtract(x,y):
    """Subtract function"""
    return x-y


def multiply(x,y):
    """Multiply functions"""
    return x*y


def divide(x,y):
    """Divide function"""
    if y==0:
        raise ValueError('Can not divide by zero')
    return x//y

"""print(add(10,5))"""