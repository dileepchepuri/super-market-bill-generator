from datetime import datetime
name=input("Please Enter your Name : ")
print(f"Hello {name} Welcome To the supermarket")
list='''
Cooking Oil ₹120/litre
Rice ₹60/kg
Dal ₹100/kg
Sugar ₹45/kgl
Aata ₹40/kg
Turmeric ₹200/kg
Coffee ₹2500/kg
Tea ₹155/kg
Dry_Fruits_Mix ₹850/kg
GreenPeas ₹120/kg
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
itemlist=[]
quantitylist=[]
plist=[]
items={
   " Cooking Oil":120,
"Rice":60,
"Dal":100,
"Sugar":45,
"Aata":40,
"Turmeric":200,
"Coffee":2500,
"Tea":155,
"Dry_Fruits_Mix":850,
"GreenPeas":120
}
user_input=int(input("To display the list of items press 1 :"))
while user_input:
    if user_input==1:
        print(list)
        break
    else:
        user_input=int(input("You have Entered invalid number Try Again : "))
for i in range(20):
    try:
        option=int(input("press 1 To add more items and 2 for exit : "))
    except Exception as e:
        print("oops! You have Entered",e)
    if option==2:
        break
    if option==1:
        item=input("Please enter your item Name Exactly shown in the list : ")
        if item in items.keys():
            quantity=int(input("Enter the quntity of item : "))
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            itemlist.append(item)
            quantitylist.append(quantity)
            plist.append(price)
            gst=totalprice*0.10
            finalamount=gst+totalprice
        else:
            print("You have given invalid input")
    else:
        print("oops! You have Entered invalid number")
    if i==19:
        print("You have entered invalid input for max times Please start form the main menu")
inp=input("Do you need a bill reciept Type 'yes' or 'no': ")
if inp=='yes':
    print('SL.NO',' ','Items',' ','Quantity',' ','Price')
    for i in range(len(pricelist)):
        print(i,'     ',itemlist[i],'     ',quantitylist[i],'      ',plist[i])
else:
    pass
print('Total Amount ',finalamount)
print(f'Thank you for the shopping {name} 😊 Visit Again!')