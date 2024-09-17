# WAP for Vote 
age = int(input("Enter Age"));
if(age >= 18 ): # here we have to use colon(:)
    {

 print("Eligiable")
    }
else:
    {
   print("NOt Eligiable")
    }

    
gender = input("Enter Gender ");
age = int(input("Enter age "));

if(gender=="male"  ):
    {
     print("You can apply for private Job ")
    }
elif(gender == "female" and age>17 ):
    {
        print("You can apply for goverment job")
    }

else:
    print("you cannot apply for any job")


#Q. WAP to check the greatest no among 3 no

A = int(input("Enter Value of A"))
B = int(input("Enter Value of B"))
C = int(input("Enter Value of C"))

if(A>B and A>C):
 print("A is Greatest form all the Rest number")

if(B>A and B>C):
 print("B is Greatest form all the Rest number")

else:
    print("C is Greatest form all the Rest number")
