import ConfigParser
import miner_api as api

def main():
    config = ConfigParser.ConfigParser()
    config.read('config.ini')
    addresses = config.items('addresses')

    total_km_value  = 0

    for address in addresses:
        res = {}
        price = 0
        if address[0] == 'eth':
            res =  api.nanopool_coin(api.NANOPOOL_ETH, address[1])
            price = api.cryptocompare_price(api.CRYPTOCOMPARE_ETH)
        if address[0] == 'xmr':
            res =  api.nanopool_coin(api.NANOPOOL_XMR, address[1])
            price = api.cryptocompare_price(api.CRYPTOCOMPARE_XMR)
        if address[0] == 'sia':
            res =  api.nanopool_coin(api.NANOPOOL_SIA, address[1])
            price = api.cryptocompare_price(api.CRYPTOCOMPARE_SIA)
        print '%s hashrate: %5s   MH\s %s balance:  %s' % (address[0].upper(), res['hashrate'], address[0].upper(),  res['balance'])
        print '%s price: %-10s' % (address[0].upper(), price)
        total_km_value += res['balance'] * price * 1.95

    print "Total value in km: " + str(total_km_value)


if __name__ == "__main__":
    main()