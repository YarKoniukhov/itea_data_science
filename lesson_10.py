import sqlite3
import pandas as pd
import numpy as np


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#  Найти всех родственников по фамилии. В результате должна получиться таблица с 2-мя колонками.
#  В первой колонке полное имя пассажира, во второй всех его родственников на борту (считать родственниками пассажиров,
#  у которых совпадает фамилия) (Titanic)

titanic_data = pd.read_csv('TitanicDataset.csv')


#  Для всех сотрудников, которые совершали какие-либо сделки, вывести дату последней их сделки
#  (chinook/invoices + chinook/customers + chinook/employees)

connection = sqlite3.connect('chinook.db')
chinook_employees = pd.read_sql_query(
    sql="SELECT * FROM employees",
    con=connection
)
chinook_customers = pd.read_sql_query(
    sql="SELECT * FROM customers",
    con=connection
)

chinook_invoices = pd.read_sql_query(
    sql="SELECT * FROM invoices",
    con=connection
)

merge_chinook = pd.merge(
    left=chinook_invoices,
    right=chinook_customers,
    on='CustomerId',
    how='left'
)

invoice_customer = merge_chinook[['InvoiceId', 'CustomerId', 'InvoiceDate', 'SupportRepId']]

merge_inv_cust_empl= pd.merge(
    left=chinook_employees,
    right=invoice_customer,
    left_on='EmployeeId',
    right_on='SupportRepId',
    how='left'
)
merge_inv_cust_empl['InvoiceDate'] = pd.to_datetime(merge_inv_cust_empl.InvoiceDate)
last_transaction = merge_inv_cust_empl.groupby(by=['EmployeeId', 'LastName', 'FirstName']).agg(
    date_of_the_last_transaction=('InvoiceDate', np.max))
print(last_transaction)
