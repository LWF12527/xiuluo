# 输出有误，v7应该在v8课程修习之前

#coding=utf8
import prettytable as pt

total_semester = int(input("请输入学期总数："))
credit_limit = int(input("请输入每学期学分上限："))
courses = {
    "V1": {"name": "计算机导论", "credit": 2, "prerequisites": []},
    "V2": {"name": "高等数学", "credit": 4, "prerequisites": []},
    "V3": {"name": "程序设计", "credit": 4, "prerequisites": ["V1", "V2"]},
    "V4": {"name": "离散数学", "credit": 2, "prerequisites": ["V2", "V3"]},
    "V5": {"name": "数据结构", "credit": 6, "prerequisites": ["V3", "V4"]},
    "V6": {"name": "编译原理", "credit": 4, "prerequisites": ["V4", "V5"]},
    "V7": {"name": "数字逻辑", "credit": 4, "prerequisites": ["V2", "V4"]},
    "V8": {"name": "组成原理", "credit": 6, "prerequisites": ["V7"]},
    "V9": {"name": "操作系统", "credit": 6, "prerequisites": ["V5", "V6", "V8"]}
}

# 处理先修课程
for course_id, course_info in courses.items():
    prerequisites = course_info["prerequisites"]
    if len(prerequisites) == 0:
        continue
    for prerequisite_id in prerequisites:
        if prerequisite_id not in courses:
            raise ValueError(f"课程{course_id}的先修课程{prerequisite_id}不存在")
        courses[prerequisite_id]["next_courses"] = courses[prerequisite_id].get("next_courses", [])
        courses[prerequisite_id]["next_courses"].append(course_id)

# 均匀策略
uniform_semester_courses = [[] for _ in range(total_semester)]
sorted_courses = sorted(courses.items(), key=lambda x: len(x[1]["prerequisites"]), reverse=False)
for course_id, course_info in sorted_courses:
    added_course = False
    for semester in uniform_semester_courses:
        if sum([courses[c]["credit"] for c in semester]) + course_info["credit"] <= credit_limit:
            semester.append(course_id)
            added_course = True
            break
    if not added_course:
        continue


# 集中策略
concentrated_semester_courses = [[] for _ in range(total_semester)]
for course_id, course_info in courses.items():
    if "next_courses" not in course_info:
        # 没有先修课程
        for i in range(total_semester):
            if sum([courses[c]["credit"] for c in concentrated_semester_courses[i]]) + course_info["credit"] <= credit_limit:
                concentrated_semester_courses[i].append(course_id)
                break
    else:
        # 有先修课程
        min_semester = 0
        for prerequisite_id in course_info["prerequisites"]:
            prerequisite_semester = next(i for i in range(total_semester) if prerequisite_id in concentrated_semester_courses[i])
            min_semester = max(min_semester, prerequisite_semester)
        for i in range(min_semester, total_semester):
            if sum([courses[c]["credit"] for c in concentrated_semester_courses[i]]) + course_info["credit"] <= credit_limit:
                concentrated_semester_courses[i].append(course_id)
                break

# 输出教学计划
table = pt.PrettyTable()
table.field_names = ["学期", "均匀策略", "集中策略"]

for i in range(total_semester):
    uniform_courses = ""
    for course_id in sorted_courses:
        if course_id[0] in uniform_semester_courses[i]:
            course_info = courses[course_id[0]]
            uniform_courses += f"{course_id[0]} {course_info['name']} {course_info['credit']}学分\n"
    concentrated_courses = ""
    for course_id in sorted_courses:
        if course_id[0] in concentrated_semester_courses[i]:
            course_info = courses[course_id[0]]
            concentrated_courses += f"{course_id[0]} {course_info['name']} {course_info['credit']}学分\n"
    table.add_row([f"第{i+1}学期", uniform_courses, concentrated_courses])

print(table)

