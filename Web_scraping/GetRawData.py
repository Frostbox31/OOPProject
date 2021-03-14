from Google import getGoogleNew
from CoinGecko import gethistoricaldataforallcoin, getdailyvolumeforallcoins
import time
from decimal import Decimal


CalculateTime = Decimal(time.perf_counter())

#getGoogleNew('polkadot') still fixing
#getdailyvolumeforallcoins()
#gethistoricaldataforallcoin()

CalculateTime = Decimal(time.perf_counter()) - CalculateTime
print(str(CalculateTime) + " Seconds")