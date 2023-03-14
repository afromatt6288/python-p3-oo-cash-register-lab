#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self.items = []
    self.new_transaction = 0

  def add_item(self, title, price, quantity = 1):
    self.new_transaction = price*quantity
    self.total += self.new_transaction
    for n in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    zeros = '.0f'
    total_price_with_discount = self.total - self.total*(self.discount/100)
    self.total = total_price_with_discount
    if self.total > 0:
      print(f"After the discount, the total comes to ${format((self.total), zeros)}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total -= self.new_transaction
    pass


