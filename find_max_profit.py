"""
Say you have an array for which the ith element is the price of
a given stock on day i. If you were only permitted to complete at
most one transaction (ie, buy one and sell one share of the stock)
design an algorithm to find the maximum profit.

Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be
larger than buying price)

Example 2:

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


# YOUR CODE GOES HERE
def max_profit_helper(price):
    if len(price)>0:
        min_stock=price[0]
        max_stock=0
        while len(price)>0:
            current_stock=price.pop(0)
            min_stock=min(min_stock, current_stock)
            if current_stock > min_stock:
                if current_stock >max_stock:
                    max_stock = current_stock
        if (max_stock - min_stock) > 0:
            max_out = max_stock - min_stock
        else:
            max_out = 0
#        print (max_out)
        return max_out
    else:
        return 0


# DON"T CHANGE THIS
def max_profit(price):
    return max_profit_helper(price)


# Please feel free to come up with your own testcases below:
# Test case: all same price.
print (max_profit([3, 3, 3, 3, 3]))
print (max_profit([]))
print (max_profit([1, 6, 6]))
print (max_profit([3]) )

msg_same = "failed test case where all elements are the same"
assert max_profit([3, 3, 3, 3, 3]) == 0, msg_same
# Test case: empty list
msg_empty = "failed test case where empty list was passed in"
assert max_profit([]) == 0, msg_empty
# Test case: two options for selling give the same profit.
msg_two = "failed test case where two options with the same profit exists"
assert max_profit([1, 6, 6]) == 5, msg_two
# Test case: only one element in list
msg_one = "failed test case where only one element was available in list"
assert max_profit([3]) == 0, msg_one
