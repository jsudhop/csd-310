#Jon Sudhop
#12/1/21
#Assignment 9.2 - MySQL joins

#I forgot the new requirements last week, sorry.

#just copied over the code from the previous weeks again here, this time i remember to pay attention to styling and was consistent on spaces.
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "jsudhop",
    #note to self, use a generic password.....
    "password": "MyDBPassword1",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
#Try/except block for raising potential errors on connection
try:
    db = mysql.connector.connect(**config)

    print("\n Database User {} connected to MySQL on host {} with database {}.".format(config["user"], config["host"], config["database"]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password was invalid.")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist.")

    else:
        print(err)

finally:
    db.close

#I am amazed at how easily python does basically everything I've had to use it for so far, pretty great to work with.  
cursor = db.cursor()
#I am also amazed at how simple MySQL queries are.
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()

#I tried to exactly copy the output style you had
print("")
print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print("")

input("\n\n Press any key to continue...")