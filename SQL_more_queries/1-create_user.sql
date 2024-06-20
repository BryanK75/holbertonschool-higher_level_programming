-- deletes the user if it already exists
DROP USER IF EXISTS 'user_01_1'@'localhost';

-- script that creates the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- script that grant all privileges to user user_01_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- flush privileges to apply the changes
FLUSH PRIVILEGES
