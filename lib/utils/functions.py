from datetime import date, timedelta, datetime
import pandas as pd
import openpyxl

def getInitialDate(end_date):
    end_date = datetime.strptime(end_date, '%d/%m/%Y')
    initial_date = (end_date.replace(day=1)) ## Gets first date from the last month
    ## Formats initial date to DD/MM/YYYY so we can pass the variable on the acceptable format to the API Link
    initial_date = initial_date.strftime('%d/%m/%Y')

    return initial_date


def getFinalDate():
    today = date.today() ## Gets today's date
    first_day = today.replace(day=1) ## Gets first day of the current month
    end_date = (first_day - timedelta(days=1)) ## Reduces 1 day from first day of the current month
    ## Formats initial date to DD/MM/YYYY so we can pass the variable on the acceptable format to the API Link
    end_date = end_date.strftime('%d/%m/%Y')
    
    return end_date


def saveXls(data_frame_dict):
    df = pd.DataFrame(
        data=data_frame_dict
    )
    
    return df


def toExcel(df, path):
    df.to_excel(
        excel_writer=path,
        sheet_name='Inadimplência Regional',
        na_rep='ERROR 404',
        index=False,
    )
