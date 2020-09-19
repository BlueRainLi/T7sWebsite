import requests as res
import sqlite3
import os
import re

db = "static/db/t7s.db"
sql_path = "static/sql/"
sql_url = "https://resource.t7s.sagilio.net/asset/sorted/sql/"
sql_list = ["m_card.sql",
            "m_character.sql",
            "m_live_music.sql",
            "m_rarity.sql",
            "m_card_type.sql"]


def get_sql(sql_list:list, sql_url:str) -> None:
    """
    Get the sql file from the api.
    :param sql_list: a list consists of names of sql.
    :param sql_url: an url of the api
    :return: None
    """
    current_path = os.getcwd()
    for item in sql_list:
        url = sql_url+item
        sql_content = res.get(url).content
        with open(current_path+"/static/sql/"+item,'wb') as f:
            f.write(sql_content)
        print(item+" saved")


def version() -> list:
    '''
    Get the current version of Tokyo 7th Sister.
    :return: str
    '''
    version_link = res.get("https://status.t7s.sagilio.net/info/version")
    ver = version_link.json()["gameVersion"]["version"]
    return ver

def create_command (post:dict,select:str,table:str) -> str:
    '''
    Create a select command from a list posted
    :param post: list
    :return: str
    '''
    Command = "SELECT "+select+" FROM "+table
    if post != {}:
        Command += " WHERE "
    keys = list(post.keys())
    for key in keys:
        if post[key] == "":
            del post[key]
    keys = list(post.keys())
    for key in keys:
        Command += key+"="+"'"+str(post[key])
        if key == keys[-1]:
            Command += "' "
        else:
            Command += "',"
    Command += ";"
    return Command

def select(db:str, operation:str) -> list:
    '''
    Execute the operation to the database
    :rtype: object
    :param db: path of the database
    :param operation: the string of the operation
    :return: list
    '''
    address = os.getcwd()
    db = address+db
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(operation)
    content = cursor.fetchall()
    conn.close()
    return content



def update_table(db:str, sql:str, sql_path:str):
    '''
    update the table by sql file
    :param db: path of the database
    :param sql: filename of sql file
    :param sql_path: path of the sql file
    :return: None
    '''
    table_name = sql[:-4]

    with open(sql_path+sql,'r',encoding="UTF-8") as f:
        content = f.readlines()

    col_name = re.search(r"\((.*)\)",content[1])
    col_name = col_name[1].split(",")
    for i in range(len(col_name)):
        col_name[i] = col_name[i][1:-1]+" varchar(255)"
    create_cmd = "CREATE TABLE "+table_name+" ( "+",".join(col_name)+" )"

    content = "".join(content).split(";")[:-1]

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    try:
        cursor.execute(create_cmd)
    except:
        print("Table %s has been created"%table_name)
    else:
        print("Table %s is created"%table_name)

    for item in content:
        try:
            cursor.execute(item)
        except sqlite3.OperationalError:
            continue
    conn.commit()
    conn.close()


if __name__ == '__main__':
    print("Current version:",version())
    get_sql(sql_list, sql_url)
    for item in sql_list:
        update_table(db, item, sql_path)
