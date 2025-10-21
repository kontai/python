vars = 2


def __getattr__(name):
    print(f'(virtual name {name})',end=' ')
    match name:
        case 'test':
            return name * vars
        case 'hack' | 'code':
            return str.upper(name)
        case _:
            raise AttributeError(f'{name} is undefined')


def __dir__():
    return ['test', 'hack', 'code', 'vars']
