-- Script that creates the table force_name on your MySQL server
-- force_name description:
--- id INT
-- name VARCHAR(256) can’t be nul
CREATE TABLE IF NOT EXISTS `force_name` (
    `id`   INT,
    `name` VARCHAR(256) NOT NULL
);
