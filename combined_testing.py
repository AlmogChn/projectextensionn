import pymysql

db = pymysql.connect(host='remotemysql.com', port=3306, user='AEfWGNA9zC', password='g0PRYTjC6R', db='AEfWGNA9zC')
cur = db.cursor()
db.autocommit(True)


class Msql:                 # this class is for "users" table
    def __init__(self, user_id=[], user_name=[], table=[]):
        self.user_id = user_id
        self.user_name = user_name
        self.table = table

    def insert_into(self):
        return \
            cur.execute(
                f"insert into AEfWGNA9zC.{self.table} (user_id, user_name, creation_date) VALUES ('{self.user_id}', '{self.user_name}', sysdate() )")

    # This function was written to insert a new row into the table

    def select_name(self):
        cur.execute(f"select * from AEfWGNA9zC.{self.table} where user_id ='{self.user_id}'")
        row = cur.fetchone()
        return row[1]

    # This function was written to select one row for table

    def select_all(self):
        cur.execute(f"select * from AEfWGNA9zC.{self.table}")
        return cur.fetchall()

    # This function was written to select all rows in a table

    def del_from_id(self):
        return \
            cur.execute(f"delete from AEfWGNA9zC.{self.table} where user_id = {self.user_id}")

    # This function was written to delete row by id

    def update_name_from_id(self):
        return \
            cur.execute(
                f"update AEfWGNA9zC.{self.table} set user_name = '{self.user_name}', creation_date= sysdate() where user_id = {self.user_id}")

    # This function was written to update name in a row

    def check_id(self):
        cur.execute(f"select * from AEfWGNA9zC.{self.table}")
        rows = cur.fetchall()
        check_id = int(self.user_id)
        for row in rows:
            if row[0] == int(check_id):
                return True

    # This function was written to check if there is already such a user id that exists in the table
