from replit import clear
from art import logo
print(logo)
#create an empty dictionary
dictionary={}
is_another_person=True
#Input person name as a key and bid amount as a value into a dictionary
while(is_another_person):
  key=input("Enter your name ")
  value=int(input("Enter Bid "))
  dictionary[key]=value
  is_person_there=input("yes or no ").lower()
  if is_person_there=="yes":
    clear()
  else:
    is_another_person=False

heigher=0
name=""
#check the heighest bid value in a dictionary and assign in a heigher variable.
for key in dictionary:
  if dictionary[key]>heigher:
    heigher=dictionary[key]
    name=key
#print the winner name and bid amount
print(f"Winner is {name} and bid amount is {heigher}")