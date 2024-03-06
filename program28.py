#Write a program to find words whose length is greater than j and less than k.


def word_k(k, s):    
    # split the string where space comes
    word = s.split(" ")
    # iterate the loop for every word
    for x in word:
        # if length of current word
        if len(x)>k:
          # greater than k then
          print(x)
k = 3
s ="Python is good"
word_k(k, s)

