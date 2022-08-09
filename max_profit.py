# в списке изменение цены во времени, найти лучшую сделку (минимальная цена покупки, максимальная цена продажи)
# обратить внимание, что мы не можем продать раньше, чем купить
from operator import itemgetter


def max_profit2(stocks):
    best_deal = -1
    for ind, el in enumerate(stocks):
        max_el = max(list(stocks[ind::]))
        if max_el - el > best_deal:
            best_deal = max_el - el
    return best_deal


def max_profit3(stocks):
    return max([max(list(stocks[ind::])) - el for ind, el in enumerate(stocks)])


def max_profit_4(stocks):
    stocks_range = [(stocks[i], stocks[j], stocks[i]-stocks[j]) for i in range(1, len(stocks)) for j in range(i)]
    return max(stocks_range, key=itemgetter(2))


stocks_ = [
    [1, 10, 5, 6],
    [6, 5, 10, 11, 3, 8, 7, 9, 8, 2, 7, 8]
]


for stock in stocks_:
    print(max_profit2(stock))
    print(max_profit3(stock))
    best_deal = max_profit_4(stock)
    print(f'highest difference: {best_deal[2]}, buy price: {best_deal[0]}, sell price: {best_deal[1]} ')

