player_coins = 0

shopSell = []
playerBuy = []
playerSell = []

equipping = []


def select_item_equip(self):
    f = 1
    for ba in p1.inventory:
        print("\n" + str(f) + ": " + str(ba.name))
        f += 1
    if len(p1.inventory) < 1:
        print("No items to equip.")
    else:
        try:
            x = int(input("What item would you like to equip?\n"))
            a = len(p1.inventory)

            if int(x) > a or int(x) <= 0:
                print("Please enter a valid input between 0-" + str(a))
                self.select_item_equip(self)
            else:
                b = p1.inventory[int(x) - 1]
                if p1.level >= b.level:
                    self.equipping.insert(1, b)
                    p1.inventory.remove(b)
                    self.equip_item(self)
                    self.equipping.remove(b)
                else:
                    print("Your level is to low to equip this item.")
                    self.select_item_equip(self)
        except ValueError:
            print("Please enter an integer only.")
            self.select_item_equip(self)
        self.equipping = []
