from functools import singledispatch


@singledispatch
def func(a):
    print(f'Other: {a}')


@func.register(int)
def _(a):
    print(f'Int: {a}')


@func.register(float)
def _(a):
    print(f'Float: {a}')

@func.register(str)
def _(a):
    print(f"Str:{a}")

if __name__ == '__main__':
    func('zzz')
    func(1)
    func(1.2)
    func("c")
