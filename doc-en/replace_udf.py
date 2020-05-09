import functools
from pyspark.sql import functions

def pandas_udf(p1, p2):

    from functools import wraps
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapper

    return inner

functions.pandas_udf=pandas_udf
