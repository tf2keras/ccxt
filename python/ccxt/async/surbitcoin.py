# -*- coding: utf-8 -*-

from ccxt import blinktrade

class surbitcoin (blinktrade):

    def describe(self):
        return self.deep_extend(super(surbitcoin, self).describe(), {
            'id': 'surbitcoin',
            'name': 'SurBitcoin',
            'countries': 'VE',
            'hasCORS': False,
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/27991511-f0a50194-6481-11e7-99b5-8f02932424cc.jpg',
                'api': {
                    'public': 'https://api.blinktrade.com/api',
                    'private': 'https://api.blinktrade.com/tapi',
                },
                'www': 'https://surbitcoin.com',
                'doc': 'https://blinktrade.com/docs',
            },
            'comment': 'Blinktrade API',
            'markets': {
                'BTC/VEF': {'id': 'BTCVEF', 'symbol': 'BTC/VEF', 'base': 'BTC', 'quote': 'VEF', 'brokerId': 1, 'broker': 'SurBitcoin'},
            },
        })
