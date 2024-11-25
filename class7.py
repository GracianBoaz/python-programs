"""
#Python code to Count Alphabets, Special character Numeric values and space 
string=input("Please enter a string: ")#take input from the user 
alphabets,num,special,space=0,0,0,0;#variable declaration and initilization
a=[]
d=[]
spl=[]
for i in range(len(string)): 
  if(string[i].isalpha()): #check Alphabets letters 
      #print(string[i],end="")
      alphabets+=1
      a.append(string[i])
  elif(string[i].isdigit()):#check numeric value 
      #print(string[i],end="")
      num+=1
      d.append(string[i])
  elif(string[i].isspace()):#check space 
      space+=1 
  else: 
      #print(string[i],end="")
      special+=1
      spl.append(string[i])
print("Alpabets letters: ",alphabets, a) 
print("\nnumbers: ",num, d) 
print("\nSpace: ",space) 
print("\nSpecial characters: ",special, spl)"""
#2
"""str = input("Enter the string:")
vcount, ccount= 0,0 
Vowels = "AaEeIiOoUu"
c=[]
v=[]
#Converting entire string to lower case to reduce the comparisons  
#str = str.lower()  
for i in range(0,len(str)):   
    #Checks whether a character is a vowel  
    if str[i] in (Vowels):  
        vcount = vcount + 1
        v.append(str[i])
        #count = [each for each in str if each in Vowels]
     
    elif (str[i] !=" " and str[i] not in (Vowels)):
        ccount = ccount + 1
        c.append(str[i])
print("Total number of vowel and consonant are" );  
print(vcount,v) 
print(ccount,c)  

"""
#3
"""
def match(s1,s2):
    count=0
    
    for i in range(min(len(s1),len(s2))):
        if s1[i].lower()==s2[i].lower():
            count=count+1
    return count

#Driver Program
S1="What"
S2="watch"
print("Total number of matches:")
print(match(S1,S2))
"""
#4
"""#Program to print number of words in a line and number of lines in a para

string='''This is the most straightforward way to count the number
of lines in a text file in Python. The readlines() method reads all
lines from a file and stores it in a list. Next, use the len() function
to find the length of the list which is nothing but total lines present in a file.'''
str1=string.split(".")
str1.pop()
print("Number of lines: ",len(str1))
print("Number of words in each line:")
for i in range(len(str1)):
    words=str1[i].split()
    #print(words)
    print("Line",i+1,len(words))
"""
#5
# Program to find number of sentences starts with "B"
"""
string=input(“Enter the Para: ”)
str1=string.split(" ...")
str1.pop()
print("Total number of lines:",len(str1))
count=0
for i in str1:
    str2=i.split()
    #print(str2)
    for j in str2:
        if j[0]=="B":
            count=count+1
print("Number of Sentences that start with letter B :",count)
"""
#6
"""str = input("Enter the String:")

# Character to find
c = input("Enter the character to find:")

# Using Naive Method
res = None
j=0
while j<len(str):
    for i in range(0,len(str),1):
        if str[i] == c:
            res = True
            print(str[i], "Index:",i)
        j=j+1
if res==None:
    print("Character not found")"""
#7
"""str=input("Enter the string:")
str=str.upper()
sort_str=sorted(str)
print(sort_str)
join_str="".join(sort_str)
rev_str=join_str[::-1]
print(join_str)
print(rev_str)"""
#8
"""string = input("Enter the string:")
string=string.lower()
repeat=[]
print("Duplicate characters in a given string: ");  
#Counts each character present in the string  
for i in range(0, len(string)):  
    count = 1
    
    for j in range(i+1, len(string)):
        
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;
            
            #Set string[j] to 0 to avoid printing visited character  
            string = string[:j] + '0' + string[j+1:]  
   
    #A character is considered as duplicate if count is greater than 1  
    if(count > 1 and string[i] != '0'):
        repeat.append(string[i])
        print(string[i],count)
        
print("Number of repeated characters:", len(repeat),repeat)

"""
#9
"""
s1 = "welcome"
s2 = "homely"
n = int(input("n="))
output = ""
i = 0
j = 0
while i < len(s1) and j < len(s2):
    output += s1[i:i+n] + s2[j:j+n]
    i += n
    j += n
output += s1[i:] + s2[j:]
print(output)
"""
#10
text = input("Enter the String: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newtext = ""
for i in range(len(text)):
    if text[i] not in vowels:
        newtext = newtext + text[i]

print("\nString after removing Vowels: ")
text = newtext
print(text)
