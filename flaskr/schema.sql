/*
# Rylee Leavitt
# 4/28/25
# SDEV1100 1st project
# SDEV 1100
#

#db.py
#Flask tutorial

#Create the Tables:
#In SQLite, data is stored in tables and columns. These need to be created before you can store and retrieve data. 
Flaskr will store users in the user table, and posts in the post table. 
Create a file with the SQL commands needed to create empty tables:
 */

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);