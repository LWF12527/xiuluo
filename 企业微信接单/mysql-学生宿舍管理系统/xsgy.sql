CREATE DATABASE xsss;
use xsss;

CREATE TABLE dormitories (
    dorm_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '宿舍编号',
    floor INT NOT NULL COMMENT '楼层',
    room_type ENUM('单人间', '双人间', '多人间') NOT NULL COMMENT '房间类型',
    capacity INT NOT NULL COMMENT '可容纳人数',
    current_occupants INT DEFAULT 0 COMMENT '当前入住人数',
    furniture_info TEXT COMMENT '家具及设施配备',
    allocation_history TEXT COMMENT '分配历史记录'
);

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '学号',
    name VARCHAR(50) NOT NULL COMMENT '姓名',
    gender ENUM('男', '女') NOT NULL COMMENT '性别',
    major VARCHAR(100) COMMENT '专业',
    class VARCHAR(50) COMMENT '班级',
    contact VARCHAR(15) NOT NULL COMMENT '联系方式',
    dorm_id INT DEFAULT NULL COMMENT '宿舍编号',
    check_in_date DATE DEFAULT NULL COMMENT '入住时间',
    check_out_date DATE DEFAULT NULL COMMENT '退房时间',
    encrypted_contact TEXT COMMENT '加密的联系方式',
    FOREIGN KEY (dorm_id) REFERENCES dormitories(dorm_id)
);

CREATE TABLE facilities (
    facility_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '设备编号',
    dorm_id INT NOT NULL COMMENT '宿舍编号',
    name VARCHAR(100) NOT NULL COMMENT '设备名称',
    brand VARCHAR(50) COMMENT '品牌',
    model VARCHAR(50) COMMENT '型号',
    purchase_date DATE COMMENT '购置时间',
    status ENUM('正常', '损坏', '报废') DEFAULT '正常' COMMENT '状态',
    FOREIGN KEY (dorm_id) REFERENCES dormitories(dorm_id)
);

CREATE TABLE maintenance_requests (
    request_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '申请编号',
    facility_id INT NOT NULL COMMENT '设备编号',
    report_date DATE NOT NULL COMMENT '报修日期',
    description TEXT COMMENT '问题描述',
    status ENUM('待处理', '维修中', '已完成') DEFAULT '待处理' COMMENT '状态',
    repair_date DATE DEFAULT NULL COMMENT '完成日期',
    repair_cost DECIMAL(10, 2) DEFAULT NULL COMMENT '维修费用',
    repair_person VARCHAR(50) DEFAULT NULL COMMENT '维修人员',
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id)
);

CREATE TABLE fee_settings (
    fee_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '费用编号',
    fee_type ENUM('住宿费', '水电费', '物业费') NOT NULL COMMENT '费用类型',
    amount DECIMAL(10, 2) NOT NULL COMMENT '收费标准',
    billing_cycle ENUM('按月', '按学期', '按年') NOT NULL COMMENT '计费周期'
);

CREATE TABLE fee_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '记录编号',
    student_id INT NOT NULL COMMENT '学号',
    fee_id INT NOT NULL COMMENT '费用编号',
    payment_date DATE DEFAULT NULL COMMENT '缴费时间',
    amount DECIMAL(10, 2) NOT NULL COMMENT '缴费金额',
    payment_method ENUM('线上支付', '线下缴费') NOT NULL COMMENT '缴费方式',
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (fee_id) REFERENCES fee_settings(fee_id)
);

CREATE TABLE visitors (
    visitor_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '访客编号',
    name VARCHAR(50) NOT NULL COMMENT '姓名',
    id_card VARCHAR(18) NOT NULL COMMENT '身份证号',
    contact VARCHAR(15) NOT NULL COMMENT '联系方式',
    visit_target INT NOT NULL COMMENT '访问对象（学生编号）',
    visit_time DATETIME NOT NULL COMMENT '访问时间',
    access_level TEXT COMMENT '访问权限',
    duration INT COMMENT '访问时长（分钟）',
    FOREIGN KEY (visit_target) REFERENCES students(student_id)
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户编号',
    username VARCHAR(50) NOT NULL COMMENT '用户名',
    password_hash TEXT NOT NULL COMMENT '密码（哈希值存储）',
    role ENUM('管理员', '宿管人员', '学生') NOT NULL COMMENT '角色',
    permissions TEXT COMMENT '权限列表'
);

CREATE TABLE logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '日志编号',
    user_id INT NOT NULL COMMENT '操作用户编号',
    action TEXT NOT NULL COMMENT '操作内容',
    action_time DATETIME NOT NULL COMMENT '操作时间',
    result ENUM('成功', '失败') NOT NULL COMMENT '操作结果',
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


INSERT INTO dormitories (floor, room_type, capacity, current_occupants, furniture_info, allocation_history)
VALUES
(1, '单人间', 1, 0, '床, 书桌, 衣柜', ''),
(1, '双人间', 2, 1, '床, 书桌, 衣柜', '张三'),
(2, '多人间', 4, 2, '床, 书桌, 衣柜', '张三, 李四'),
(3, '单人间', 1, 0, '床, 书桌, 衣柜', ''),
(3, '双人间', 2, 2, '床, 书桌, 衣柜', '王五, 赵六'),
(4, '多人间', 6, 4, '床, 书桌, 衣柜', '多人'),
(5, '单人间', 1, 1, '床, 书桌, 衣柜', '李七'),
(6, '双人间', 2, 0, '床, 书桌, 衣柜', ''),
(7, '多人间', 8, 6, '床, 书桌, 衣柜', '多人'),
(8, '单人间', 1, 0, '床, 书桌, 衣柜', ''),
(9, '双人间', 2, 1, '床, 书桌, 衣柜', '刘八'),
(10, '多人间', 4, 3, '床, 书桌, 衣柜', '多人'),
(11, '单人间', 1, 1, '床, 书桌, 衣柜', '陈九'),
(12, '双人间', 2, 2, '床, 书桌, 衣柜', '周十, 钱十一'),
(13, '多人间', 6, 4, '床, 书桌, 衣柜', '多人'),
(14, '单人间', 1, 0, '床, 书桌, 衣柜', ''),
(15, '双人间', 2, 1, '床, 书桌, 衣柜', '孙十二'),
(16, '多人间', 8, 6, '床, 书桌, 衣柜', '多人'),
(17, '单人间', 1, 0, '床, 书桌, 衣柜', ''),
(18, '双人间', 2, 2, '床, 书桌, 衣柜', '李十三, 王十四');

INSERT INTO students (name, gender, major, class, contact, dorm_id, check_in_date, check_out_date, encrypted_contact)
VALUES
('张三', '男', '计算机科学', '2023级1班', '12345678901', 1, '2023-09-01', NULL, 'encrypted_1'),
('李四', '女', '软件工程', '2023级2班', '12345678902', 2, '2023-09-02', NULL, 'encrypted_2'),
('王五', '男', '土木工程', '2023级3班', '12345678903', 3, '2023-09-03', NULL, 'encrypted_3'),
('赵六', '女', '机械工程', '2023级4班', '12345678904', 3, '2023-09-03', NULL, 'encrypted_4'),
('李七', '男', '金融学', '2023级5班', '12345678905', 5, '2023-09-04', NULL, 'encrypted_5'),
('刘八', '女', '法学', '2023级6班', '12345678906', 9, '2023-09-05', NULL, 'encrypted_6'),
('陈九', '男', '电子信息', '2023级7班', '12345678907', 11, '2023-09-06', NULL, 'encrypted_7'),
('周十', '女', '医学', '2023级8班', '12345678908', 12, '2023-09-07', NULL, 'encrypted_8'),
('钱十一', '男', '护理学', '2023级9班', '12345678909', 12, '2023-09-08', NULL, 'encrypted_9'),
('孙十二', '女', '会计学', '2023级10班', '12345678910', 15, '2023-09-09', NULL, 'encrypted_10'),
('李十三', '男', '教育学', '2023级11班', '12345678911', 18, '2023-09-10', NULL, 'encrypted_11'),
('王十四', '女', '心理学', '2023级12班', '12345678912', 18, '2023-09-11', NULL, 'encrypted_12'),
('王十五', '男', '化学', '2023级13班', '12345678913', NULL, NULL, NULL, 'encrypted_13'),
('张十六', '女', '物理学', '2023级14班', '12345678914', NULL, NULL, NULL, 'encrypted_14'),
('李十七', '男', '数学', '2023级15班', '12345678915', NULL, NULL, NULL, 'encrypted_15'),
('赵十八', '女', '哲学', '2023级16班', '12345678916', NULL, NULL, NULL, 'encrypted_16'),
('陈十九', '男', '历史学', '2023级17班', '12345678917', NULL, NULL, NULL, 'encrypted_17'),
('周二十', '女', '生物学', '2023级18班', '12345678918', NULL, NULL, NULL, 'encrypted_18'),
('孙二十一', '男', '地理学', '2023级19班', '12345678919', NULL, NULL, NULL, 'encrypted_19'),
('钱二十二', '女', '天文学', '2023级20班', '12345678920', NULL, NULL, NULL, 'encrypted_20');


INSERT INTO facilities (dorm_id, name, brand, model, purchase_date, status)
VALUES
(1, '空调', '格力', 'KFR-35GW', '2022-01-01', '正常'),
(2, '热水器', '美的', 'JSQ22-12HWB', '2022-02-01', '正常'),
(3, '洗衣机', '海尔', 'XQG70-1010', '2022-03-01', '正常'),
(4, '冰箱', '西门子', 'BCD-610W', '2022-04-01', '损坏'),
(5, '电风扇', '艾美特', 'FSW65T', '2022-05-01', '正常'),
(6, '微波炉', '松下', 'NN-DF383B', '2022-06-01', '正常'),
(7, '电视', '创维', '55G8S', '2022-07-01', '正常'),
(8, '吸尘器', '戴森', 'V10', '2022-08-01', '报废'),
(9, '路由器', '华为', 'AX3', '2022-09-01', '正常'),
(10, '打印机', '佳能', 'G3800', '2022-10-01', '正常'),
(1, '空调', '格力', 'KFR-35GW', '2022-01-01', '正常'),
(2, '热水器', '美的', 'JSQ22-12HWB', '2022-02-01', '正常'),
(3, '洗衣机', '海尔', 'XQG70-1010', '2022-03-01', '正常'),
(4, '冰箱', '西门子', 'BCD-610W', '2022-04-01', '损坏'),
(5, '电风扇', '艾美特', 'FSW65T', '2022-05-01', '正常'),
(6, '微波炉', '松下', 'NN-DF383B', '2022-06-01', '正常'),
(7, '电视', '创维', '55G8S', '2022-07-01', '正常'),
(8, '吸尘器', '戴森', 'V10', '2022-08-01', '报废'),
(9, '路由器', '华为', 'AX3', '2022-09-01', '正常'),
(10, '打印机', '佳能', 'G3800', '2022-10-01', '正常'),


INSERT INTO students (name, gender, major, class, contact, dorm_id, check_in_date, check_out_date, encrypted_contact)
VALUES
('张三', '男', '计算机科学', '2023级1班', '12345678901', 1, '2023-09-01', NULL, 'encrypted_1'),
('李四', '女', '软件工程', '2023级2班', '12345678902', 2, '2023-09-02', NULL, 'encrypted_2'),
('王五', '男', '土木工程', '2023级3班', '12345678903', 3, '2023-09-03', NULL, 'encrypted_3'),
('赵六', '女', '机械工程', '2023级4班', '12345678904', 3, '2023-09-03', NULL, 'encrypted_4'),
('李七', '男', '金融学', '2023级5班', '12345678905', 5, '2023-09-04', NULL, 'encrypted_5'),
('刘八', '女', '法学', '2023级6班', '12345678906', 9, '2023-09-05', NULL, 'encrypted_6'),
('陈九', '男', '电子信息', '2023级7班', '12345678907', 11, '2023-09-06', NULL, 'encrypted_7'),
('周十', '女', '医学', '2023级8班', '12345678908', 12, '2023-09-07', NULL, 'encrypted_8'),
('钱十一', '男', '护理学', '2023级9班', '12345678909', 12, '2023-09-08', NULL, 'encrypted_9'),
('孙十二', '女', '会计学', '2023级10班', '12345678910', 15, '2023-09-09', NULL, 'encrypted_10'),
('李十三', '男', '教育学', '2023级11班', '12345678911', 18, '2023-09-10', NULL, 'encrypted_11'),
('王十四', '女', '心理学', '2023级12班', '12345678912', 18, '2023-09-11', NULL, 'encrypted_12'),
('王十五', '男', '化学', '2023级13班', '12345678913', NULL, NULL, NULL, 'encrypted_13'),
('张十六', '女', '物理学', '2023级14班', '12345678914', NULL, NULL, NULL, 'encrypted_14'),
('李十七', '男', '数学', '2023级15班', '12345678915', NULL, NULL, NULL, 'encrypted_15'),
('赵十八', '女', '哲学', '2023级16班', '12345678916', NULL, NULL, NULL, 'encrypted_16'),
('陈十九', '男', '历史学', '2023级17班', '12345678917', NULL, NULL, NULL, 'encrypted_17'),
('周二十', '女', '生物学', '2023级18班', '12345678918', NULL, NULL, NULL, 'encrypted_18'),
('孙二十一', '男', '地理学', '2023级19班', '12345678919', NULL, NULL, NULL, 'encrypted_19'),
('钱二十二', '女', '天文学', '2023级20班', '12345678920', NULL, NULL, NULL, 'encrypted_20');



INSERT INTO maintenance_requests (facility_id, report_date, description, status, repair_date, repair_cost, repair_person) 
VALUES 
(1, '2023-10-01', '空调不制冷', '待处理', NULL, NULL, NULL),
(2, '2023-10-02', '洗衣机漏水', '维修中', NULL, NULL, '李师傅'),
(3, '2023-10-03', '热水器无法加热', '已完成', '2023-10-05', 150.00, '张师傅'),
(4, '2023-10-04', '冰箱噪音大', '维修中', NULL, NULL, '王师傅'),
(4, '2023-10-04', '冰箱噪音大', '维修中', NULL, NULL, '王师傅'),
(1, '2023-10-01', '空调不制冷', '待处理', NULL, NULL, NULL),
(2, '2023-10-02', '洗衣机漏水', '维修中', NULL, NULL, '李师傅'),
(3, '2023-10-03', '热水器无法加热', '已完成', '2023-10-05', 150.00, '张师傅'),
(1, '2023-10-01', '空调不制冷', '待处理', NULL, NULL, NULL),
(2, '2023-10-02', '洗衣机漏水', '维修中', NULL, NULL, '李师傅'),
(3, '2023-10-03', '热水器无法加热', '已完成', '2023-10-05', 150.00, '张师傅'),
(4, '2023-10-04', '冰箱噪音大', '维修中', NULL, NULL, '王师傅'),
(1, '2023-10-01', '空调不制冷', '待处理', NULL, NULL, NULL),
(2, '2023-10-02', '洗衣机漏水', '维修中', NULL, NULL, '李师傅'),
(3, '2023-10-03', '热水器无法加热', '已完成', '2023-10-05', 150.00, '张师傅'),
(4, '2023-10-04', '冰箱噪音大', '维修中', NULL, NULL, '王师傅'),
(1, '2023-10-01', '空调不制冷', '待处理', NULL, NULL, NULL),
(2, '2023-10-02', '洗衣机漏水', '维修中', NULL, NULL, '李师傅'),
(3, '2023-10-03', '热水器无法加热', '已完成', '2023-10-05', 150.00, '张师傅'),
(4, '2023-10-04', '冰箱噪音大', '维修中', NULL, NULL, '王师傅'),
(5, '2023-10-05', '电风扇无法启动', '已完成', '2023-10-06', 50.00, '刘师傅');


INSERT INTO fee_settings (fee_type, amount, billing_cycle) 
VALUES 
('住宿费', 1200.00, '按学期'),
('水电费', 50.00, '按月'),
('物业费', 30.00, '按月'),
('住宿费', 1200.00, '按学期'),
('水电费', 50.00, '按月'),
('物业费', 30.00, '按月'),
('住宿费', 2400.00, '按年'),
('住宿费', 1200.00, '按学期'),
('水电费', 50.00, '按月'),
('物业费', 30.00, '按月'),
('住宿费', 2400.00, '按年'),
('住宿费', 1200.00, '按学期'),
('水电费', 50.00, '按月'),
('物业费', 30.00, '按月'),
('住宿费', 2400.00, '按年'),
('住宿费', 1200.00, '按学期'),
('水电费', 50.00, '按月'),
('物业费', 30.00, '按月'),
('住宿费', 2400.00, '按年'),
('住宿费', 2400.00, '按年'),
('水电费', 100.00, '按学期');

INSERT INTO fee_records (student_id, fee_id, payment_date, amount, payment_method) 
VALUES 
(1, 1, '2023-09-01', 1200.00, '线上支付'),
(2, 2, '2023-09-02', 50.00, '线下缴费'),
(3, 3, '2023-09-03', 30.00, '线上支付'),
(4, 1, '2023-09-04', 1200.00, '线下缴费'),
(1, 1, '2023-09-01', 1200.00, '线上支付'),
(2, 2, '2023-09-02', 50.00, '线下缴费'),
(3, 3, '2023-09-03', 30.00, '线上支付'),
(4, 1, '2023-09-04', 1200.00, '线下缴费'),
(1, 1, '2023-09-01', 1200.00, '线上支付'),
(2, 2, '2023-09-02', 50.00, '线下缴费'),
(3, 3, '2023-09-03', 30.00, '线上支付'),
(4, 1, '2023-09-04', 1200.00, '线下缴费'),
(1, 1, '2023-09-01', 1200.00, '线上支付'),
(2, 2, '2023-09-02', 50.00, '线下缴费'),
(3, 3, '2023-09-03', 30.00, '线上支付'),
(4, 1, '2023-09-04', 1200.00, '线下缴费'),
(1, 1, '2023-09-01', 1200.00, '线上支付'),
(2, 2, '2023-09-02', 50.00, '线下缴费'),
(3, 3, '2023-09-03', 30.00, '线上支付'),
(4, 1, '2023-09-04', 1200.00, '线下缴费'),
(5, 4, NULL, 2400.00, '线上支付');


INSERT INTO visitors (name, id_card, contact, visit_target, visit_time, access_level, duration) 
VALUES 
('李明', '110101199001011234', '13812345678', 1, '2023-10-10 10:00:00', '宿舍楼1', 60),
('王芳', '120202198902021234', '13987654321', 2, '2023-10-11 14:00:00', '宿舍楼2', 120),
('张强', '130303197003031234', '13765432109', 3, '2023-10-12 09:00:00', '宿舍楼3', 30),
('赵云', '140404196004041234', '13876543210', 4, '2023-10-13 15:00:00', '宿舍楼4', 90),
('李明', '110101199001011234', '13812345678', 1, '2023-10-10 10:00:00', '宿舍楼1', 60),
('王芳', '120202198902021234', '13987654321', 2, '2023-10-11 14:00:00', '宿舍楼2', 120),
('张强', '130303197003031234', '13765432109', 3, '2023-10-12 09:00:00', '宿舍楼3', 30),
('赵云', '140404196004041234', '13876543210', 4, '2023-10-13 15:00:00', '宿舍楼4', 90),
('李明', '110101199001011234', '13812345678', 1, '2023-10-10 10:00:00', '宿舍楼1', 60),
('王芳', '120202198902021234', '13987654321', 2, '2023-10-11 14:00:00', '宿舍楼2', 120),
('张强', '130303197003031234', '13765432109', 3, '2023-10-12 09:00:00', '宿舍楼3', 30),
('赵云', '140404196004041234', '13876543210', 4, '2023-10-13 15:00:00', '宿舍楼4', 90),
('李明', '110101199001011234', '13812345678', 1, '2023-10-10 10:00:00', '宿舍楼1', 60),
('王芳', '120202198902021234', '13987654321', 2, '2023-10-11 14:00:00', '宿舍楼2', 120),
('张强', '130303197003031234', '13765432109', 3, '2023-10-12 09:00:00', '宿舍楼3', 30),
('赵云', '140404196004041234', '13876543210', 4, '2023-10-13 15:00:00', '宿舍楼4', 90),
('李明', '110101199001011234', '13812345678', 1, '2023-10-10 10:00:00', '宿舍楼1', 60),
('王芳', '120202198902021234', '13987654321', 2, '2023-10-11 14:00:00', '宿舍楼2', 120),
('张强', '130303197003031234', '13765432109', 3, '2023-10-12 09:00:00', '宿舍楼3', 30),
('赵云', '140404196004041234', '13876543210', 4, '2023-10-13 15:00:00', '宿舍楼4', 90),
('钱坤', '150505199505051234', '13654321098', 5, '2023-10-14 13:00:00', '宿舍楼5', 45);

INSERT INTO users (username, password_hash, role, permissions) 
VALUES 
('admin', 'HASH12345', '管理员', '全权限'),
('dorm_manager1', 'HASH67890', '宿管人员', '管理宿舍1'),
('dorm_manager2', 'HASH11111', '宿管人员', '管理宿舍2'),
('student1', 'HASH22222', '学生', '查看个人信息'),
('student2', 'HASH33333', '学生', '查看个人信息');

INSERT INTO logs (user_id, action, action_time, result) 
VALUES 
(1, '创建学生数据', '2023-10-15 10:00:00', '成功'),
(2, '修改宿舍分配', '2023-10-16 11:00:00', '成功'),
(3, '记录访客信息', '2023-10-17 12:00:00', '成功'),
(4, '查看费用记录', '2023-10-18 13:00:00', '成功'),
(5, '维修申报', '2023-10-19 14:00:00', '失败');
