#Write a program which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
#in a comma-separated sequence on a single line.

n=[]
for i in range(2000,3201):
    if i % 7 == 0:
        n.append(i)
print(int(n))


#Write a Python program to accept the user's first and last name and then getting them
#printed in the the reverse order with a space between first name and last name.

first_name =input("Enter your First Name : ")
last_name = input("Enter your Last Name : ")
full_name = first_name+" "+last_name
print("The reverse order of your name is ",full_name[::-1])


#Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r 3
#pi =3.141592653589793
import math
d=12
r=d/2
V=4.0/3.0*math.pi*pow(r,3)
print("The Volume of a Sphere is :",V)