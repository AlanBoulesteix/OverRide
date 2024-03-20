## Project README: Finding flag05

We have a small program, after decompile it, we gain the [source code](./source). We can se that it takes two input from STDIN, first is a string, the second is the value of this string serialized.

We have a function with a algo which serialize our string and check if the value is the same as our second input.

### Analysis

The goal is to simply recode the algo but instead of compare the two value we will print the first one. Like this we will have the login and the value of the serialization of this login.


### Progress

After some tries, we manage to write the following python code: [script](./Ressources/craker.py).

We try with one of our name alanboulesteix.

```sh
╭─aboulest at bess-f2r5s1 in ~/Documents/42_Post_CC/OverRide/level06/Ressources on main✘✘✘
╰─± python craker.py              
alanboulesteix
6238474
```

Let's try our cominaison:

- login: `alanboulesteix`
- serial: 6238474

```sh 
level06@OverRide:~$ ./level06 
***********************************
*		level06		  *
***********************************
-> Enter Login: alanboulesteix
***********************************
***** NEW ACCOUNT DETECTED ********
***********************************
-> Enter Serial: 6238474
Authenticated!
$ cd ../level07
$ cat .pass
GbcPDRgsFK77LNnnuh7QyFYA2942Gp8yKj9KrWD8
$ 
```