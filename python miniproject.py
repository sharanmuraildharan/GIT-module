#fist step gather the input from user
import datetime #i have imported the date time libaray so that it will be easy to find it
birthYear = int (input ("Enter Your Birth Year:"))
age = datetime.datetime.now () .year - birthYear
print ("You are",age, "Years Old'")
print("lets move on to the survival finder")
def surv1(age,survival=69.99): #the default age is 100 
    if age<0:
        print("Enter the valid age")
    elif age>survival:
        print("Enter the valid age")    
    else:
        print("you will survive on this planet over",survival-age,"years")
surv1(age,survival=69.99)
print("Thank you")      
