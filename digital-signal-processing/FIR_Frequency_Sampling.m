%%Design a linear phase FIR low pass filter using
%%frequency sampling method. Let M=17(order)
%%and cutoff frequency is wc=pi/2 rad/sample
%%Desired frequency response
%%Hd(w)= exp(-%j*w(M-1)/2) for 0<=w<=pi/2
%% = 0 for pi/2<=w<=pi
%%from Hd(w) we get H(k) by sampling w=(2*pi*k)/M
%% H(k)= Hd(w)| at w=(2*pi*k)/M
%% h(n)=1/M <summ k=0 to M-1>[H(k)e^j2pikn/M] 0<=n<=M-1
%%h(n) must be real
%% h(n)=1/M(H(0)+ 2 <summ n=1 to p> Re[H(k)e^j2pikn/M])
%%p=(M-1)/2 if N is odd
%% =M/2 -1 if N is even


clc;
clear all;
close all;
wc=pi/2; %%cutt of freq in rad/sample
M=17; %%take odd order
%%Desired frequency response
w=0:(pi/256):pi;
Hd_w =([w<=pi/2]).* exp(-i*w*(M-1)/2);
figure;
subplot(3,1,1);
plot(w,abs(Hd_w));
title('Magnitude response of desired filter');
xlabel('w');
ylabel('|Hd(w)|');

%%(2*pi*kc)/M <= pi/2
%% kc <= (pi/2)*(M/(2*pi))
%% kc<= M/4 = 17/4, but k can take only integer=4
kc = floor(wc*(M/(2*pi)));
k=0:(M-1)/2;
%%frequency sampling Hd_w to get Hk
Hk = ([k<=kc]).* exp(-i*(2*pi*k/M)*((M-1)/2))
subplot(3,1,2);
stem(k,abs(Hk));
title('Sampled Magnitude response Hd_w');
xlabel('k');
ylabel('|H(k)|');
%% Taking idft of H(k) to find h(n)
for n=0:(M-1)
sumHk=0;
for k=1:(M-1)/2
sumHk = sumHk+real(Hk(k+1)*exp(i*2*pi*k*n/M));
end
hn(n+1)=(1/M)*(Hk(1)+2*sumHk);
end

n=0:(M-1);
subplot(3,1,3);
stem(n,hn);
title('Impulse response h(n) of filter')
xlabel('n');
ylabel('hn');

[H,f]=freqz(hn,1,1000);
H_mag=20*log10(abs(H));
figure;
plot(f,H_mag);
xlabel('Normalized frequency');
ylabel('Magnitude');
disp('FIR Filter coeff hn');
disp(hn);