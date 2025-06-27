menu={
    'Pizza':100,
    'Burger':70,
    'Pasta':60,
    'Salad':30,
    'Coffee':50
}
menu1={}
for i in menu:
    menuuu=i.lower()
    menu1[menuuu]=menu[i]

print("Hello! Welcome to our Resturant: ")
print("Here all the items from our resturant: ")
for i in menu:
    print(i,f" : ",menu[i])
order_total=0
item1=input("Enter the name of item that you want to order !! ").lower()
if item1 in menu1:
    order_total+=menu1[item1]
    print(f"your item {item1} has been added to your order")
else:
    print(f"please order something that is available in our resturant...\n You can order only {menu1} ")

while(True):
    
    another_order=input("Do you want to add another item ? (Yes/No) ").lower()
  
    if(another_order=='yes'):
        item=input("Enter the next item you want to add !!").lower()
        if(item in menu1):
          order_total+=menu1[item]
          print(f"the item {item} is added to your order ")
        else:
            print(f"ordered item {item} is not available ")
    else:
        break
    
print("The total amount of item to pay is ",order_total)
print("Thank You !!!")
