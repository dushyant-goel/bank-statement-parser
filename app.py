import sqlite3

from pathlib import Path

from app.parser import *
from app.db_manager import *

def main():

    directory = 'statements'
    transactions = []

    for pdfpath in Path(directory).rglob('*.pdf'):
        bank = pdfpath.parts[-2]

        if bank == 'BB' :
            transactions += parse_bb(pdfpath)
        elif bank == 'BNI':
            transactions += parse_bni(pdfpath)
        elif bank == 'FCB':
            transactions += parse_fcb(pdfpath)
        elif bank == 'ST':
            transactions += parse_st(pdfpath)
        else:
            print("bank implementation not found")

    with sqlite3.connect('database') as conn:
        create_db(conn)
        add_to_db(conn, transactions)

    while True:
        user_input = input(
            """
            for all parsed transactions
            > 1

            for transaction in date range (dd/mm/yyyy)
            > 2 date_from date_to 

            for balance on date across accounts
            > 3 date

            'q' to quit:
            """
        )

        if user_input == '1':
            get_existing_trans(conn)
        elif user_input == '2':
            date_from = input("Enter start date (dd/mm/yyyy): ")
            date_to = input("Enter end date (dd/mm/yyyy): ")
            get_by_date_range(conn, date_from, date_to)
        elif user_input == '3':
            date = input("Enter date to get balances (dd/mm/yyyy): ")
            get_balance_by_date(date)
        elif user_input.lower() == 'q':
            print("Exiting the loop...")
            break  
        else:
            print("Invalid input. Please enter '1', '2', '3' or 'q'")

if __name__ == '__main__':
    main()