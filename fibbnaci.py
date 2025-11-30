# Write a Python program to generate the Fibonacci series of N terms.
f0=0
f1=1
for x in range (1,8):
    fn=f0+f1
    print(f0)
    f0=f1
    f1=fn
    