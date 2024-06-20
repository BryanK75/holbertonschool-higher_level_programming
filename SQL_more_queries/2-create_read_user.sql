-- Creates a database names hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates a user user_0d_2 with a password user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant selected privileges to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
