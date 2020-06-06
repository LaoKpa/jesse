from jesse.models import Route


class RouterClass:
    def __init__(self):
        self.routes = []
        self.extra_candles = []
        self.market_data = []

    def set_routes(self, routes):

        import jesse.helpers as jh
        from jesse import exceptions

        self.routes = []

        total_weight = 0

        for r in routes:
            # validate strategy
            strategy_name = r[3]
            if jh.is_unit_testing():
                exists = jh.file_exists('jesse/strategies/{}/__init__.py'.format(strategy_name))
            else:
                exists = jh.file_exists('strategies/{}/__init__.py'.format(strategy_name))

            if not exists:
                raise exceptions.InvalidRoutes(
                    'A strategy with the name of "{}" could not be found.'.format(r[3]))

            # validate timeframe
            timeframe = r[2]
            if timeframe not in ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '3h', '4h', '6h', '8h', '1D']:
                raise exceptions.InvalidRoutes(
                    'Timeframe "{}" is invalid. Supported timeframes are 1m, 3m, 5m, 15m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 1D'.format(
                        timeframe)
                )
            if not jh.is_unit_testing():
                # validate weights
                weight = r[4]
                if weight > 1 or weight < 0:
                    raise exceptions.InvalidRoutes(
                        'Weight "{}" is invalid. Supported are values between 0 and 1'.format(
                            weight)
                    )

                total_weight += weight

            self.routes.append(Route(*r))

        if not jh.is_unit_testing():
            if total_weight > 1 or total_weight == 0:
                raise exceptions.InvalidRoutes(
                    'Total weight of all routes is "{}". Supported are values greater 0 and smaller 1'.format(
                        total_weight)
                )

    def set_market_data(self, routes):
        self.market_data = []
        for r in routes:
            self.market_data.append(Route(*r))

    def set_extra_candles(self, extra_candles):
        self.extra_candles = extra_candles


router: RouterClass = RouterClass()
