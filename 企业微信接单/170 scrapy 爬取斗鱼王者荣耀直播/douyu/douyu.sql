drop database if exists douyu;
CREATE DATABASE IF NOT EXISTS douyu;
USE douyu;



CREATE TABLE IF NOT EXISTS douyu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255),
    gkrs INT,
    user_id VARCHAR(255),
    title VARCHAR(255),
    user_tx VARCHAR(255)
);


