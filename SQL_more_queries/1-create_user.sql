-- creates user if not exist
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost' IDENTIFIED WITH 'user_0d_1_pwd';
GRANT ALL PRIVILIGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
