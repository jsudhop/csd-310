#Jon Sudhop
#12/1/21
#Assignment 9.3 - MySQL update and delete

#I just copied over the code from the previous weeks again here.
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

#Create cursor
cursor = db.cursor()

#do the insert
cursor.execute("INSERT INTO player (player_id, first_name, last_name, team_id) Values (21, 'Smeagol', 'Shire Folk', 1)")

#printing the insert
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()

#Mine seems to only want to put Smeagol with the rest of his team, unlike yours, not sure how to make that look different.  But it is at least actually adding him in.
print("")
print("-- DISPLAYING PLAYER RECORDS AFTER INSERT--")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print("")

#do the update
cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

#printing again
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()

print("")
print("-- DISPLAYING PLAYER RECORDS AFTER UPDATE--")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print("")

#lava does tend to delete people
cursor.execute("DELETE FROM player WHERE player_id = 21")

#one last print
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
players = cursor.fetchall()

print("")
print("-- DISPLAYING PLAYER RECORDS AFTER DELETE--")
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team Name: {}".format(player[3]))
    print("")

#making sure we are able to see our output before exiting
input("\n\n Press any key to continue...")