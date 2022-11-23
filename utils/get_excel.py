import xlsxwriter
from pathlib import Path

def excel_maker(dataset, destination):
    excel_path = Path(__file__).parents[1]/ f'outputs/{destination}.xlsx'
    workbook = xlsxwriter.Workbook(excel_path)
    worksheet = workbook.add_worksheet('data')

    worksheet.write(0,0,'Hotel Name')
    worksheet.write(0,1,'Hotel Score')
    worksheet.write(0,2,'Hotel Reviews')
    worksheet.write(0,3,'Hotel Distance')

    for i,data in enumerate(dataset):
        worksheet.write(i+1,0,data['title'])
        worksheet.write(i+1,1,data['score'])
        worksheet.write(i+1,2,data['review_cnt'])
        worksheet.write(i+1,3,data['distance'])

    workbook.close()


