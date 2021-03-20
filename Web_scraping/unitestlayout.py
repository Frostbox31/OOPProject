import unittest
from layout import app
import layout.routes

class TestFunction(unittest.TestCase):
    def test_dash(self):
        self.assertIsNotNone(layout.routes.getalltrend())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.gettopchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getyrdashchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkdashchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmdashchart())                   #Check if there is output for website

    def test_bitcoin(self):
        self.assertIsNotNone(layout.routes.getyrbtcchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkbtcchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmbtcchart())                   #Check if there is output for website
    
    def test_ethereum(self):
        self.assertIsNotNone(layout.routes.getyrethchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkethchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmethchart())                   #Check if there is output for website
    
    def test_tether(self):
        self.assertIsNotNone(layout.routes.getyrtetchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwktetchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmtetchart())                   #Check if there is output for website
    
    def test_cardano(self):
        self.assertIsNotNone(layout.routes.getyrcarchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkcarchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmcarchart())                   #Check if there is output for website

    def test_binance(self):
        self.assertIsNotNone(layout.routes.getyrbinancechart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkbinancechart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmbinancechart())                   #Check if there is output for website
    
    def test_polkadot(self):
        self.assertIsNotNone(layout.routes.getyrpolkadotchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkpolkadotchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmpolkadotchart())                   #Check if there is output for website
    
    def test_xrp(self):
        self.assertIsNotNone(layout.routes.getyrxrpchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkxrpchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmxrpchart())                   #Check if there is output for website
    
    def test_uniswap(self):
        self.assertIsNotNone(layout.routes.getyruniswapchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkuniswapchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmuniswapchart())                   #Check if there is output for website
    
    def test_litecoin(self):
        self.assertIsNotNone(layout.routes.getyrlitecoinchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwklitecoinchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmlitecoinchart())                   #Check if there is output for website
    
    def test_chainlink(self):
        self.assertIsNotNone(layout.routes.getyrchainlinkchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getwkchainlinkchart())                   #Check if there is output for website
        self.assertIsNotNone(layout.routes.getmchainlinkchart())                   #Check if there is output for website

if __name__ == '__main__':
    unittest.main()