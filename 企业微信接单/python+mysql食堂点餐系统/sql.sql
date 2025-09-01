CREATE DATABASE if not exists food_court;
USE food_court;
CREATE TABLE user (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      username VARCHAR(255) NOT NULL UNIQUE,
                      password VARCHAR(255) NOT NULL,
                      role VARCHAR(255) NOT NULL,
                      balance FLOAT DEFAULT 0
);
CREATE TABLE menu (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      name VARCHAR(255) NOT NULL UNIQUE,
                      quantity INT DEFAULT 0,
                      cost FLOAT DEFAULT 0,
                      price FLOAT DEFAULT 0,
                      rating INT DEFAULT 0
);
INSERT INTO menu (name, quantity, cost, price, rating) VALUES
                                                           ('∫Ï…’»‚', 100, 10, 15, 4),
                                                           ('”„œ„»‚Àø', 80, 12, 18, 5),
                                                           ('π¨±£º¶∂°', 90, 11, 16, 4),
                                                           ('«Â’Ùˆ‘”„', 70, 20, 28, 5),
                                                           ('Ã«¥◊¿Ôºπ', 110, 9, 13, 4),
                                                           ('À·¿±Õ¡∂πÀø', 120, 5, 8, 3),
                                                           ('À‚»ÿŒ˜¿ºª®', 100, 6, 10, 4),
                                                           ('∑¨«—≥¥µ∞', 80, 7, 12, 3);