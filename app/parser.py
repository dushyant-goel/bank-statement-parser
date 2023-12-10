
import re
import pdfplumber

from pathlib import Path

def parse_bb(pdfpath):
    text = ""

    with pdfplumber.open(pdfpath) as pdf:
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=1)

        # print(text)
        transactions = re.findall(r'(\d{2}/\d{2}/\d{4})\s(.*?)\s([\d,]+\.\d{2})\s([\d,]+\.\d{2})\s([\d,]+\.\d{2})', text)

    return transactions
    # print(transactions)
    # for transaction in transactions:
    #     date, description, credit, debit, balance = transaction
    #     print(f"Date: {date}, Description: {description}, Credit: {credit}, Debit: {debit}, Balance: {balance}")

def parse_bni(pdfpath):
    text = ""

    with pdfplumber.open(pdfpath) as pdf:
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=1)

        # print(text)
        transactions = re.findall(r'(\d{2}/\d{2}/\d{4})\s(.*?)\s([\d,]+\.\d{2})\s([\d,]+\.\d{2})\s([\d,]+\.\d{2})', text)

    return transactions
    # print(transactions)

    # for transaction in transactions:
    #     date, description, credit, debit, balance = transaction
    #     print(f"Date: {date}, Description: {description}, Credit: {credit}, Debit: {debit}, Balance: {balance}")

def parse_fcb(pdfpath):
    text = ""

    with pdfplumber.open(pdfpath) as pdf:
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=1)

        # print(text)
        transactions = re.findall(r'(\d{2}/\d{2}/\d{4})\s(.*?)\s([\d,]+\.\d{2})\s([\d,]+\.\d{2})\s([\d,]+\.\d{2})', text)

    return transactions
    # print(transactions)

    # for transaction in transactions:
    #     date, description, credit, debit, balance = transaction
    #     print(f"Date: {date}, Description: {description}, Credit: {credit}, Debit: {debit}, Balance: {balance}")    

def parse_st(pdfpath):
    text = ""

    with pdfplumber.open(pdfpath) as pdf:
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=1)

        # print(text)
    
    raw_transactions = re.findall(r'(\d{2}/\d{2}/\d{4})\s(.*?)\s([\d,]+\.\d{2})', text)
    transactions = []

    previous_balance = 0.0
    for transaction in transactions:
        date, description, amount = transaction
        amount = float(amount)

        if(amount < 0) :
            credit = -amount
            debit = 0.0
        else :
            credit = 0.0
            debit = amount

        balance = previous_balance - amount
        previous_balance = balance

        transactions += [(date, description, credit, debit, balance)]

        # print(f"Date: {date}, Description: {description}, Credit: {credit}, Debit: {debit}, Balance: {balance}")
    
    return transactions
