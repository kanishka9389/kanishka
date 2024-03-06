#Write a program to find  uncommon words from two string.

def UncommonWords(A, B):

    A=A.split()

    B=B.split()

    x=[]

    for i in A:

        if i not in B:

            x.append(i)

    for i in B:

        if i not in A:

            x.append(i)

    x=list(set(x))

    return x

             
 

A = "Geeks for Geeks"

B = "Learning from Geeks for Geeks"
 


print(UncommonWords(A, B))






