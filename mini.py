print("INTRANCE EXAMINATION FOX NIMCET(MCA) 2024")
n=0
name=input("ENTER YOUR NAME :")
roll= int(input("ENTER YOUR EXAMINATION ROLL NUMBER :"))
password= (input("ENTER YOU PASSWORD (YOUR PASSWORD IS YOUR DATE OF BIRTH.):"))
print("\nHey",name,"You have Successfully Login.. ")
print("Your Roll No. is",roll)
print("And Password is",password)
print("\n*ALL 10 QUESTIONS ARE MCQ*")
print(" \n1. Who developed pythan programming language?")
r=input("a) Wick van Rossum\nb) Rasmus Lerdorf\nc) Guido van Rossum\nd) Niene Stom")
print(r)
if r == "c":
  n +=1
else:
    n +=0
  
print("2. Which type of Programming does Python support?")
r=input("a) object-oriented programming\nb) structured programming\nc) functional programming\nd) all of the mentioned")
print(r)
if r=="d":
 n +=1
else:
  n +=0
print("3. Is Python case sensitive when dealing with identifiers?")
r=input("a) no\nb) yes\nc) machine dependent\nd) none of the mentioned")
print(r)
if r=="b":
  n +=1
else:
   n +=0
print("4.  Which of the following is the correct extension of the Python file?")
r=input("a) .python\nb) .pl\nc) .py\nd) .p")
print(r)
if r=="c":
   n +=1
else:
  n +=0
print("5.Is Python code compiled or interpreted?")
r=input("a) Python code is both compiled and interpreted\nb) Python code is neither compiled nor interpreted\nc) Python code is only compiled\nd) Python code is only interpreted")
print(r)
if r=="a":
   n +=1
else:
    n +=0
print("6. What will be the value of the following Python expression?\n4 + 3 % 5")
r=input("a) 7\nb) 2\nc) 4\nd) 1")
print(r)
if r=="b":
   n +=1
else:
    n +=0
print("7. Which of the following is used to define a block of code in Python language?")
r=input("a) Indentation\nb) Key\nc) Brackets\nd) All of the mentioned")
print(r)
if r=="a":
   n +=1
else:
   n +=0
print("8. Which keyword is used for function in Python language?")
r=input("a) Function\nb) def\nc) Fun\nd) Define")
print(r)
if r=="b":
   n +=1
else:
    n +=0
print("9. Which of the following character is used to give single-line comments in Python? ")
r=input("a) //\nb) #\nc) !\nd) /*")
print(r)
if r=="b":
   n +=1
else:
    n +=0
print("10. Which of the following functions can help us to find the version of python that we are currently working on? ")
r=input("a) sys.version(1)\nb) sys.version(0)\nc) sys.version()\nd) sys.version")
print(r)
if r=="d":
   n +=1
else:
    n +=0
print("Your total score is",n,"out of 10")
if n>=7:
   print("\nCONGRATES!",name,"YOU ARE SELECTED FOR (THE National Institute of Technology, Warangal, Telangana)\nNEXT INFORMATION IS SENT TO YOUR EMAIL SOON.")
elif n>=5:
   print("\nCONGRATES!",name,"YOU ARE SELECTED FOR (NIT KURUKSHETRA) NEXT INFORMATION IS SENT TO YOUR EMAIL SOON.")
else:
   print( "\nSORRY",name,"YOU ARE NOT SELECTED IN ANY COLLEG.\nSO PLEASE TRY AGAIN NEXT YEAR")

 


   


   

