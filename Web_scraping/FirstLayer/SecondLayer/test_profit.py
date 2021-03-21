import unittest
from Profit import data_manu as dm


class TestProfits(unittest.TestCase):

    def setUp(self):
        testprofit = [('bitcoin', '2021-03-19', '$58,243'),                       # use the lastest date to get today's price to compare to get profit
                    ('bitcoin', '2021-03-10', '$56,020'),
                    ('ethereum', '2021-03-19', '$1,817.13'),                     # use the lastest date to get today's price to compare to get profit                            ,
                    ('ethereum', '2021-03-10', '$1,802.31')]

        testavgprofit_data = [('bitcoin', '2021-03-19', 0.0),                     # use data of weekly profit for 2 coins for testing of average profit
                             ('bitcoin', '2021-03-18', 0.55), 
                             ('bitcoin', '2021-03-17', -1.33), 
                             ('bitcoin', '2021-03-16', 2.43),
                             ('bitcoin', '2021-03-15', 4.19), 
                             ('bitcoin', '2021-03-14', -2.04), 
                             ('bitcoin', '2021-03-13', -5.27), 
                             ('bitcoin', '2021-03-12', 1.53),
                             ('ethereum', '2021-03-19', 0.0), 
                             ('ethereum', '2021-03-18', 2.03), 
                             ('ethereum', '2021-03-17', -0.64),
                             ('ethereum', '2021-03-16', 0.47),
                             ('ethereum', '2021-03-15', 1.44), 
                             ('ethereum', '2021-03-14', -2.69), 
                             ('ethereum', '2021-03-13', -6.09), 
                             ('ethereum', '2021-03-12', 2.54)]

        self.test_profit = testprofit                                                  # list  of data gotten from SQL 
        self.testavg = testavgprofit_data

    def test_calprofit(self):
        profit_list = list((0.0,3.82,0.0,0.82))                                                             # as  profit is 0 as its using today price as both argument
        price_list = list(('58243','56020','1817.13','1802.31'))                                            # removed $ symbol to be inserted into price list
        date_list =list(('2021-03-19','2021-03-10','2021-03-19','2021-03-10'))                              # testing for range of dates to be appended into date list
        name_list =list(('bitcoin','bitcoin','ethereum','ethereum'))              
        self.assertEqual(dm.cal_profit_dict(self,self.test_profit),(profit_list,price_list,date_list,name_list)) # returning 4 diff array of data to be inserted into SQL


    def test_avg_profit(self):
        avg_profit_list = list((0.01,-0.35))                                                                 #average profit of 2 coins
        coins_list = list(('bitcoin','ethereum'))                                                            #coins list
        self.assertEqual(dm.avg_dict(self,self.testavg),(avg_profit_list,coins_list))                        # returning 2 arrays using data of individual daily profit of different coins


if __name__ == '__main__':
    unittest.main() 




