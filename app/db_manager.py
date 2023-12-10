from datetime import datetime

def create_db(conn):
    conn.execute(
        """
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY,
            account varchar(255),
            date datetime,
            description varchar(255),
            credit REAL,
            debit REAL,
            balance REAL)
        """
    )

def add_to_db(conn, transactions):
    conn.executemany(
        """
        INSERT INTO transactions
        (account, date, description, credit, debit, balance)
        VALUES
        (?, ?, ?, ?, ?, ?)
        """,
        transactions
    )

def get_existing_trans(conn):
    existing_rows = conn.execute(
        """
        SELECT *
        FROM transactions
        """
    ).fetchall()

    print(existing_rows)

def get_by_date_range(conn, date_from, date_to):
    result_set = conn.execute(
        """
        SELECT *
        FROM transactions
        WHERE date BETWEEN ? AND ? 
        """, 
        [date_from, date_to]
    ).fetchall()

    print(result_set)

def get_balance_by_date(conn):
    result_set = conn.execute(
        """ 
        SELECT account_no, max(date), balance
        FROM your_table
        WHERE date <= ?  
        GROUP BY account_no
        """, [date]
    )

    balance = 0.0
    for transaction in result_set:
        print(transaction)
        balance += float(transaction[2].replace(',',''))

    print("total across accounts: ?", balance)
