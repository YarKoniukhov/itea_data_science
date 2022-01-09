import pandas as pd
import sqlite3


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#  В предыдущем разделе мы получили словарь таблиц при чтении из Excel файла - crime_data.
#  Необходимо объединить все таблицы словаря в один DataFrame

crime_data = pd.read_excel(
    'CrimesData.xlsx',
    sheet_name=None
)
crime_d = pd.concat(crime_data, axis=0)


# Найти уникальные комбинации значений колонок `Survived/Pclass/Sex` для пассажиров, у которых не известен возраст

connection = sqlite3.connect('TitanicDataset.db')
titanic_data = pd.read_sql_query(
    sql="SELECT * FROM MainTable",
    con=connection
)

titanic_data.dropna(subset=['Age'], inplace=True)
new_titanic_data = titanic_data.drop_duplicates(subset=['Survived', 'Pclass', 'Sex'])

print(new_titanic_data)

