def recur_fibo(x):
    if x<=1:
        return x
    else:
        return (recur_fibo(x-1) + recur_fibo(x-2))
nterms = int(input("Enter a number for fibonaci sequence "))

if nterms <= 0:
    print("Enter a positive number ")
else:
    print("The fibonaci sequence is : ")
    for i in range(nterms):
        print(recur_fibo(i))
