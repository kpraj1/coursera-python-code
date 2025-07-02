import sqlite3

# Connect to the SQLite database file (or create it if it doesn't exist)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Drop the table if it already exists to start fresh
cur.execute('DROP TABLE IF EXISTS Counts')

# Create a new table named Counts with auto-incrementing SNo
cur.execute('''
    CREATE TABLE Counts(
        SNo INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        count INTEGER
    )
''')

# Ask user for input file name; use default if empty
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'mbox-short.txt'

# Open the file for reading
fh = open(fname)

# Process each line in the file
for line in fh:
    if not line.startswith('From: '):  # Only process lines that start with 'From: '
        continue
    pieces = line.split()
    email = pieces[1]  # Extract the email address

    # Check if this email already exists in the database
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()

    if row is None:
        # Insert a new email with count 1
        cur.execute('INSERT INTO Counts(email, count) VALUES (?, 1)', (email,))
    else:
        # Update the existing count for that email
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    conn.commit()  # Commit changes after each line

# Retrieve top 10 emails by descending count
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# Print header
print("\n{:<30} {:>5}".format("Email", "Count"))
print("-" * 36)

# Print each row with nicely formatted output
for row in cur.execute(sqlstr):
    #print("DEBUG: row =", row)  # This shows exactly what each row looks like - DEBUG: row = ('cwen@iupui.edu', 5)
    print("{:<30} {:>5}".format(row[0], row[1]))

cur.close()
