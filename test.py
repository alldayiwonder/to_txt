import xlrd
import csv

def csv_from_excel(file_path):
    csv_name = file_path.split("/")[-1].split(".")[0]+".csv"
    wb = xlrd.open_workbook(file_path)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(csv_name, 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

csv_from_excel("thing.xlsx")
