numbersTaken =[2,3,4,5]
print("print the numbers from 1 to 10 except these")
for n in range(1,10):
    if n in numbersTaken:
        continue
    else:
        print(n)
print("functions and return")
def allowed_age(my_age):
    girls_age=my_age/2+7
    return girls_age
bucky=allowed_age(27)
print(bucky)

def marriage_age(my_ages):
    age=my_ages/2+7
    return age
for i in range(15,25):
    a=marriage_age(i)
    print(a)
print("dafault values")

def get_gender(sex="unknown"):
    if sex is 'm':
        sex="male"
    elif sex is 'f':
        sex="female"
    print(sex)
a=get_gender()
print("//VARIABLE SCOPE//")

def corn():
    a=12
    print(a)
def fudge():
    a=14
    print(a)
fudge()
corn()
print("///KEYWORD ARGUMENTS///")
def name(a="i",b="am",c="stupid"):
    print(a,b,c)
name()
name(a="you",b="are")
name(c="mental")
name("i","love","apple")
name(c='idiot')
print("///FLEXIBLE NUMBER OF ARGUMENTS///")
def mul_numbers(*args):
    product=1
    for a in args:
        product*=a
    print(product)
mul_numbers(2)
mul_numbers(2,3)
mul_numbers(2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,10)

print("///FACTORIAL///")
def factorial(n):
  fact=1
  for i in range(1,n+1):
    fact*=i
  print(fact)
factorial(5)

print("///POWER///")
def power(x,y):
    pow=1
    for i in range(1,y+1):
        pow*=x
    print(pow)
power(3,4)

print("///CHECK PRIME///")
def check_prime(n):
    count=0
    if n>1:
        if n==2:
            count=0
        else:
          for i in range(2,n-1):
            if n%i==0:
             count+=1
             break
    else:
        count=1
    if count==0:
        print("YES")
    else:
        print("NO")
check_prime(2)
check_prime(9)
check_prime(3)
check_prime(1)
print("///PRINT ALL PRIME FROM X TO Y///")
def prime(x,y):
    for i in range(x,y+1):
        count=0
        if i==1:
            count=1
        else:
         for j in range(2,i-1):
            if(i%j==0):
                count+=1
                break
        if(count==0):
            print(i)
prime(1,20)
print("///SWAP TWO NUMNERS USING EXTRA VARIABLE///")
def swap(a,b):
    c=a
    a=b
    b=c
    print(a,b)
swap(2,3)
print("///SWAP TWO NUMBERS WITHOUT OTHER VARIABLE///")
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)
swap(2,3)
print("///REVERSE OF A NUMBER///")
def reverse(n):
    rev=0
    while(n!=0):
        d=n%10
        rev=rev*10 + d
        n=n//10
    print(rev)
reverse(23)
reverse(324)
reverse(5678)
print("///CHECK THE SIGN OF NUMBER///")
def sign(n):
    if(n>0):
        print("positive number")
    elif (n<0):
        print("negative number")
    else:
        print("number is zero")
sign(-7)
print("///SQUARE ROOT OF A NUMBER///")
import math
def square_root(a):
    print(math.sqrt(a))
square_root(5)
square_root(25)

print("///CHECK FOR PALINDROME///")
def palindrome(a):
    rev=0
    c=a
    while(a!=0):
        d=a%10
        rev=rev*10+d
        a=a//10
    if(rev==c):
        print("number is palindrome")
    else:
        print("not palindrome")
palindrome(121)
print("///PRINT ALL PALINDROME BETWEEN TWO NUMBERS")
def print_palindrome(a,b):
    for i in range(a,b+1):
        rev=0
        c=i
        while(i!=0):
            d=i%10
            rev=rev*10+d
            i=i//10
        if(rev==c):
            print(c)
print_palindrome(100,120)
print("///PATTERN///")
def pattern(n):
 for i in range(1,n+1):
    for j in range(i):
        print("*",end='')
    print("")
 for i in range(1,n):
    for j in range(n-i):
        print("*",end="")
    print("")
pattern(6)
print("///CHECK IF NUMBER IS ARMSTRONG")
def armstrong(n):
    c=n
    sum=0
    while(n!=0):
        d=n%10
        sum=sum+(d*d*d)
        n=n//10
    if(sum==c):
        print("number is armstrong")
    else:
        print("not armstrong")
armstrong(153)
armstrong(212)
print("///PRINT ALL ARMSTRONG NUMBERS BETWEEN TWO NUMBERS")
def print_armstrong(a,b):
    for i in range(a,b+1):
        sum=0
        c=i
        while(i!=0):
            d=i%10
            sum=sum+(d*d*d)
            i=i//10
        if(sum==c):
            print(c)
print_armstrong(150,155)
print_armstrong(1,500)
#n=int(input())
# for i in range(1,11):
    #p=n*i
    #print(n,'*',i,'=', p )
print("///FIBONACCI///")
def fibonacci(n):
    #for i in range(1,n+1):
        if n<=1:
            return n
        else:
           return(fibonacci(n-1)+fibonacci(n-2))
        print(a)
a=fibonacci(5)
print(a)
print("///NUMBER PATTERN")
for i in range(1,6):
    for j in range(i):
      print(i,end='')
    print("")

print("//NUMBER PATTERN 2///")
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")
for i in range(1,6):
    for j in range(i-1,-1,-1):
        print(2**j,end=' ')
    print('')


print("///UNPACKING ARGUMENTS///")
def calculator(a,b,c):
    ans=(100-a)+(b)+c
    print(ans)
list=[100,2,3]
calculator(list[0],list[1],list[2])
calculator(*list)
print(list)
print(*list)

print("///GROCERY LIST///")
groceries={"milk","cereal","beer","milk"}
print(groceries)
print(*groceries)
if 'milk' in groceries:
    print("you already have milk")
else:
    print("oh yes,you have milk")
print(groceries)

print("///KEY AND VALUES///")
array={'a':'lucy','b':'tony','c':'tuna'}
print(array)
print(array['a'])



