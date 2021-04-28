AREA strcpy, CODE, READWRITE
adr r0,source
adr r1,destination
mov r2,#8
loop1 ldrb r3,[r0],#1
strb r3,[r1],#1
subs r2,r2,#1
bne loop1
source dcb 'a','a','y','u','s','h';
destination dcb '0','0','0','0','0','0'
end

