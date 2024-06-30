-- creates user if not existS
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
