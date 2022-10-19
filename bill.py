''' wapp for billing software '''
menu = {"idli":20,"poha":15,"upma":15,"oats":45}
amount=0.0
while True:
    op=int(input("1 add,2 amount,3 exit"))
    if op==1:
        item=input("Enter Item u want to eat")
        price=menu.get(item, 0)
        print(price)
        if price==0:
            print("not available")
        else:
            quantity=int(input("Enter no of items"))
            amount=amount+price*quantity
    elif op==2:
        print("amount=",amount)
    elif op==3:
        break
    else:
        print("invalid option")
