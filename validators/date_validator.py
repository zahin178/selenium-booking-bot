from datetime import datetime as dt

def date_formatter(date:str):
    '''
    formats date from ddmmyyyy into yyyy-mm-dd e.g. '31122022' to '2022-12-31'
    '''
    date_date = date[:2]
    date_month = date[2:4]
    date_year = date[4:]

    re_date =f'{date_year}-{date_month}-{date_date}'

    return re_date

def date_validator(check_in_date:str, check_out_date:str):
    '''
    validates the check-in and check-out dates.
    '''
    check_in_date_date = check_in_date[:2]
    check_in_date_month = check_in_date[2:4]
    check_in_date_year = check_in_date[6:]
    re_check_in_date_string = f'{check_in_date_date}/{check_in_date_month}/{check_in_date_year}'
    re_check_in_date = dt.strptime(re_check_in_date_string, "%d/%m/%y") # converting from string to datetime object

    check_out_date_date = check_out_date[:2]
    check_out_date_month = check_out_date[2:4]
    check_out_date_year = check_out_date[6:]
    re_check_out_date_string = f'{check_out_date_date}/{check_out_date_month}/{check_out_date_year}'
    re_check_out_date = dt.strptime(re_check_out_date_string, "%d/%m/%y") # converting from string to datetime object

    today = dt.today()

    days_gap = re_check_out_date-re_check_in_date
    threshold_gap = 90 # the gap between the check-in date and check-out date cannot be more than 90 days

    if re_check_in_date < re_check_out_date and days_gap.days <= threshold_gap and re_check_in_date >= today:
        return 0
    else:
        print(f'Invalid dates!')
        return 1

