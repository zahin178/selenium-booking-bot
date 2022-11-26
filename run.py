from main.booking import Booking
from validators import date_validator, guest_validator
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--currency', type=str, help='Type of currency e.g. "USD", "GPB", "EUR" ')
parser.add_argument('-d', '--destination', type=str, required=True, help='Destination name')
parser.add_argument('-ci','--check_in', type=str, required=True, 
                    help='Check in date in the format of ddmmyyyy e.g for 26th June 2022 the input value should be 26062022')
parser.add_argument('-co','--check_out', type=str, required=True, 
                    help='Check out date in the format of ddmmyyyy e.g for 7th May 2023 the input value should be 07052023')
parser.add_argument('-an', '--adult_num', type=int, required=True, help='Number of total adults')
parser.add_argument('-cn', '--children_num', type=int, help='Number of total children')
parser.add_argument('-ca', '--children_ages', type=str, help='Children ages with space between the ages e.g. 11 7 6...')
parser.add_argument('-rn', '--room_num', type=int, help='Number of total rooms', required=True)
# parser.add_argument('-get', '--get_data', action='store_true', help='Set to True if the excel file is required, else False')

args = parser.parse_args()

currency = args.currency
destination = args.destination
check_in_date = args.check_in
check_out_date = args.check_out
adult_num = args.adult_num
children_num = args.children_num
children_ages_str = args.children_ages
children_ages = None
rooms = args.room_num
# data_bool = args.get_data
# print('data_bool',data_bool)


if children_ages_str:
    children_ages = children_ages_str.split(' ')

# running the validations
date_val_res = date_validator.date_validator(check_in_date, check_out_date)
guest_val_res = guest_validator.guest_validator(adult_num, children_num, children_ages, rooms)


if date_val_res + guest_val_res == 0:
    with Booking() as b:
        if b.open_first_page():
            if currency:
                b.change_currency(currency)
            b.select_destination(destination)
            b.set_dates(check_in_date, check_out_date)
            b.set_guests(adult_num, children_num, children_ages, rooms)
            b.apply_search()
            # if data_bool:
            b.make_data(destination)
            print('Completed')
        else:
            print('Could not find the desired element, Please run again!')

else:
    print('Invalid Inputs')

