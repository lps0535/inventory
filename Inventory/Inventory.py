from Products import Products


class Inventory(Products):
    def __init__(self):
        Products.__init__(self)
        self.sum = 0

    def product_status(self,id):
        return self.products_status(id)

    def sum_of_products(self):
        self.sum = 0
        for value in self.all_products().values():
            self.sum += value[0]*value[2]
        return self.sum

if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_new_product(1,[5,10,2])
    print inventory.product_status(1)
    print inventory.sum_of_products()