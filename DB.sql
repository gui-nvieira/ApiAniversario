CREATE DATABASE aniversario
CHARACTER SET utf8mb4 
COLLATE utf8mb4_general_ci;

USE aniversario;

CREATE TABLE `users` (
user_id INT NOT NULL auto_increment,
`name` VARCHAR(20) NOT NULL,
`email` VARCHAR(50) NOT NULL,
`confirm` BOOLEAN DEFAULT 0,
`role` ENUM ('user', 'admin') DEFAULT 'user',
`signup_date` DATETIME DEFAULT NOW(),
`last_updated` DATETIME DEFAULT NOW(),
PRIMARY KEY (user_id)
)DEFAULT charset = utf8mb4;

INSERT INTO users
(`name`,`email`, `confirm`, `role`)
VALUES
('Chester','lelel@gmail.com', 1, 'admin');
