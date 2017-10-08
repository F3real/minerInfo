import requests

NANOPOOL_ETH = 'https://api.nanopool.org/v1/eth/balance_hashrate/'
NANOPOOL_XMR = 'https://api.nanopool.org/v1/xmr/balance_hashrate/'
NANOPOOL_SIA = 'https://api.nanopool.org/v1/sia/balance_hashrate/'

CRYPTOCOMPARE_ETH = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=ETH,EUR'
CRYPTOCOMPARE_XMR = 'https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=XMR,EUR'
CRYPTOCOMPARE_SIA = 'https://min-api.cryptocompare.com/data/price?fsym=SC&tsyms=SC,EUR'


def nanopool_coin(url, address):
    r = requests.get(url + address)
    return r.json()['data']

def cryptocompare_price(url):
    r = requests.get(url)
    return r.json()['EUR']