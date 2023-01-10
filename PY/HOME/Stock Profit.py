def stock_profit(array):
    match array:
        case list() as inf:
            min_as_req = inf[0]
            for i, j in enumerate(inf):
                if j < min_as_req and i != len(inf) - 1:
                    min_as_req = j
            counter = 0
            max_price = 0
            min_price = min_as_req
            for i in inf:
                if min_price == i and counter == 0:
                    counter += 1
                elif counter == 1 and i > min_price and i > max_price:
                    max_price = i
            result = max_price - min_price
            if result < 0:
                result = 0
            print(f"  {max_price}  {min_price}  rezult={result}")
            return result

        case _:
            print(F"Неправильный формат данных")

    # def stock_profit(stock: list) -> int:
    #     n = 1
    #     profits = [0]
    #     for buy in stock:
    #
    #         for sell in stock[n:]:
    #             profits.append(sell - buy)
    #         n += 1
    #     return max(profits)



#
stock_profit([2, 3, 4, 5])                        #3
stock_profit([3, 1, 3, 4, 5, 1])                  #4
stock_profit([4, 3, 2, 1])                        #0
stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4])      #4
stock_profit([1, 1, 1, 2, 1, 1, 1])               #1
stock_profit([4, 3, 2, 1, 2, 1, 2, 1])            #1
stock_profit([1, 1, 1, 1])                        #0

