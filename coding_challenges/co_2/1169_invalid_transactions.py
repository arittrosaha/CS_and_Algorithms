# https://leetcode.com/problems/invalid-transactions/
import collections

def invalid_transactions(transactions): # Time: O(nlogn) ; Space: O(n)
    transaction_dict = collections.defaultdict(list)
    invalid_trans = set()

    for transaction in transactions: # O(n)
        name, time, amount, city = transaction.split(",")
        if int(amount) > 1000:
            invalid_trans.add(transaction)
        else:
            transaction_dict[name].append([name, time, amount, city])
    
    for name, transactions in transaction_dict.items(): # O(n) + O(nlogn)
        transactions.sort(key=lambda t: t[0])
        i = 1
        while i < len(transactions):
            curr_trans = ",".join(transactions[i])
            prev_trans = ",".join(transactions[i-1])
            if int(transactions[i][1]) < int(transactions[i-1][1]) + 60:
                if curr_trans not in invalid_trans:
                    invalid_trans.add(curr_trans)
                if prev_trans not in invalid_trans:
                    invalid_trans.add(prev_trans)
            i += 1
    
    return list(invalid_trans)


# print(invalid_transactions(["alice,20,800,mtv", "alice,50,100,beijing"]))
# print(invalid_transactions(["alice,20,800,mtv", "alice,50,1200,mtv"]))
# print(invalid_transactions(["alice,20,800,mtv", "bob,50,1200,mtv"]))

             


