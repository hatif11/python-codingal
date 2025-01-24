def first():
    print('hello guys this my first function')

first()

def new(name):
    print(f'hello this is me {name}')

new('hatif')
#####
def solve(a,b):
    return a + b

print(solve(20 ,30))
#####
def recursion(n):
    if n==10:
        print('time,s up')
    else :
        print(n)
        recursion(n+1)

recursion(5)