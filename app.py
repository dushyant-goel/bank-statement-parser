# import re
# import pdfplumber

from app import db_manager
from app import parser

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
        db_manager.create_db(conn)
        db_manager.add_to_db(conn, transactions)


if __name__ == '__main__':
    main()