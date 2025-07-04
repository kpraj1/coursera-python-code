import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript(
'''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);    

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (course_id) REFERENCES Course(id)
);
'''
)

fname = input('Enter the input file name: ')
if len(fname)<1:
    fname = 'roster_data_sample.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0];
    title = entry[1];
    role = entry[2];

   # print((name,title))

    cur.execute('''INSERT OR IGNORE INTO User(name) VALUES (?)''',(name,))
    cur.execute('SELECT id FROM User WHERE name = ?',(name,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course(title) VALUES (?)''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Member(user_id,course_id,role) VALUES (?,?,?)''', (user_id,course_id,role))

    conn.commit()

sqlstr = '''SELECT User.name, Member.role, Course.title
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name'''

# Print header
print('\n{:<30} {:<5} {:>5}'.format("Name", "Role", "Course id"))
print("-" * 50)
# Print each row with nicely formatted output
for row in cur.execute(sqlstr):
    #print("DEBUG: row =", row)  # This shows exactly what each row looks like - DEBUG: row = ('cwen@iupui.edu', 5)
    #print(row[0],row[1],row[2])
    print("\n{:<30} {:<5} {:>5}".format(row[0],row[1],row[2]))
cur.close()
