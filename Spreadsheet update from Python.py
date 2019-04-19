import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials1.json', scope)

client = gspread.authorize(credentials)

sheet = client.open('Name of the Spreadsheet').sheet1


values = ["Argentina", "Uruguay"]
sheet.insert_row(values, 4) # crea una nueva fila entre las 3 y la 4 e inserta los valores de la variable values en la nueva fila 4 (En la celda A4 Argentina y en la celda B4 Uruguay)
