-- script converts hbtn_0c_0 database to 'UTF8'
-- convetred are hbtn_0c_0,
-- first_table,
-- Field name in first_table
USE hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
