# [How to] Set up MySQL User
## create the setup file
```
$ cat setup_mysql_dev.sql 
-- script to create MySQL user on web servers

-- create user if not exist
-- user should should be identified with password projectcorrection280hbtn
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- grant holberton_user permission to check primary/replica status
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
```
## Prepare the bash script to transfer the setup file to the server 
File: [1-transfer_file](./1-transfer_file)
## transfer the setup file to the server
```
./1-transfer_file setup_mysql_dev.sql 52.207.208.230 ubuntu ~/.ssh/school
```

## Execute the setup file on the individual servers as such:
```
cat setup_mysql_dev.sql | sudo mysql
```