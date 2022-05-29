class PurchaseDetails:
    PurchaseList=[]
    name:str
    ItemName:str
    ItemPrice:float
    quantity:int
    TotalTax:float
    FinalBill:float
    FInalBillForExmptedItems:float

    def UserInput(self):
        PurchaseList=input().split()
        self.quantity = (PurchaseList[0])
        self.ItemName = (PurchaseList[-3])
        self.ItemPrice = (PurchaseList[-1])
    
    def NeededQuantity(self):
        return int(self.quantity)
    def NeededItem(self):
        return self.ItemName
    def Price(self):
        return float(self.ItemPrice)

    def PrintPurchaseList(self):
        print("----Welcome----\n")
        print("Your purchase list")
        print("Name of the Item :",self.NeededItem())
        print("price of the Item :",self.Price())
        print("Quantity needed :",self.NeededQuantity())

    def TaxPerItem(self):
        TaxAmount = (15/100)*(float(self.ItemPrice))
        self.Tax = TaxAmount
        Total = (int(self.quantity))*(float(self.Tax))
        self.TotalTax = Total
        return self.TotalTax


    def TotalBillAmount(self):
        TotalAmount = ((self.NeededQuantity())*(self.Price()))+((self.TaxPerItem()))
        self.FinalBill = TotalAmount
        return self.FinalBill

    def BillForExempted(self):
        TotalBill = self.NeededQuantity()*self.Price()
        self.FInalBillForExmptedItems = TotalBill
        return self.FInalBillForExmptedItems

    def PrintBill(self):
        print("---Your Bill---")
        print(self.NeededItem(),"*",self.NeededQuantity(),"----------------",self.Price()*self.NeededQuantity())
        print("Total Tax amount for this purchase","--",self.TaxPerItem())
        print("Final Amount To Pay","-------",self.FinalBill)

    def PrintExemptedBill(self):
        print("---Your Bill---")
        print(self.NeededItem(),"*",self.NeededQuantity(),"----------------",self.Price()*self.NeededQuantity())
        print("your Final Amount to Pay","-----",self.BillForExempted())
        

class StoreDetails:
    ItemsList = []
    ExemptedItemsList = []
    def check(self,name):
        if name in self.ExemptedItemsList:
            a = "yes"
        else:
            a = "no"
        return a

    def Details(self):
        self.ItemsList.append("pen")
        self.ItemsList.append("pencil")
        self.ItemsList.append("paper")
        self.ItemsList.append("hair oil")
        self.ItemsList.append("sunscream")
        self.ExemptedItemsList.append("milk")
        self.ExemptedItemsList.append("vegetable")
        self.ExemptedItemsList.append("medicine")
    


    
def main():
    Purchase = PurchaseDetails()
    Purchase.UserInput()
    ItemName = Purchase.NeededItem()
    Store = StoreDetails()
    Check1 = Store.check(ItemName)
    if Check1=="yes":
        Purchase.PrintPurchaseList()
        Purchase.FInalBillForExmptedItems()
        Purchase.PrintExemptedBill()
    else:
        Purchase.PrintPurchaseList()
        Purchase.TotalBillAmount()
        Purchase.PrintBill()

if __name__ == "__main__":
    main()









        


