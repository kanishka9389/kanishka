#Write a program to print all the character whose length is even. 

def printWords(s): 

     

      s = s.split(' ') 

      for word in s: 

         

        

        if len(word)%2==0: 

            print(word) 

s = "i am smriti"
printWords(s) 







