#•	Get the number entered from keyboard and store it into a variable userMessage
#•	If the userMessage is lower than 0, display “Negative Number!” 
#•	Else display “Positive Number” 
user_input=int(input("Enter the number:"))
userMessage=" "
if user_input <=0:
    userMessage="Negative Number!"
else:
    userMessage="Positive Number"
print(userMessage)
