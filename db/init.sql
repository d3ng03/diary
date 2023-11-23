-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS diary
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE diary;

-- Create the "content" table
CREATE TABLE IF NOT EXISTS content (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contents TEXT NOT NULL,
    date DATE NOT NULL
);

-- Insert some sample data into the "content" table
INSERT INTO content (contents, date) VALUES
    ("Today is a good day", CURDATE()),
    ("I'm so sad today", CURDATE());
