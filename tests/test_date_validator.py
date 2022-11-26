import unittest
from validators.date_validator import date_validator, date_formatter
from datetime import date, timedelta

class TestDateValidator(unittest.TestCase):

    def test_date_validator(self):
        # case 1: check-in date is after or same as the check-out date
        date1a = '30122022'
        date1b = '30122022'
        self.assertEqual(date_validator(date1a, date1b), 1)
        date2a = '30122022'
        date2b = '13122022'
        self.assertEqual(date_validator(date2a, date2b), 1)
        date3a = '30122022'
        date3b = '30112022'
        self.assertEqual(date_validator(date3a, date3b), 1)
        date4a = '30012023'
        date4b = '30122022'
        self.assertEqual(date_validator(date4a, date4b), 1)

        # case 2: gap between check-in and check-out dates within 90 days
        date5a = '01012023'
        date5b = '02042023'
        self.assertEqual(date_validator(date5a, date5b), 2)
        date6a = '01012023'
        date6b = '01012024'
        self.assertEqual(date_validator(date6a, date6b), 2)
        
        # case 3: chcek-in date is before today
        delta7 = timedelta(days=1)
        today = date.today()
        date7a = today-delta7
        date7b = today+delta7
        date7a_str = date7a.strftime('%d%m%Y')
        date7b_str = date7b.strftime('%d%m%Y')
        self.assertEqual(date_validator(date7a_str, date7b_str), 3)
        delta8 = timedelta(days=30)
        today = date.today()
        date8a = today-delta8
        date8b = today+delta8
        date8a_str = date8a.strftime('%d%m%Y')
        date8b_str = date8b.strftime('%d%m%Y')
        self.assertEqual(date_validator(date8a_str, date8b_str), 3)

        # case 4: valid dates
        today = date.today()

        delta9a = timedelta(days=30)
        delta9b = timedelta(days=35)
        date9a = today+delta9a
        date9b = today+delta9b
        date9a_str = date9a.strftime('%d%m%Y')
        date9b_str = date9b.strftime('%d%m%Y')
        self.assertEqual(date_validator(date9a_str, date9b_str), 0)

        delta10a = timedelta(days=30)
        delta10b = timedelta(days=31)
        date10a = today+delta10a
        date10b = today+delta10b
        date10a_str = date10a.strftime('%d%m%Y')
        date10b_str = date10b.strftime('%d%m%Y')
        self.assertEqual(date_validator(date10a_str, date10b_str), 0)

        delta11a = timedelta(days=1)
        delta11b = timedelta(days=91)
        date11a = today+delta11a
        date11b = today+delta11b
        date11a_str = date11a.strftime('%d%m%Y')
        date11b_str = date11b.strftime('%d%m%Y')
        self.assertEqual(date_validator(date11a_str, date11b_str), 0)

    def test_date_formatter(self):
        input1 = '01012022'
        output1 = '2022-01-01'
        self.assertEqual(date_formatter(input1), output1)

        input2 = '12122022'
        output2 = '2022-12-12'
        self.assertEqual(date_formatter(input2), output2)

        input3 = '20221201'
        output3 = ValueError
        self.assertEqual(date_formatter(input3), output3)

        input4 = '051122'
        output4 = ValueError
        self.assertEqual(date_formatter(input4), output4)


        
        


        


