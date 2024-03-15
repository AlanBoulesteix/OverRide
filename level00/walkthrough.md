## Project README: Finding flag00

### Introduction
In this level of the OverRide project, our task is to gain access to the level01 user account. We begin by connecting to our virtual machine using SSH:

```sh
ssh level00@localhost -p 4545
```

Upon successful authentication, we find a program waiting for us. Our first step is to understand its functionality. To accomplish this, we utilize the excellent tool [dogbolt](https://dogbolt.org/) to decompile the binary, revealing the [source code](./source).

### Analysis

Upon examining the source code, we discover that the program expects a password to be entered. Interestingly, line 12 of the source code reveals that the password must be `5276`.

### Progress

With this information in hand, we proceed to execute the program with the provided password:

```sh
level00@OverRide:~$ ./level00 
***********************************
* 	     -Level00 -		  *
***********************************
Password:5276

Authenticated!
$ whoami
level01
$ 
```
Success! We have authenticated as `level01`. Now, all that remains is to navigate to our home directory and read the `.pass` file.