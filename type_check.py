from functools import wraps

def typed(*type_args, **type_kwargs):
    def dec(fn):
        @wraps(fn)
        def wrap(*args, **kwargs):
            for i, t in enumerate(type_args):
                if not isinstance(args[i], t):
                    print('pos {} argument {} type error'.format(i, args[i]))
                    return None
            for k, t in type_kwargs.items():
                if not isinstance(kwargs[k], t):
                    print('keyword argument {} => {} type error'.format(k, kwargs[k]))
                    return None
            return fn(*args, **kwargs)
        return wrap
    return dec

@typed(x=float,y=float)
def add(x,y):
    return x +y

print (add(x=1.5,y=1.5))
