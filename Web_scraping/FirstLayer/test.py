import unittest
from GetRawData import _getDailyVolumeForAllCoins, _getHistoricalDataForAllCoin,_generateGoogleYahooReddit
from GetResult import getTotalVolumeForTheDay,getCoinsName,getCoinsShortForm

class TestFunction(unittest.TestCase):
    def test_function(self):

       self.assertFalse(_getDailyVolumeForAllCoins())                   #False because this function return value

       self.assertFalse(_getHistoricalDataForAllCoin(1))                #False because this function return value          
       self.assertFalse(_getHistoricalDataForAllCoin(10))               #False because this function return value
       self.assertFalse(_getHistoricalDataForAllCoin(0))                #False because this function return value   
       self.assertFalse(_getHistoricalDataForAllCoin(100))              #False because this function return value
       self.assertFalse(_getHistoricalDataForAllCoin('ABC'))            #False because this function return value

       self.assertFalse(_generateGoogleYahooReddit('Yahoo',150))        #False because this function doesn't return any value
       self.assertFalse(_generateGoogleYahooReddit('Yahoo','ABC'))      #False because this function doesn't return any value
       self.assertFalse(_generateGoogleYahooReddit('Yahoo',1000))       #False because this function doesn't return any value
       self.assertFalse(_generateGoogleYahooReddit('Yahoo',1020))       #False because this function doesn't return any value
       self.assertFalse(_generateGoogleYahooReddit('Yahoo',0))          #False because this function doesn't return any value

       #self.assertFalse(_generateGoogleYahooReddit('Google',''))

       self.assertFalse(_generateGoogleYahooReddit('Reddit',1))         #False because this function doesn't return any value
       self.assertFalse(_generateGoogleYahooReddit('Reddit','ABC'))     #False because this function doesn't return any value
       self.assertFalse(_generateGoogleYahooReddit('Reddit',-3))        #False because this function doesn't return any value
       self.assertFalse(_generateGoogleYahooReddit('',''))                #False because this function doesn't return any value
 
       self.assertTrue(getTotalVolumeForTheDay())                       #True because this function return value
       self.assertTrue(getCoinsName())                                  #True because this function return value
       self.assertTrue(getCoinsShortForm())                             #True because this function return value

if __name__ == '__main__':
 unittest.main()