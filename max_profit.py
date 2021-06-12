# в списке изменение цены во времени, найти лучшую сделку (минимальная цена покупки, максимальная цена продажи)
# обратить внимание, что мы не можем продать раньше, чем купить



stocks = [1, 10, 5, 6]


def max_profit2(stocks):
    best_deal = -1
    for ind, el in enumerate(stocks):
        max_el = max(list(stocks[ind::]))
        if max_el - el > best_deal:
            best_deal = max_el - el
    return best_deal


def max_profit3(stocks):
    return max([max(list(stocks[ind::])) - el for ind, el in enumerate(stocks)])


print(max_profit2(stocks))
print(max_profit3(stocks))
