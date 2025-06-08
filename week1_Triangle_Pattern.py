# printing lower triange
def lower_tri(n):
    for i in range(1,n+1):
        print('* '*i)

# printing upper triangle
def upper_tri(n):
    for i in range(n,0,-1):
        print(((n-i)*'  ')+('* '*i))


# printing triangle pyramid
def pyramid_tri(n):
    for i in range(1,n+1):
        print(((n-i)*' ')+('* '*i))


def main():
    n=int(input('Enter the no. of lines of pattern : '))
    print('____LOWER TRIANGLE____\n')
    lower_tri(n)
    print('____UPPER TRIANGLE____\n')
    upper_tri(n)
    print('____TRIANGLE PYRAMID____\n')
    pyramid_tri(n)
main()
