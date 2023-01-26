



class EMA(object):

    def __init__(self, alpha=0.5):
        self.value = 0
        self.alpha = alpha

    def update(self, price):
        self.value = self.value + self.alpha * (price - self.value)

def ema(alpha=0.5):
    result = 0
    previous = (yield)
    while True:
        price = (yield result)
        result = result + alpha(price - result)





