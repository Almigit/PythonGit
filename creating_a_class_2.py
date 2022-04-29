class Flower:
    def __init__(self, name, price, blue):
        self.name = name
        self.price = price
        self.blue = blue
        
        self.shop_name = "Lovely Bouquets"

    def count_price(self):
        if (self.name == "Tulip" and self.price >= 200):
            self.price  -= 25
            print("--------------")
            print(self.name)
            print(self.price)
            return
       
        if (self.name == "Rose" and self.blue == True):
            self.price += 200
            print("--------------")
            print(self.name)
            print(self.price)
            return
        else:
            print("--------------")
            print(self.name)
            print(self.price)

        

rose = Flower("Rose", 200, False) 
rose_blue = Flower("Rose", 200, True) 
tulip_cheap = Flower("Tulip", 150, False)
tulip_expensive = Flower("Tulip", 250, False)

rose.count_price()
rose_blue.count_price()
tulip_cheap.count_price()
tulip_expensive.count_price()
