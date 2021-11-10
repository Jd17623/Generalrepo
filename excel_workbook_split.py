import xlwings as xd

EXCEL_FILE = 'C:\Users\Jeffrey\Downloads\Ardent mills\Ardent_POC_Mills_Data (1).xlsx'

try:
    excel_app = xd.App(visible=False)
    wb = excel_app.books.open(EXCEL_FILE)
    for sheet in wb.sheets:
        wb_new = xd.Book()
        sheet.copy(after=wb_new.sheets[0])
        wb_new.sheets[0].delete()
        wb_new.save(f'{sheet.name}.xlsx')
        wb_new.close()
finally:
    excel_app.quit()
