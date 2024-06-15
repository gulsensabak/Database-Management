#Standard library import
import mysql.connector
import json
#Connect with the precise info, also with dataset name
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="7gimtwDS.1.1",
  database="volleyballdatabase"
)


def return_team_id(username):
    
    mycursor = mydb.cursor()
    query = f"""SELECT team_ID
    FROM team
    WHERE coach_username = '{username}'
    AND NOW() BETWEEN contract_start AND contract_finish"""
    mycursor.execute(query)
    shows=[]
    for i in mycursor:
        shows.append({"team_id": i[0]})
    mycursor.close()
    return shows

def delete_session(session_id):
    mycursor = mydb.cursor()
    query = f"""DELETE FROM match_session
WHERE session_ID = '{session_id}'"""
    mycursor.execute(query)
    mycursor.close()


def returns_sessions(coach_name):
    mycursor = mydb.cursor()
    query = f"""SELECT ms.session_ID
        FROM team t
        JOIN match_session ms ON t.team_ID = ms.team_id
        WHERE t.coach_username = '{coach_name}'"""
    shows=[]
    mycursor.execute(query)
    for i in mycursor:
        shows.append({"session_ID": i[0]})
    mycursor.close()

    return shows


def add_session(username, session_ID, team_id, stadium_ID, time_slot, date, assigned_jury_username, played_player_username_list):
    mycursor = mydb.cursor()
    shows=return_team_id(username)[0]["team_id"]
    rating = None
    if(len(session_ID)==0):
        session_ID="NULL"
    else:
        session_ID="'" + session_ID + "'"
    if(len(team_id)==0):
        team_id2="NULL"
    else:
        team_id2="'" + team_id + "'"    
    if(len(stadium_ID)==0):
        stadium_ID="NULL"
    else:
        stadium_ID="'" + stadium_ID + "'"    
    if(len(time_slot)==0):
        time_slot="NULL"
    else:
        time_slot="'" + time_slot + "'"    
    if(len(date)==0):
        date="NULL"
    else:
        date="'" + date + "'"    
    if(len(assigned_jury_username)==0):
        assigned_jury_username="NULL"
    else:
        assigned_jury_username="'" + assigned_jury_username + "'"
    if(len(played_player_username_list)==0):
        played_player_username_list="NULL"
    else:
        played_player_username_list="'" + played_player_username_list + "'"


    if(shows==int(team_id)):
        query = f"INSERT INTO match_session (session_ID, team_id, stadium_ID, time_slot, date, assigned_jury_username, rating, played_player_username_list) VALUES ({session_ID}, {team_id2}, {stadium_ID}, {time_slot}, {date}, {assigned_jury_username}, NULL, {played_player_username_list})"
        mycursor.execute(query)
        mycursor.close()

        return (True, shows)

    else:
        mycursor.close()

        return (False,shows)


def return_std_name_and_counties():
    mycursor = mydb.cursor()
    query ="SELECT S.stadium_name, S.stadium_country FROM stadium S;"
    shows=[]
    mycursor.execute(query)
    for i in mycursor:
        shows.append({"name": i[0],"surname": i[1]})
    mycursor.close()

    return shows

def return_player_home1(username):
    mycursor = mydb.cursor()
    query = f"""
        SELECT DISTINCT
            u.name,
            u.surname
        FROM 
            played_in_m pm
        JOIN 
            user u ON pm.username = u.username
        WHERE 
            pm.session_ID IN (
                SELECT 
                    session_ID
                FROM 
                    match_session
        WHERE 
            JSON_CONTAINS(played_player_username_list->'$[*]', '"{username}"') > 0
    )

    """
    shows=[]
    mycursor.execute(query)
    for i in mycursor:
        shows.append({"name": i[0],"surname": i[1]})
    mycursor.close()

    return shows




def return_player_home2(username):
    mycursor = mydb.cursor()
    query = f"""
        SELECT
    AVG(p.height) AS average_height
FROM 
    player p
JOIN 
    user u ON p.username = u.username
WHERE 
    p.username IN (
        SELECT
            p.username
        FROM 
            played_in_m pm
        JOIN 
            player p ON pm.username = p.username
        JOIN 
            user u ON p.username = u.username
        WHERE 
            pm.session_ID IN (
                SELECT 
                    session_ID
                FROM 
                    match_session
                WHERE 
                    JSON_CONTAINS(played_player_username_list->'$[*]', '"{username}"') > 0
            )
        AND
            p.username != '{username}' -- Exclude username
        GROUP BY
            p.username
        HAVING
            COUNT(p.username) = (
                SELECT 
                    MAX(player_count)
                FROM (
                    SELECT
                        COUNT(p.username) AS player_count
                    FROM 
                        played_in_m pm
                    JOIN 
                        player p ON pm.username = p.username
                    JOIN 
                        user u ON p.username = u.username
                    WHERE 
                        pm.session_ID IN (
                            SELECT 
                                session_ID
                            FROM 
                                match_session
                            WHERE 
                                JSON_CONTAINS(played_player_username_list->'$[*]', '"{username}"') > 0
                        )
                    GROUP BY
                        p.username
                ) AS max_player_count
            )
    )

    """
    shows=[]
    mycursor.execute(query)
    for i in mycursor:
        shows.append({"height": i[0]})

    mycursor.close()

    return shows

    
def return_unrated_sessions(jury_username):
    mycursor = mydb.cursor()
    query = f"""
    SELECT 
            m.session_ID
        FROM 
            match_session m
        LEFT JOIN 
            rate r ON m.session_ID = r.session_ID
        LEFT JOIN 
            jury j ON m.assigned_jury_username = j.username
        WHERE 
            m.assigned_jury_username = '{jury_username}'
            AND m.rating IS NULL
            AND m.date < CURDATE()
    """
    shows=[]
    mycursor.execute(query)
    for i in mycursor:
        shows.append({"name": i[0]})
    mycursor.close()

    return shows


def returnRatings(jury_username):
    mycursor = mydb.cursor()
    query = """
        SELECT 
            j.username, 
            AVG(m.rating) AS avrge_rating, 
            COUNT(*) AS total_rated_sessions 
        FROM 
            jury j 
        JOIN 
            rate r ON j.username = r.username 
        JOIN 
            match_session m ON r.session_ID = m.session_ID AND j.username = m.assigned_jury_username
        WHERE 
            j.username = %s
        GROUP BY 
            j.username
            """
    shows=[]
    mycursor.execute(query, (jury_username,))
    for i in mycursor:
        shows.append({"username": i[0], "avg_rating": i[1], "count": i[2]})
    mycursor.close()

    return shows

def rate_sessions(username ,Match_Session_ID ,rate):
    mycursor = mydb.cursor()
    query = f"UPDATE match_session SET rating = '{rate}' WHERE session_ID = '{Match_Session_ID}' AND assigned_jury_username = '{username}'"
    mycursor.execute(query)
    query = f"INSERT INTO rate (session_ID, username) VALUES ('{Match_Session_ID}', '{username}')"
    mycursor.execute(query)
    mycursor.close()



def create_player(username, date_of_birth, height, weight, password):
    if not isManName(username):
        mycursor = mydb.cursor()
        query =f"INSERT INTO user (username, password) VALUES('{username}', '{password}')"
        mycursor.execute(query)
        query =f"INSERT INTO player (username, date_of_birth, height, weight, password) VALUES('{username}', '{date_of_birth}', '{height}', '{weight}', '{password}')"
        mycursor.execute(query)
        mycursor.close()
        return False
    else:
        return True



def create_coach(username, nationality, password):
    if not isManName(username):
        mycursor = mydb.cursor()
        query =f"INSERT INTO user (username, password) VALUES('{username}', '{password}')"
        mycursor.execute(query)
        query =f"INSERT INTO coach (username, nationality, password) VALUES('{username}', '{nationality}', '{password}')"
        mycursor.execute(query)
        mycursor.close()
        return False
    else:
        return True

    
def create_jury(username, nationality, password):
    if not isManName(username):
        mycursor = mydb.cursor()
        query =f"INSERT INTO user (username, password) VALUES('{username}', '{password}')"
        mycursor.execute(query)
        query =f"INSERT INTO jury (username, nationality, password) VALUES('{username}', '{nationality}', '{password}')"
        mycursor.execute(query)
        mycursor.close()
        return False
    else:
        return True


def returnStadimName():
    shows=[]
    mycursor = mydb.cursor()
    mycursor.execute("SELECT S.stadium_name FROM stadium S")
    for x in mycursor:
        shows.append({"name": x[0]})
    mycursor.close()

    return shows

def changeStadium(old_name, new_name):
    mycursor = mydb.cursor()
    query = f"UPDATE stadium SET stadium_name = '{new_name}' WHERE stadium_name = '{old_name}'"
    mycursor.execute(query)
    mycursor.close()



def coach_return_available_session(coach_name):
    mycursor = mydb.cursor()
    query = f"""SELECT m.session_ID
        FROM match_session m
        WHERE m.played_player_username_list IS NULL
        AND m.team_ID IN (
            SELECT t.team_ID
            FROM team t
            WHERE t.coach_username = '{coach_name}'
            AND NOW() BETWEEN t.contract_start AND t.contract_finish
        )"""
    mycursor.execute(query)
    shows=[]
    for x in mycursor:
        shows.append({"name": x[0]})
    mycursor.close()

    return shows

def coach_return_player_names(coach_name):
    mycursor = mydb.cursor()
    query = f"""SELECT register.username
FROM register
JOIN player ON register.username = player.username
WHERE register.team_ID = (
    SELECT team_ID
    FROM team
    WHERE coach_username = '{coach_name}'
    AND NOW() BETWEEN contract_start AND contract_finish
) """
    mycursor.execute(query)
    shows=[]
    for x in mycursor:
        shows.append({"username": x[0]})
    mycursor.close()

    return shows

def coach_add_new_squad_quer( playerlist,session):
    mycursor = mydb.cursor()
    playerlist_json = json.dumps(playerlist)
    query = f"""UPDATE match_session SET played_player_username_list = '{playerlist_json}' WHERE session_ID = '{session}'"""
    mycursor.execute(query)
    mycursor.close()


def isManName(username):
    mycursor = mydb.cursor()

    mycursor.execute("SELECT M.username, M.password FROM manager M")
    for x in mycursor:
        if username==x[0]:
            mycursor.close()
            return True
    mycursor.close()
    return False
        
