-- creates user if not existS
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- all privileges to the user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
