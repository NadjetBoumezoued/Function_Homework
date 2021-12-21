#qst1
def palindrome(string):
	l = 0
	r = len(string) - 1
	
	while r >= l:
		if string[l] != string[r]:
			return False
		l = l+1
		r = r-1
	return True
print(palindrome('madam'))
 #qst2
def prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            
            if(n % x==0):
                return False
        return True             
print(prime(12))
#qst3
def exist(n):
   if n in range(2,200) :
       print("the number exist in the range")
   else:
        print("the number doesn't exist in the range")
exist(255)
#qst4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))
#qst5
def reverse(a):
    ra = a[::-1]
    print(ra)
reverse('hello')
#qst6
def sum(numbers):
    sum = 0
    for a in numbers:
        sum= sum+a
    return sum
print(sum((3,5,2,4,1)))
#qst7
def f(n1,n2,n3):

    if(n1>=n2) and (n1>=n3):

        max=n1

    elif(n2>=n1) and (n2>=n3):

        max=n2

    else:

        max=n3

    print("the max of the three numbers is",max)

f(5,9,3)