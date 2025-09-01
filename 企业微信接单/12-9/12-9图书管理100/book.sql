-- 创建数据库book_system
CREATE DATABASE IF NOT EXISTS book_system;
USE book_system;
 
-- 创建用户信息表 (User)
CREATE TABLE User (
  UserID INT NOT NULL PRIMARY KEY,
  Name VARCHAR(255) NOT NULL,
  Gender VARCHAR(10),
  Age INT,
  ContactNumber VARCHAR(20),
  Address VARCHAR(255)
);

-- 创建图书信息表 (Book)
CREATE TABLE Book (
  BookID INT NOT NULL PRIMARY KEY,
  BookName VARCHAR(255) NOT NULL,
  Author VARCHAR(255),
  Publisher VARCHAR(255),
  PublicationDate DATE,
  Category VARCHAR(255)
);

-- 创建借阅信息表 (Borrow)
CREATE TABLE Borrow (
  BorrowID INT NOT NULL PRIMARY KEY,
  UserID INT NOT NULL,
  BookID INT NOT NULL,
  BorrowDate DATE NOT NULL,
  ReturnDate DATE,
  FOREIGN KEY (UserID) REFERENCES User(UserID),
  FOREIGN KEY (BookID) REFERENCES Book(BookID)
);
 
-- 插入数据
INSERT INTO User (UserID, Name, Gender, Age, ContactNumber, Address)
VALUES
  (1, 'Alice', 'Female', 25, '1234567890', '123 Main St'),
  (2, 'Bob', 'Male', 30, '9876543210', '456 Elm St'),
  (3, 'Charlie', 'Male', 35, '5678901234', '789 Oak St');

INSERT INTO Book (BookID, BookName, Author, Publisher, PublicationDate, Category)
VALUES
  (1, 'Book A', 'Author A', 'Publisher A', '2021-01-01', 'Category 1'),
  (2, 'Book B', 'Author B', 'Publisher B', '2022-02-02', 'Category 2'),
  (3, 'Book C', 'Author C', 'Publisher C', '2023-03-03', 'Category 3');

INSERT INTO Borrow (BorrowID, UserID, BookID, BorrowDate, ReturnDate)
VALUES
  (1, 1, 1, '2022-01-01', '2022-01-10'),
  (2, 2, 2, '2022-02-02', '2022-02-12'),
  (3, 3, 3, '2022-03-03', NULL);

 
-- 在用户信息表的UserID字段上创建索引：
CREATE INDEX idx_User_UserID ON User(UserID);
 
-- 在图书信息表的BookName字段上创建索引：
CREATE INDEX idx_Book_BookName ON Book(BookName);
 
-- 创建一个视图，显示已归还的借阅记录：
CREATE VIEW ReturnedBorrow AS
SELECT * FROM Borrow WHERE ReturnDate IS NOT NULL;

-- 创建一个视图，显示每位用户借阅的图书数量：
CREATE VIEW UserBorrowCount AS
SELECT UserID, COUNT(*) AS BorrowCount
FROM Borrow
GROUP BY UserID;

-- 创建一个视图，显示每种图书类别的平均借阅时长：
CREATE VIEW CategoryAvgDuration AS
SELECT Category, AVG(DATEDIFF(ReturnDate, BorrowDate)) AS AvgDuration
FROM Borrow
JOIN Book ON Borrow.BookID = Book.BookID
WHERE ReturnDate IS NOT NULL
GROUP BY Category;
 
-- 创建创建一个触发器，在插入新的借阅记录时更新图书信息表中的借阅数量：
CREATE TRIGGER UpdateBorrowCount
AFTER INSERT ON Borrow
FOR EACH ROW
BEGIN
  UPDATE Book SET BorrowCount = BorrowCount + 1 WHERE BookID = NEW.BookID;
END;

-- 创建一个触发器，在删除借阅记录时更新图书信息表中的借阅数量：
CREATE TRIGGER UpdateBorrowCount
AFTER DELETE ON Borrow
FOR EACH ROW
BEGIN
  UPDATE Book SET BorrowCount = BorrowCount - 1 WHERE BookID = OLD.BookID;
END;	

-- 创建一个触发器，在修改借阅记录的归还日期时更新图书信息表中的借阅数量：
CREATE TRIGGER UpdateBorrowCount
AFTER UPDATE OF ReturnDate ON Borrow
FOR EACH ROW
BEGIN
  IF NEW.ReturnDate IS NULL THEN
    UPDATE Book SET BorrowCount = BorrowCount - 1 WHERE BookID = NEW.BookID;
  ELSE
    UPDATE Book SET BorrowCount = BorrowCount + 1 WHERE BookID = NEW.BookID;
  END IF;
END;	
 
-- 创建一个存储过程，根据用户ID查询该用户的借阅记录：
CREATE PROCEDURE GetUserBorrowHistory(IN userID INT)
BEGIN
  SELECT * FROM Borrow WHERE UserID = userID;
END;

-- 创建一个存储过程，插入新的图书信息：
CREATE PROCEDURE InsertBook(IN bookName VARCHAR(255), IN author VARCHAR(255), IN publisher VARCHAR(255))
BEGIN
  INSERT INTO Book (BookName, Author, Publisher) VALUES (bookName, author, publisher);
END;
 
-- 查询所有用户的姓名和年龄：
SELECT Name, Age FROM User;
-- 查询借阅信息表中借阅日期在特定日期范围内的记录：
SELECT * FROM Borrow WHERE BorrowDate BETWEEN '2023-01-01' AND '2023-12-31';
 
-- 使用嵌套查询，查询借阅信息表中已归还的借阅记录的图书名称：
SELECT BookName FROM Book WHERE BookID IN (SELECT BookID FROM ReturnedBorrow);

-- 使用子查询，查询借阅信息表中借阅次数最多的图书名称：
SELECT BookName FROM Book WHERE BookID = (SELECT BookID FROM Borrow GROUP BY BookID ORDER BY COUNT(*) DESC LIMIT 1);
 
-- 每位用户借阅的图书数量和姓名：
SELECT User.Name, UserBorrowCount.BorrowCount
FROM User
JOIN UserBorrowCount ON User.UserID = UserBorrowCount.UserID;
 
-- 查询每种图书类别的平均借阅时长和类别名称：
SELECT Category, AvgDuration FROM CategoryAvgDuration;
 
-- 更新用户信息表中ID为1的用户的联系电话：
UPDATE User SET ContactNumber = '1234567890' WHERE UserID = 1;
 
-- 更新图书信息表中ID为1的图书的作者：
UPDATE Book SET Author = 'New Author' WHERE BookID = 1;
 
-- 将借阅信息表中归还日期为空的记录的归还日期设置为当前日期：
UPDATE Borrow SET ReturnDate = CURDATE() WHERE ReturnDate IS NULL;
 
-- 删除借阅信息表中借阅日期早于2022年1月1日的记录：
DELETE FROM Borrow WHERE BorrowDate < '2022-01-01';
 
