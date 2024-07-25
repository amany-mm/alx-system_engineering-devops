# How To Set Up Replication in MySQL
https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql

## Step 3 - Grant permissions

Master server
```
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'replica_server_ip';

e.g.
CREATE USER 'replica_user'@'18.204.11.104' IDENTIFIED WITH mysql_native_password BY 'projectcorrection280hbtn';
```
```
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'replica_server_ip';
e.g.
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'18.204.11.104';
```
