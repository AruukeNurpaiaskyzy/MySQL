import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully connected ...")
    print("#" * 20)

    try:
        with connection.cursor() as cursor:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS `user` (
                id INT AUTO_INCREMENT,
                name VARCHAR(32),
                password VARCHAR(32),
                email VARCHAR(32),
                PRIMARY KEY (id)
            );
            """
            cursor.execute(create_table_query)
            print("Table created successfully")
        connection.commit()
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)
