import re

import pandas as pd
import pymysql

# new_list = []
# data = pd.read_excel("question.xlsx", sheet_name="Sheet1")
#
# # 处理题目
# question_list = data["题目"].to_list()
#
# # 选择题
# question_xz = '''<QuestionContent>
#   <title>{}</title>
#   <titleImg></titleImg>
#   <choiceList>
#     <entry>
#       <string>A</string>
#       <string>{}</string>
#     </entry>
#     <entry>
#       <string>B</string>
#       <string>{}</string>
#     </entry>
#     <entry>
#       <string>C</string>
#       <string>{}</string>
#     </entry>
#     <entry>
#       <string>D</string>
#       <string>{}</string>
#     </entry>
#   </choiceList>
#   <choiceImgList/>
# </QuestionContent>'''
#
# # 判断题和单选框
# question_pd = '''<QuestionContent>
#   <title>{}</title>
#   <titleImg></titleImg>
#   <choiceList/>
#   <choiceImgList/>
# </QuestionContent>'''
#
# # 简答题和文本框
# question_jd = '''<QuestionContent>
#   <title>{}</title>
#   <titleImg></titleImg>
# </QuestionContent>'''
#
# xz_A_list = data["选项A"].to_list()
# xz_B_list = data["选项B"].to_list()
# xz_C_list = data["选项C"].to_list()
# xz_D_list = data["选项D"].to_list()
# for i in range(0, 32):
#     new_list.append(question_pd.format(question_list[i]))
# for i in range(32, 96):
#     new_list.append(question_xz.format(question_list[i], re.split(r'[. ]', xz_A_list[i])[-1],  re.split(r'[. ]', xz_B_list[i])[-1],  re.split(r'[. ]', xz_C_list[i])[-1],  re.split(r'[. ]', xz_D_list[i])[-1]))
# for i in range(96, 128):
#     new_list.append(question_jd.format(question_list[i]))
# question_list = new_list
# new_list = []
# # print(question_list)
# # 处理答案
# answer_list = data["答案"].to_list()
# for i in answer_list:
#     if i == "正确":
#         i = 'T'
#     elif i == "错误":
#         i = 'F'
#     new_list.append(i)
# answer_list = new_list
# new_list = []
# # print(answer_list)
#
# # 处理类型
# question_type_list = data["类型"].to_list()
# for i in question_type_list:
#     if i == '简答题':
#         i = 5
#     elif i == '判断题':
#         i = 3
#     elif i == '选择题':
#         i = 1
#     elif i == '多选题':
#         i = 2
#     new_list.append(i)
# question_type_list = new_list
# new_list = []
# # print(question_type_list)
#
# name_list = []
# for i in data["题目"].to_list():
#     name_list.append(i[0:10] + '···')
# # print(name_list)
#
# points_list = data["分值"].to_list()
# # print(points_list)
#

# 数据库插入
pymysql1 = pymysql.connect(host='localhost', user='root', password='123456', database='examxx', port=3306,autocommit =True)
cursor1 = pymysql1.cursor()  # 游标执行sql指令
query = "insert into et_question (name, content,question_type_id,points,answer) values ({},{},{},{},{})"
# for i in range(0, len(question_list)):
#     name = name_list[i]
#     content = question_list[i]
#     question_type = question_type_list[i]
#     points = points_list[i]
#     answer = answer_list[i]
#     sql1 = "insert into et_question (name, content,question_type_id,points,answer) values (%s,%s,%s,%s,%s)"
#
#     values = (name, content, int(question_type), int(points), answer)
#     cursor1.execute(sql1, values)

# 插入et_question_2_point3
for i in range(120,128):
    sql1 = "insert into et_question_2_point (question_id, point_id) values (%s,%s)"
    values = (i+1, 4)
    cursor1.execute(sql1, values)

cursor1.close()
pymysql1.commit()
pymysql1.close()
