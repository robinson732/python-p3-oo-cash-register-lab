#!/usr/bin/env python3
#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        # Add to total
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.last_transaction = transaction_amount

        # Add items to the list (duplicates for quantity)
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            self.total = int(self.total) if self.total.is_integer() else self.total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0
        # Remove last added items
        if self.items:
            # Count how many of the last transaction's item were added
            last_item = self.items[-1]
            count = self.items.count(last_item)
            # Remove only the last transaction items
            for _ in range(count):
                self.items.pop()

