EXPLANATION
==================

In the beginning, we have freq['blue']=0 and freq['yellow']=0

The first line of the file is:
My name is John and I live in the blue house

After we lower, strip, and split we get the following list of words:
words=['my','name','is','john','and','i','live','in','the','blue','house']

after going over all the words in the list, the counts become:

freq['blue']=1
freq['yellow']=1

We proceed in the same way for all the lines in the file.


NOTES
================
- Remember to use indentation. Best to use a <TAB>. Add one level for each if,for,while

- We create a new dictionary by typing: myDict={}. A dictionary maps keys to values. In our case, words to numbers (their frequencies).
Keys are unique, values are not. Searching for keys in dictionaries is fast!

- Remember to wrap string in quotes ('textfile, 'blue', etc)