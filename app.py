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

if __name__ == '__main__':
    main()