a=int(input("Enter the 1st number:"))
b=int(input("enter the 2nd number:"))
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a    

def lcm(a,b):
    return a*b // gcd(a,b)

g=gcd(a,b)
l=lcm(a,b)
print("GCD:",g)
print("LCM:",l)