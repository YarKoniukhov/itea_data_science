import pandas as pd
import sqlite3

# В столбце Pclass заменить оригинальные значения 1, 2, 3 на текст "First", "Second", "Third" (TitanicDataset)
titanic_data = pd.read_csv('TitanicDataset.csv',
                           sep=',',
                           header=0
                           )

titanic_data['Pclass'].replace([1, 2, 3], ['First', 'Second', 'Third'], inplace=True)
print(titanic_data.head(10))


# Найти пассажиров, у которых был самый дорогой билет (TitanicDataset)
expensive_ticket = titanic_data.loc[titanic_data['Fare'].argmax()]
print(expensive_ticket)


# Найти пассажиров с максимальным количеством родственников на борту (TitanicDataset)
max_relatives = titanic_data.loc[(titanic_data['SibSp'] + titanic_data['Parch']).argmax()]
print(max_relatives)


# Найти количество преступлений, произошедших в декабре 2012 года в интервале между часом ночи и пятью утра (CrimesData)
crime_data = pd.read_excel(
    'CrimesData.xlsx',
    sheet_name='2012',
    parse_dates=['CrimeDate']
)


def fix_time(cell):
    if len(cell) == 4 and ':' not in cell:
        return f'{cell[:2]}:{cell[2:]}:00'
    else:
        return cell


crime_data['CrimeTime'] = crime_data['CrimeTime'].apply(fix_time)

time_of_crime = crime_data[['CrimeDate', 'CrimeTime']][
    (crime_data.CrimeDate >= '2012-12-01') &
    (crime_data.CrimeDate <= '2012-12-31') &
    (crime_data.CrimeTime >= '01:00:00') &
    (crime_data.CrimeTime <= '05:00:00')
    ]

print(f'number of crimes: {len(time_of_crime)}')


# Вычислить средний интервал между преступлениями за 2012 год в часах (CrimesData)


# Заменить пропущенные значения возраста на среднее, в зависимости от пола и класса каюты (Titanic)
titanic_data['Age'] = titanic_data.groupby(['Pclass', 'Sex']).Age.apply(lambda x: x.fillna(x.mean()))


# Найти общую сумму продаж по месяцам 2019-го года; вывести в формате месяц - сумма в порядке возрастания суммы (Sales)
sales_data = pd.read_csv('SalesData.csv',
                         parse_dates=['OrderDate']
                         )

date_2019 = sales_data[['OrderDate', 'Total']][
    (sales_data.OrderDate >= '2019-01-01') &
    (sales_data.OrderDate <= '2019-12-31')]

date_2019['Month'] = date_2019['OrderDate'].dt.strftime('%B')

month_total = date_2019.groupby(['Month'])['Total'].sum().reset_index().sort_values('Total', ascending=True)
print(month_total)


# Найти всех исполнителей, у которых более 10 альбомов (chinook/albums)
connection = sqlite3.connect('chinook.db')
chinook_album = pd.read_sql_query(
    sql="SELECT * FROM albums",
    con=connection
)

filtered_artist = chinook_album['ArtistId'].value_counts().loc[lambda x: x >= 10].to_frame()
print(filtered_artist)


# Выберите всю информацию по инвойсам, сумма которых в 3 раза превышает среднее значение (chinook/invoices)
connection = sqlite3.connect('chinook.db')
chinook_invoices = pd.read_sql_query(
    sql="SELECT * FROM invoices",
    con=connection
)

invoice_three_times_more = chinook_invoices.loc[(chinook_invoices['Total'].mean() * 3) < chinook_invoices['Total']]
print(invoice_three_times_more)