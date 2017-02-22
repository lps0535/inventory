class Products(object):
    def __init__(self):
        self.products = {}

    def add_product(self,id,quantity):
        lst = self.products.get(id)
        lst[2]+=quantity
        self.products[id] = lst

    def add_new_product(self,id,lst):
        self.products[id] = lst

    def remove_product(self,id,quantity):
        lst = self.products.get(id)
        lst[2] -= quantity
        self.products[id] = lst

    def products_status(self,id):
         return self.products[id][2]

    def all_products(self):
        return self.products
