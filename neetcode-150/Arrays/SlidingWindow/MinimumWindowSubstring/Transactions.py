def getMinTransactions(n, debts):

    trs_amounts = [0]*n
    positives = []
    negatives = []

    for debt in debts:

        trs_amounts[debt[1]] += debt[2]
        trs_amounts[debt[0]] -= debt[2]

    for amount in trs_amounts:
        if amount > 0:
            positives.append(amount)
        else:
            negatives.append(amount)
            
    transactions = 0
    while positives and negatives:
        min_debt = min(positives[0], -negatives[0])
        positives[0] -= min_debt
        negatives[0] += min_debt
        transactions += 1

        if positives[0] == 0:
            positives.pop(0)
        if negatives[0] == 0:
            negatives.pop(0)

    return transactions

n = 4
debts = [[1,2,15],[3,2,14],[0,3,10],[3,1,20]]

print(getMinTransactions(n, debts))