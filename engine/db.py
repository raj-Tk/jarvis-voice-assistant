import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()   # variable which execute the query


#system command
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'One Note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# con.commit() # this is to saved the database at current  stage

# ------------- this is commemnt out cuz if executed once again it will create dublicate file ----------


#webcommand

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)


# query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.in/')"
# cursor.execute(query)
# con.commit() # this is to saved the database at current  stage

# query = "INSERT INTO web_command VALUES (null,'YouTube', 'https://www.youtube.com/')"
# cursor.execute(query)
# con.commit() # this is to saved the database at current  stage



# query = "INSERT INTO web_command VALUES (null,'YouTube Music ', 'https://music.youtube.com/')"
# cursor.execute(query)
# con.commit() # this is to saved the database at current  stage