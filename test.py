def date_formatter(date:str):
    '''
    formats date from ddmmyyyy into yyyy-mm-dd
    '''
    date_date = date[:2]
    date_month = date[2:4]
    date_year = date[4:]

    re_date =f'{date_year}-{date_month}-{date_date}'

    return re_date

print(date_formatter('31122022'))