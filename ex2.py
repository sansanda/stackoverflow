#Defining mem as stackoverflow-question-305981 list
mem = [1]

def fibo(n):

    #print(mem)
    # len(mem) being shorter than n will indicate that the position is not filled(memoized)
    # if it is equal then is has the required value it wont have to calculate res = fibo(n-1)+ fibo(n-2)
    if len(mem) == n :
        return mem[n]

    #General cases
    if n == 1 or n == 2 :
        res = 1
    elif n == 0 :
        res = 0
    else :
        res = fibo(n-1)+ fibo(n-2)

    #Here the len(m) should be n-1 and thus we append the value of 'res'so at one point we can return it instead of calculating
    mem.append(res)
    return res



def main():
    #Start of Program
    n = int(input("Enter the position :"))


    print(fibo(n))

if __name__ == '__main__':
    main()
