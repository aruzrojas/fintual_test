
#Portfolio class for each user, maybe a user can have more than one portfolio :?

#LLM conversation (CHAT-GPT): https://chatgpt.com/share/69829f80-8108-8004-ae15-87b834630b3f

class Portfolio:

    user = USUARIO()
    #stocks of user, it's possible to get with a function like get_stocks
    stocks = ['META', 'APPL']
    #balance stocks for user, it's posibble to get with a function and that info stored in db
    balance_stocks = {"META": 0.4, "APPL": 0.6}

    #get amount for a stock
    def get_amount(self, stock):
        return bd.get_amount(self.user.id, stock)

    def get_total_amount(self):
        return self.user.get_total_amount()

    def sell_stock(self):
        ...
    
    def buy_stock(self):
        ...

    def balance_portfolio(self):
        total_amount = self.get_total_amount()
        for stock in stocks:

            balance_percentage = balance_stocks[stock]
            stock_amount = self.get_amount(stock)
            total_amount = self.get_total_amount()
            new_percentage = stock_amount/total_amount

            if new_percentage > balance_percentage:
                percentage_to_sell = balance_percentage - new_percentage
                amount_to_sell = total_amount * percentage_to_sell
                self.sell_stock(stock, amount_to_sell)
            else:
                percentage_to_buy = new_percentage - balance_percentage
                amount_to_buy = total_amount * percentage_to_buy
                self.buy_stock(stock, amount_to_buy)

