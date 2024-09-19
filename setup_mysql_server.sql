-- prepare a mysql server for the study mate project
CREATE DATABASE IF NOT EXISTS study_mate_db;
CREATE USER IF NOT EXISTS 'study_mate_dev'@'localhost' IDENTIFIED BY 'Kim&go$3';
GRANT ALL PRIVILEGES ON `study_mate_db`.* TO 'study_mate_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'study_mate_dev'@'localhost';
FLUSH PRIVILEGES;
