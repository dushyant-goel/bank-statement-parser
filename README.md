# bank-statement-parser
Valyrx Interview Round Project

To install
`pip install -r requirements.txt`

To run
`python3 app.py`

- The app parses the statements in the folder `./statements`
- The parsed transactions can be accesed interactively.  
The three functionalities are : 
1. List all parsed transactions
2. List all transactions by date range
3. List total balance on the date across all accounts, and their total. If the date is earlier than the first known transaction in all accounts, the default balance is 0.

Structure
- statements folder contains the bank statement pdfs
- app folder contains the application logic:
- - db_manager for database queries
  - parser for parsing pdfs
  - app.py for database connection and interactive loop.
 
To Do
- Gmail connection for auto download of bank-statements

