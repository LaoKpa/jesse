class Route:
    def __init__(self, exchange, symbol, timeframe=None, strategy_name=None, weight=1, dna=None):
        self.exchange = exchange
        self.symbol = symbol
        self.timeframe = timeframe
        self.strategy_name = strategy_name
        self.strategy = None
        self.weight = weight
        self.dna = dna
