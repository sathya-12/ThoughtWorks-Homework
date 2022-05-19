class IceCreamType:
    icecream_type_name:str
    icecream_type_price:int
    def __init__(self,name:str,price:float):
        self.icecream_type_name=name
        self.icecream_type_price=price
    def type_name(self):
        return self.icecream_type_name
    def type_price(self):
        return self.icecream_type_price

class Toppings:
    toppings_name:str
    toppings_price:int
    def __init__(self,topping_name,topping_price):
        self.toppings_name=topping_name
        self.toppings_price=topping_price
    def topping_name(self):
        return self.toppings_name
    def topping_price(self):
        return self.toppings_price
    
    
class IceCreamFlavour:
    icecream_flavour_name:str
    icecream_flavour_price:int
    
    def __init__(self,flavour_name,flavour_price):
        self.icecream_flavour_name=flavour_name
        self.icecream_flavour_price=flavour_price
    def flavour_name(self):
        return self.icecream_flavour_name
    def flavour_price(self):
        return self.icecream_flavour_price
    
class shop:
    list_of_types=[]
    list_of_flavours=[]
    choices = ["Yes","No"]
    list_of_toppings=[]
    topping_preference:str
    user_type:int
    user_flavour:int
    user_topping:int
    quantity_choice:int
    total_bill_amount:int
    def list_of_icecreams(self):
        self.list_of_types.append(IceCreamType("cup",10))
        self.list_of_types.append(IceCreamType("stick",15))
        self.list_of_types.append(IceCreamType("cone",20))

        self.list_of_flavours.append(IceCreamFlavour("vanilla",10))
        self.list_of_flavours.append(IceCreamFlavour("strawberry",15))
        self.list_of_flavours.append(IceCreamFlavour("chocolate",20))


    def Toppings(self):

        self.list_of_toppings.append(Toppings("Oreo Crumbles",20))
        self.list_of_toppings.append(Toppings("Cherries",35))
        self.list_of_toppings.append(Toppings("Chocolate Chips",60))
        self.list_of_toppings.append(Toppings("Friuty-Fruity",10))

    def Individual_menu_card(self):
        serial_number_type = 1
        serial_number_flavour = 1
        print("\n---TYPES LIST---\n")
        for type in self.list_of_types:
            print(serial_number_type , ")" , type.type_name() , type.type_price())
            serial_number_type = serial_number_type + 1
        print("\n---FLAVOURS LIST---\n")
        for flavour in self.list_of_flavours:
            print(serial_number_flavour , ")" , flavour.flavour_name() , flavour.flavour_price())
            serial_number_flavour = serial_number_flavour + 1

    def combined_menu_card(self):
        serial_num = 1
        for type in self.list_of_types:
            for flavour in self.list_of_flavours:
                print(serial_num,")",flavour.flavour_name()," ",type.type_name(),"----Rs.",type.type_price()+flavour.flavour_price())
                serial_num = serial_num + 1

    def Toppings_menu(self):
        serial_number_toppings = 1
        print("\n---TOPPINGS LIST---\n")
        for topping in self.list_of_toppings:
            print(serial_number_toppings,")" , topping.topping_name() , topping.topping_price())
            serial_number_toppings += 1

    def get_type(self):
        type_choice= int(input("\nEnter the type of your choice : \n"))
        self.user_type=type_choice
        

    def get_flavour(self):
        flavour_choice=int(input("\nEnter the flavour of your choice : \n"))
        self.user_flavour=flavour_choice
        return self.user_flavour

    def get_quantity(self):
        quantity = int(input("\nEnter the quantity of iceceream : \n"))
        self.quantity_choice=quantity

    def topping_needed_or_not(self):
        print("Additional Toppings Available for the chosen flavour.Would you like to add toppings ??")
        si_no=1
        for choice in self.choices:
            print(si_no,choice,'\n')
            si_no = si_no+1
        topping_choice=int(input("\nEnter your Preference : "))
        self.topping_preference = topping_choice
        return self.topping_preference


    def get_toping(self):
        topping_choice=int(input("\nEnter the Topping of your choice\n"))
        self.user_topping = topping_choice


    def calculate_bill_amount(self):
        cost_of_chosen_type = self.list_of_types[self.user_type - 1].type_price()
        cost_of_chosen_flavour = self.list_of_flavours[self.user_flavour - 1].flavour_price()
        bill_amount = (cost_of_chosen_type + cost_of_chosen_flavour) * self.quantity_choice
        self.total_bill_amount = bill_amount
    def Print_bill(self):
        print("\n ------ Your Order -----  \n")
        print(self.list_of_types[self.user_type-1].type_name(),"----- Rs" , self.list_of_types[self.user_type-1].type_price())
        print(self.list_of_flavours[self.user_flavour-1].flavour_name(),"-----Rs" , self.list_of_flavours[self.user_flavour-1].flavour_price())
        print('\n')
        print("You Chose " ,self.list_of_flavours[self.user_flavour-1].flavour_name()," ",self.list_of_types[self.user_type-1].type_name())
        print("Required Quantity is : ",self.quantity_choice)
        print('\n')
        print("Total  Bill  Amount" , "-----Rs" , self.total_bill_amount)

    def Bill_with_toppings(self):
         cost_of_chosen_type = self.list_of_types[self.user_type - 1].type_price()
         cost_of_chosen_flavour = self.list_of_flavours[self.user_flavour - 1].flavour_price()
         cost_of_chosen_topping = self.list_of_toppings[self.user_topping -1].topping_price()
         bill_amount = (cost_of_chosen_type + cost_of_chosen_flavour+ cost_of_chosen_topping)
         self.total_bill_amount = bill_amount
         self.bill_with_toppings = self.total_bill_amount  * self.quantity_choice

        

    def Print_bill_with_toppings(self):
         print("\n ------ Your Order -----  \n")
         print(self.list_of_types[self.user_type-1].type_name(),"-----Rs" , self.list_of_types[self.user_type-1].type_price())
         print(self.list_of_flavours[self.user_flavour-1].flavour_name(),"-----Rs" , self.list_of_flavours[self.user_flavour-1].flavour_price())
         print(self.list_of_toppings[self.user_topping - 1].topping_name(),"-----Rs" , self.list_of_toppings[self.user_topping-1].topping_price())
         print('\n')
         print("You  Chose " ,self.list_of_flavours[self.user_flavour-1].flavour_name()," ",self.list_of_types[self.user_type-1].type_name()," with ",self.list_of_toppings[self.user_topping - 1].topping_name()," topping")
         print("Required  Quantity  is : ",self.quantity_choice)
         print('\n')
         print("Total  Bill  Amount","-----Rs",self.bill_with_toppings)



    
obj = shop()
obj.list_of_icecreams()
obj.Individual_menu_card()
obj.combined_menu_card()
obj.get_type()
chosen_flavour = obj.get_flavour()
if(chosen_flavour == 3):
    choice = obj.topping_needed_or_not()
    if(choice== 1):
        obj.Toppings()
        obj.Toppings_menu()
        obj.get_toping()
        obj.get_quantity()
        obj.Bill_with_toppings()
        obj.Print_bill_with_toppings()
   
    else:
       obj.get_quantity()
       obj.calculate_bill_amount()
       obj.Print_bill()
else:
    obj.get_quantity()
    obj.calculate_bill_amount()
    obj.Print_bill()