products={1:"laptop",2:"mobile"}
def view_menu():
    for id,product in products.items():
       print(id,product)
print("1.view menu\n2.exit")
while True:
   n=int(input("enter your choice"))
   if n==1:
      view_menu()
   else:
      print("please enter a valid input")
   if n==2:
      print("thankyou")
      break

    