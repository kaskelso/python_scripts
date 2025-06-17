#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:59:10 2024

@author: kennyaskelson
"""

class Category:
    def __init__(self, nam):
        self.items = nam
        self.balance = 0
        self.ledger = []
    def deposit(self, val, thing1=""):
        self.balance = self.balance + val
        if not thing1:
            thing1 = ""
        self.ledger.append({'amount': val, 'description': thing1})
    def withdraw(self, sub, thing2=""):
        if self.balance >= sub:
            self.balance = self.balance - sub
            if not thing2:
                thing2 = ""
            self.ledger.append({'amount': -sub, 'description': thing2})
            return True
        else:
            return False
    def get_balance(self):
        return self.balance
    def transfer(self, amount, destination_category):
        if self.balance >= amount:
            self.withdraw(amount, f"Transfer to {destination_category.items}")
            destination_category.deposit(amount, f"Transfer from {self.items}")
            return True
        else:
            return False
    def check_funds(self, money):
        if self.balance >= money:
            return True
        else:
            return False
    def __str__(self):
        item_length = len(self.items)
        asterisks = '*' * ((30 - item_length) // 2)  
        result = f"{asterisks}{self.items}{asterisks}\n" #\n makes a line break!
        for transaction in self.ledger:
            amount_str = "{:.2f}".format(transaction['amount']) #formats amount with 2 decimal
            result += f"{transaction['description'][:23]:<23}{amount_str:>7}\n" # += adds to the right of variables! this command left aligns description with 23 characters and right aligns amount with 7 characters
        result += f"Total: {self.balance:.2f}"
        return result

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    # Calculate the total withdrawals and deposits for each category
    total_withdrawals = [sum(transaction['amount'] for transaction in category.ledger if transaction['amount'] < 0) for category in categories]
    all_withdrawals = sum(total_withdrawals)

    # Calculate the percentages spent for each category
    percentages_spent = [] 
    for with_draw in total_withdrawals:
        percentages_spent.append((with_draw/all_withdrawals) * 100)

    # Build the chart
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for percentage in percentages_spent:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Add the horizontal line
    chart += "    " + "---" * len(categories) + "-\n"

    # Find the maximum length of category names
    max_length = max(len(category.items) for category in categories)

    # Build the category labels
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.items):
                chart += f"{category.items[i]}  "
            else:
                chart += "   "
        chart += "\n" if i < max_length - 1 else ""  # Add a newline character except for the last iteration

    return chart





        
            
