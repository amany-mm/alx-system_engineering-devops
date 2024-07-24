## Transfer the 3-create-replica_user.sql file to the server 
```
./1-transfer_file 3-create-replica_user.sql 52.207.208.230 ubuntu ~/.ssh/school
```

## Execute the create replica user file on the individual servers as such:
```
cat 3-create-replica_user.sql | sudo mysql
```

## Check if replica user created
```
mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'

```