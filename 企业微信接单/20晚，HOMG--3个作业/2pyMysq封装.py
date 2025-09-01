import pymysql

class pyMySql:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def execute_update(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.rowcount

    def execute_insert(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.lastrowid

if __name__ == "__main__":
    # 配置数据库连接信息
    host = "localhost"
    user = "root"
    password = "123456"
    database = "stu"

    # 创建pyMySql实例
    db = pyMySql(host, user, password, database)

    # 连接数据库
    db.connect()

    # 插入数据
    insert_query = 'insert into students(name, gender, score, age) values("aaa","男",25, 18)'
    inserted_id = db.execute_insert(insert_query)
    print(f"Inserted ID: {inserted_id}")

    # 查询数据
    select_query = "SELECT * FROM students"
    result = db.execute_query(select_query)
    print("Query Result:")
    for row in result:
        print(row)

    # 更新数据
    update_query = "UPDATE students SET gender = '女' WHERE id = 1"
    updated_rows = db.execute_update(update_query)
    print(f"Updated Rows: {updated_rows}")

    # 删除数据
    delete_query = "DELETE FROM students WHERE id = 3"
    deleted_rows = db.execute_update(delete_query)
    print(f"Deleted Rows: {deleted_rows}")

    # 断开数据库连接
    db.disconnect()
