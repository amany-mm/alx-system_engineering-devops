# Shell Basics

### All your scripts must be executable. To make your file executable, use the chmod command:
```bash
chmod u+x file.
```


#### 0. Where am I?
Prints the absolute path name of the current working directory.

```bash
$ ./0-current_working_directory
/root/alx-system_engineering-devops/0x00-shell_basics
$
```


#### 1. What’s in there?
Display the contents list of your current directory.

```bash
$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
$
```


#### 2. There is no place like home
Changes the working directory to the user’s home directory.

```bash
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ echo $HOME
/home/julien
julien@ubuntu:/tmp$ source ./2-bring_me_home
julien@ubuntu:~$ pwd
/home/julien
julien@ubuntu:~$
```

#### 3. The long format
Display current directory contents in a long format.

```bash
$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
$
```


#### 4. Hidden files
Display current directory contents, including hidden files (starting with .). Use the long format.

```bash
$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
$
```

#### 5. I love numbers
Display current directory contents.
- Long format
- with user and group IDs displayed numerically
- And hidden files (starting with .)

```bash
$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
$
```


#### 6. Welcome
Create a directory named `my_first_directory` in the `/tmp/` directory.

```bash
$ ./6-firstdirectory
$ file /tmp/my_first_directory/
/tmp/my_first_directory/: directory
$
```

#### 7. Betty in my first directory
Move the file betty from `/tmp/` to `/tmp/my_first_directory`.

```bash
$ ./7-movethatfile
$ ls /tmp/my_first_directory/
betty
$
```

#### 8. Bye bye Betty
Delete the file betty.

- The file betty is in `/tmp/my_first_directory`

```bash
$ ./8-firstdelete
$ ls /tmp/my_first_directory/
$
```

#### 9. Bye bye My first directory
Delete the directory `my_first_directory` that is in the `/tmp` directory.

```bash
$ ./9-firstdirdeletion
$ file /tmp/my_first_directory
/tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
$
```

#### 10. Back to the future
Change the working directory to the previous one.

```bash
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp

```
