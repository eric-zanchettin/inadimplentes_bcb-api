import requests
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import os

from lib.region_codes import regions
import lib.utils.functions as utils

print('Criando arquivos necessários ...')

keys = regions.keys()
data_frame_dict = {'Estado': [], 'Valor': []}

print('Adquirindo data da última atualização de Inadimplência do BCB ...')

end_date = utils.getFinalDate()
initial_date = utils.getInitialDate(end_date)

print('Conectando à API de Inadimplência Regional do BCB ...')

i = 1
for key in keys:
    response = requests.get(f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{regions[key]}/dados?formato=json&dataInicial={initial_date}&dataFinal={end_date}")
    data_frame_dict['Estado'].append(key)
    data_frame_dict['Valor'].append(response.json()[0]['valor'])
    print(f'{i} - {key} ✔ ({int((i/27)*100)}%)')
    i += 1

initial_date = initial_date.replace('/', '.')
end_date = end_date.replace('/', '.')

name_file = f'Inadimplência Regional {initial_date} - {end_date}.xlsx'

print('Salvando arquivos ...')

df = utils.saveXls(data_frame_dict)

utils.toExcel(df, f'./lib/generated/{name_file}')

while True:
    try:
        save_xls = filedialog.askdirectory()
        utils.toExcel(df, f'{save_xls}/{name_file}')

        break
    except:
        print('Você deve escolher um diretório para salvar ...')

input('Sucesso! Aperte "Enter" para finalizar ...')
os.startfile(f'{save_xls}/{name_file}')