## Brute force sollution
## TC = O(N*2)
## SC = O(1)
def max_profit(prices):
    max_profit = 0
    n = len(prices)
    for i in range(n):
        for j in range(i+1,n):
            if prices[j] > prices[i]:
                max_profit = max(max_profit,prices[j]-prices[i])
    return max_profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))

## optimal solution
## TC = O(N)
## SC = O(1)

def max_profit(prices):
    max_profit = 0
    min_price = float("inf")
    n = len(prices)
    for i in range(n):
        min_price = min(min_price,prices[i])
        max_profit = max(max_profit,prices[i]-min_price)
        
    return max_profit

print(max_profit(prices))