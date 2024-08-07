# [How to] Create Table
## Log in to your MySQL server as a user with sufficient privileges, such as the root user.
```
sudo mysql -uroot -p
```

## Create the tyrell_corp database:
```
CREATE DATABASE tyrell_corp;
```
## Switch to the tyrell_corp database:
```
USE tyrell_corp;
```
## Create the nexus6 table with appropriate columns and add at least one entry. Here's an example schema with two columns, id and name:
```
CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO nexus6 (name) VALUES ('Leon');
```
## Grant SELECT permissions on the nexus6 table to the holberton_user:
```
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
```

## Check if it is created successfully
```
$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
```

## Exit the MySQL server.
```
$ exit
```


