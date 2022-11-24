import unittest
from validators.guest_validator import guest_validator

class TestGuest(unittest.TestCase):

    def test_guest_validator(self):
        # cases for number of adults
        self.assertEqual(guest_validator(31,2,[3,10],2),1)
        self.assertEqual(guest_validator(103,2,[3,10],2),1)

        # cases for number of rooms
        self.assertEqual(guest_validator(3,2,[3,10],31),2)
        self.assertEqual(guest_validator(3,2,[3,10],123),2)

        # case of no children and no ages
        self.assertEqual(guest_validator(3,None,None,2),0)

        # case of no children with some ages
        self.assertEqual(guest_validator(3,None,[3],2),3)
        self.assertEqual(guest_validator(3,None,[3,4,6,7],2),3)

        # case of number of children
        self.assertEqual(guest_validator(3,11,[1,2,3,4,5,6,7,8,9,10,11],2),4)

        # case of children with no ages
        self.assertEqual(guest_validator(3,1,None,2),5)
        self.assertEqual(guest_validator(3,10,None,2),5)

        # case of chlidren ages less than children
        self.assertEqual(guest_validator(3,3,[12,9],2),6)
        self.assertEqual(guest_validator(3,2,[9],2),6)
        self.assertEqual(guest_validator(3,4,[11,12],2),6)

        # case of chlidren ages greater than children
        self.assertEqual(guest_validator(3,3,[12,9,7,0],2),7)
        self.assertEqual(guest_validator(3,2,[9,2,12,12],2),7)
        self.assertEqual(guest_validator(3,4,[11,12,9,0,3],2),7)

        # case for valid children ages
        self.assertEqual(guest_validator(3,3,[12,14,18],2),8)
        self.assertEqual(guest_validator(3,3,[18,20,22],2),8)
        self.assertEqual(guest_validator(3,3,[18,18,18],2),8)

        # case with valid values
        self.assertEqual(guest_validator(3,1,[0],2),0)
        self.assertEqual(guest_validator(1,0,[],1),0)
        self.assertEqual(guest_validator(4,None,None,2),0)
        self.assertEqual(guest_validator(5,3,[12,14,17],2),0)
        self.assertEqual(guest_validator(30,10,[1,2,3,4,5,6,7,8,9,10],30),0)






        

