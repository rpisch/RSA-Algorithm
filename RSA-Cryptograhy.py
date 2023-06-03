
import random

# this function generates a lsit of prime numbers of length "N"
def primes_list(N):
    primes = []                         # new list
    primes.append(2)                    # 2 must be added to the list first since it is the first prime, and cannot be computed by the algorithm
    k = 3                               # set starting value to 3
    count = 0                          
    check = 0  
    # while the length of the list is less than the desired list length                         
    while check<N-1: 
        # if an even number is not divisible by any number in the primes list, it is a prime number                   
        for value in primes:
            if (k%value != 0):          
                count +=1
        # if a number is a prime add it to the list
        if (count == len(primes)):      
            primes.append(k)
            check +=1                   
        k+=2                            # loop through even numbers
        count = 0                       # reset list counter
    return primes


# this function returns s: the inverse of a mod p, and a flag of whether the inverse exists or not
def inverse_mod_n(a,p):
    r, s = gcd(a,p)         # take the gcd of a and p
    # if the gcd is not one, there is no inverse
    if (r!= 1):             
        flag = False
    # if the gcd is one, there is an inverse
    else:
        flag = True
    return s,flag           # return a^-1 % p


# this function takes numbers a and p and returns the gcd result (oldr) ad olds
# uses the extended euclidian algorithm to divide the divisor by the remainder until the remainder is zero
def gcd(a,p):
    (oldr,r) = (a,p)                    # initialize oldr as a and r as p
    (olds,s) = (1,0)                    # initialize olds as 1 ans s as 0
    (oldt,t) = (0,1)                    # initialize oldt as 0 and t as 1
    # loop while the remaindor is not yet zero
    while (r!=0):                       
        q = oldr//r                     # divide dividor by remaindor
        (oldr,r) = (r,oldr - q*r)       # r becomes old r and the new r becomes the old r minus q*r
        (olds,s) = (s,olds - q*s)       # s becomes old s and the new s becomes the old s minus q*s
        (oldt,t) = (t,oldt - q*t)       # t becomes old t and the new t becomes the old t minus q*t
    if (olds<0):                        # if the prevous iteration of s is negative add p to make it positive
        olds = olds + p
    return oldr, olds                   # return the gcd


# simple recursive exponent function
# returns x^n % N
def expn(x,n,N):
    # x^0 = 1
    if (n == 0):
        return 1
    # if the exponent is even:
    elif (n%2 == 0):
        return expn((x*x) % N, int(n/2), N)                 # keep multiplying the number by itself until n is zero and the function ends, take the mod
    # if the exponent is odd:
    else:
        return (x*expn((x*x) % N, int((n-1)/2), N)) % N     # starting with x since its odd, keep multiplying the number by itself until n is zero and the function ends, take the mod


# RSA to encode the message and give a public key
def RSA(n):
    # use list of primes
    primes = primes_list(n)
    # select 2 random indexes of the primes list
    p = random.randint(0,n-1)
    q = random.randint(0,n-1)
    # use the index to pick to random prime values
    prime1 = primes[p]
    prime2 = primes[q]
    # find the gcd of these random prime numbers minus 1
    (g,s) = gcd(prime1-1, prime2-2)
    # multiply the primes -1 to eachother and divide by the gcd
    l = (((prime1-1)*(prime2-1))/g)

    
    found = False
    while(found == False):
        e = random.randint(3,l)         # take a random integer e in between 3 and l, this is the first half of the public key
        k,found = inverse_mod_n(e,l)    # end the loop when an inverse of e is found
    N = prime1*prime2                   # when e has an inverse, muliply the original prime numbers for the second half of the key

    s = []                              # new list s for encrypted list
    d = []                              # new list d for decrypted list

    m = input("Encode a message: ")         # take m as an input message
    for i in range (0, len(m)):             # encrypt all characters of m and add to s
        s.append(expn(ord(m[i]),e,N))       # s is the encrypted output using the public keys

    for i in range (0, len(s)):             # loop through all index's of encrypted list 
        d.append(chr(expn(s[i],k,N)))       # convert all characters into string type using the public and private keys
    decrypted_RSA = ''.join(d)              # join into a string from the list


    # print results including the encoded message and the public keys, and the decoded message
    print()                                 
    print("Encrypted Message: ")
    print(s)
    print("public key: N =", N, " e =",e)
    print()
    print("Decrypted Message: ")
    print(decrypted_RSA)
    print()


print()
RSA(100)    #call RSA function with 100 primes in the prime list
