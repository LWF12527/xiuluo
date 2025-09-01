# -*- coding: gbk -*-
import pyodbc

# ����SQL Server���ݿ�������Ϣ
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=localhost,1433;'  # ������д���SQL Serverʵ�������ƻ�IP
    r'DATABASE=gxjs;'  # ���ݿ�����
    r'UID=sa;'  # SQL Server�û���
    r'PWD=L.sa123456'  # SQL Server����
)

# ���ӵ����ݿ�
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
print(cursor)

def add_teacher(teacher_id, name, gender, birth_date, department):
    try:
        cursor.execute('''
        INSERT INTO Teacher (teacher_id, name, gender, birth_date, department)
        VALUES (?, ?, ?, ?, ?)
        ''', (teacher_id, name, gender, birth_date, department))
        conn.commit()
        print("��ʦ��Ϣ����ӣ�")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def delete_teacher(teacher_id):
    try:
        cursor.execute('''
        DELETE FROM Teacher WHERE teacher_id = ?
        ''', (teacher_id,))
        conn.commit()
        print("��ʦ��Ϣ��ɾ����")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def update_teacher(teacher_id, name=None, gender=None, birth_date=None, department=None):
    try:
        update_fields = []
        update_values = []

        if name:
            update_fields.append("name = ?")
            update_values.append(name)
        if gender:
            update_fields.append("gender = ?")
            update_values.append(gender)
        if birth_date:
            update_fields.append("birth_date = ?")
            update_values.append(birth_date)
        if department:
            update_fields.append("department = ?")
            update_values.append(department)

        if not update_fields:
            print("û��������Ҫ���¡�")
            return

        update_fields.append("teacher_id = ?")
        update_values.append(teacher_id)

        update_query = f"UPDATE Teacher SET {', '.join(update_fields)} WHERE teacher_id = ?"
        cursor.execute(update_query, tuple(update_values))
        conn.commit()
        print("��ʦ��Ϣ�Ѹ��£�")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()

def get_teacher(teacher_id=None):
    try:
        if teacher_id:
            cursor.execute('''
            SELECT * FROM Teacher WHERE teacher_id = ?
            ''', (teacher_id,))
        else:
            cursor.execute('''
            SELECT * FROM Teacher
            ''')

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"ID: {row[0]}, ����: {row[1]}, �Ա�: {row[2]}, ��������: {row[3]}, ����: {row[4]}")
        else:
            print("û���ҵ���ʦ��Ϣ��")
    except Exception as e:
        print(f"Error: {e}")
def get_teachers_for_course(course_name):
    try:
        cursor.execute('''
        SELECT T.* 
        FROM Teacher T
        INNER JOIN Course C ON T.teacher_id = C.teacher_id
        WHERE C.course_name = ?
        ''', (course_name,))

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"ID: {row[0]}, ����: {row[1]}, �Ա�: {row[2]}, ��������: {row[3]}, ����: {row[4]}")
        else:
            print(f"û���ҵ����� {course_name} �Ľ�ʦ��Ϣ��")
    except Exception as e:
        print(f"Error: {e}")
def get_grades_by_teacher(teacher_id):
    try:
        cursor.execute('''
        SELECT G.student_id, C.course_name, G.score 
        FROM Grade G
        INNER JOIN Course C ON G.course_id = C.course_id
        WHERE G.teacher_id = ?
        ''', (teacher_id,))

        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(f"ѧ��: {row[0]}, �γ�: {row[1]}, ����: {row[2]}")
        else:
            print(f"û���ҵ���ʦIDΪ{teacher_id}�ĳɼ���Ϣ��")
    except Exception as e:
        print(f"Error: {e}")


def main():
    while True:
        print("\n��У��ʦ��Ϣ����ϵͳ")
        print("1. ��ӽ�ʦ")
        print("2. ɾ����ʦ")
        print("3. ���½�ʦ��Ϣ")
        print("4. ��ѯ��ʦ��Ϣ")
        print("5. ��ѯ�ض��γ̵Ľ�ʦ��Ϣ")
        print("6. ��ѯ��ʦ�ĳɼ���Ϣ")
        print("7. �˳�")

        choice = input("������ѡ��: ")

        if choice == '1':
            teacher_id = int(input("�������ʦID: "))
            name = input("�������ʦ����: ")
            gender = input("�������Ա� (M/F): ")
            birth_date = input("������������� (YYYY-MM-DD): ")
            department = input("�����벿��: ")
            add_teacher(teacher_id, name, gender, birth_date, department)

        elif choice == '2':
            teacher_id = int(input("������Ҫɾ���Ľ�ʦID: "))
            delete_teacher(teacher_id)

        elif choice == '3':
            teacher_id = int(input("������Ҫ���µĽ�ʦID: "))
            print("���½�ʦ��Ϣ��������ֵ�����������ĳ����س�������")
            name = input("�µ�����: ")
            gender = input("�µ��Ա�: ")
            birth_date = input("�µĳ������� (YYYY-MM-DD): ")
            department = input("�µĲ���: ")
            update_teacher(teacher_id, name or None, gender or None, birth_date or None, department or None)

        elif choice == '4':
            teacher_id = input("�������ʦID��ѯ����ֱ�ӻس���ѯ���н�ʦ: ")
            if teacher_id:
                get_teacher(int(teacher_id))
            else:
                get_teacher()

        elif choice == '5':
            course_name = input("������γ�����: ")
            get_teachers_for_course(course_name)

        elif choice == '6':
            teacher_id = int(input("�������ʦID��ѯ�ɼ�: "))
            get_grades_by_teacher(teacher_id)

        elif choice == '7':
            print("�˳�����")
            break
        else:
            print("��Чѡ����������롣")


if __name__ == '__main__':
    main()
