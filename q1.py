




def priceCheck(products, productPrices, productSold, soldPrice):
    incorrect_prices = 0
    # Making map for context price with product
    
    product_prices = dict(zip(products, productPrices))
    
    # Finding errors in the prices sold     
    
    for i in range(len(productSold)):
        if productSold[i] not in product_prices:
            incorrect_prices += 1
        elif soldPrice[i] != product_prices[productSold[i]]:
            incorrect_prices += 1
    return incorrect_prices

# Test
print(priceCheck(
    products=['rice', 'sugar', 'wheat', 'cheese'],
    productPrices=[16.89, 56.92, 20.89, 345.99],
    productSold=['rice', 'cheese'],
    soldPrice=[18.99, 400.89]
)) # Output: 2
