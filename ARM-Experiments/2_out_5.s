AREA twoout5,code,readwrite
LDR R0, =0xff8899aa
mov R1, #5
mov R2, #0
mov r5, #0x50
back movs r0, r0, RRX
BCC loop
add r2,r2,#1
loop subs r1,r1,#1
BNE back
cmp r2,#2
BNE here
mov r4,#0xff
here str r4,[r5]
end1 B end1
SPACE 50
end