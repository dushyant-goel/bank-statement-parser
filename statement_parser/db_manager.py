from datetime import datetime

def create_db(conn):
    conn.execute(
        """
        CREATE TABLE transactions (
            id INTEGER PRIMARY KEY,
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
        (date, description, credit, debit, balance)
        VALUES
        (?, ?, ?, ?, ?)
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

def get_by_date_range(conn):
    pass

def get_balance_by_date(conn):
    pass

