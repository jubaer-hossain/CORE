# Minimum price seen so far - Min with previous price
# Profit we can make if we sell today - Max with previous profit

# O(n) time | O(1) space
def buyAndSellStockOnce(prices):
    minPriceSeenSoFar, maxProfit = float('inf'), 0

    for price in prices:
        minPriceSeenSoFar = min(minPriceSeenSoFar, price)
        
        currentProfit = price - minPriceSeenSoFar # How much we can make if we sell today
        maxProfit = max(currentProfit, maxProfit)
    return maxProfit


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] # 30
pricesTwo = [200, 100] # 0
pricesThree = [100, 200] # 100
pricesFour = [100, 200, 50, 200] # 150
print(buyAndSellStockOnce(prices))
print(buyAndSellStockOnce(pricesTwo))
print(buyAndSellStockOnce(pricesThree))
print(buyAndSellStockOnce(pricesFour))



def buyAndSellStockVersionTwo(prices):
    minPriceSoFar, maxProfit = float("inf"), 0

    for price in prices:
        currentProfit = price - minPriceSoFar
        maxProfit = max(maxProfit, currentProfit)
        
        minPriceSoFar = min(price, minPriceSoFar)
    
    return maxProfit


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
pricesTwo = [200, 100]
pricesThree = [100, 200]
pricesFour = [100, 200, 50, 200]

print("EPI Implementation: ")
print(buyAndSellStockVersionTwo(prices))
print(buyAndSellStockVersionTwo(pricesTwo))
print(buyAndSellStockVersionTwo(pricesThree))
print(buyAndSellStockVersionTwo(pricesFour))