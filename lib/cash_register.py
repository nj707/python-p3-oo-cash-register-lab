# !/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total * ((100 - self.discount)/100))
            print(f"After the discount, the total comes to ${self.total}.")
        else: print("There is no discount to apply.")

    def void_last_transaction(self):
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            self.items.pop()