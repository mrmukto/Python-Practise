class Computer:
    pass


class Computer():
    def __init__(self, brand, quality, price):
        self.brand = brand
        self.quality = quality
        self.price = price

    mouse = Computer()
    keyboard = Computer('HP','wirconnect', 575)



    print( mouse.__dict__ )

    

