## Project README: Finding flag03
When we use gdb to see assembly code we saw that we have 3 important functions:

- main
- test
- decrypt

### Analysis

After puting our code into langage C, we saw that our code sub our input 
to 322424845, and then try if the result is between 1 and 21. if it does, we use the dif as key for each char of the string v4. if we have the good one, The program will change the string ``Q}|u`sfg~sf{}|a3`` into `Congratulations!` and then run a bash. Okay simple, let's just try to brutforce our program. 

### Progress

We did a small [script](./Ressources/script.py) that trys every key to decode the password ``Q}|u`sfg~sf{}|a3`` and it return `18`.

322424845 - 18 = 322424827

Let's try:

```sh
level03@OverRide:~$ ./level03 
***********************************
*		level03		**
***********************************
Password:322424827
$ whoami
level04
$
```

As always, let's mouve into level03 directory then print .pass file.