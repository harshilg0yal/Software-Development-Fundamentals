def problem1(n:int,steps:int=0) -> int:
    if n == 1:
        return steps
    elif n % 2 == 0:
        return problem1(n//2,steps+1)
    else:
        return problem1(3*n+1,steps+1)

def reverse_line(name:str):
    op_file=(str)name+"_op.txt"
    with open(name,"r") as infile,open(op_file,"w") as outfile:
        for line in infile:
            
            if line.endswith("\n"):
                strip_line=line[:-1]
                newchar="\n"
            else:
                strip_line=line
                newchar=""

            rev_str=strip_line[::-1]
            outfile.write(rev_str+newchar)

def wordcount(filename: str="wclist.txt"):
    with open(filename, 'r') as f:
        text = f.read()
    
    char_count = len(text)
    
    words = text.split()  
    word_count = len(words)
    unique_word_count = len(set(words))
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    line_count = len(lines)
        
    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")
    print(f"Unique Words: {unique_word_count}")

    
def dictdiff(d1:dict,d2:dict)->dict:
    d3={}
    for key in d1.keys():
        if key in d2 and d1[key]!=d2[key]:
            d3[key]=[d1[key],d2[key]]
        elif key not in d2:
            d3[key]=[d1[key],None]
    for key in d2.keys():
        if key not in d1:
            d3[key]=[None,d2[key]]
    return d3

PEOPLE = [{'first':'Narendra', 'last':'Modi',
'email':'naren@modi.co.in'}, {'first':'Donald',
'last':'Trump','email':'president@whitehouse.gov'},
{'first':'Vladimir', 'last':'Putin',
'email':'president@kremvax.ru'}]

def alphabetize_name():
    return sorted(PEOPLE,key=lambda person:(person['last'],person['first']))

def most_repeating_word(sequence_of_strings):
    most_rep_letter=0
    most_repeating_word=""
    for word in sequence_of_strings:
        for letter in set(word):
            if word.count(letter)>most_rep_letter:
                most_rep_letter=word.count(letter)
                most_repeating_word=word
    return most_repeating_word

def format_sort_records(PEOPLE):
    string=""
    for person in PEOPLE:
        string += f"{person[1]} {person[0]} {person[2]:.2f}\n"
    return string

def passwd_to_dict(name:str):
    with open("passwd.txt","r") as f:
        lines=f.readlines()
    passwd_dict={}
    for line in lines:
        if ":" in line:
            parts = line.split(":")
            passwd_dict[parts[0].strip()]=parts[2].strip()
    return passwd_dict
            
def gematria_for(word:str)->int:
    alpha_dict={}
    for i in range(26):
        alpha_dict[chr(i+97)]=i+1
    gematria_score=0
    for i in range(len(word)):
        if word[i] in alpha_dict:
            gematria_score += alpha_dict[word[i]]
    return gematria_score

def gematria_for_list(word_list:list)->list:
    gematria_list=[]
    for word in word_list:
        gematria_list.append(gematria_for(word))
    return gematria_list

import random
def create_password_generator(input:str):
    def generate_password(length:int)->str:
        return ''.join(random.choice(input) for _ in range(length))
    return generate_password

class Circle:
    def __init__(self,sequence,number:int):
        self.sequence=sequence
        self.number=number
    def __iter__(self):
        return CircleIterator(self.sequence,self.number)

class CircleIterator:
    def __init__(self,sequence,number:int):
        self.sequence=sequence
        self.number=number
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=self.number:
            raise StopIteration
        else:
            value=self.sequence[self.index%len(self.sequence)]
            self.index+=1
            return value

class Animal:
    def __init__(self, color, number_of_legs):
        self.color = color
        self.number_of_legs = number_of_legs

    def __str__(self):
        return f"Animal(Color: {self.color}, Legs: {self.number_of_legs})"


class Cage:
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        animal_list = ", ".join(str(animal) for animal in self.animals)
        return f"Cage {self.cage_id}: [{animal_list}]"


class Zoo:
    def __init__(self):
        self.cages = {}

    def add_cage(self, cage):
        if cage.cage_id in self.cages:
            print(f"Cage with ID {cage.cage_id} already exists.")
        else:
            self.cages[cage.cage_id] = cage

    def add_animal_to_cage(self, cage_id, animal):
        if cage_id in self.cages:
            self.cages[cage_id].add_animal(animal)
        else:
            print(f"Cage {cage_id} does not exist in the zoo.")

    def filter_animals_by_color(self, color):
        result = []
        for cage in self.cages.values():
            for animal in cage.animals:
                if animal.color.lower() == color.lower():
                    result.append(animal)
        return result

    def filter_animals_by_legs(self, number_of_legs):
        result = []
        for cage in self.cages.values():
            for animal in cage.animals:
                if animal.number_of_legs == number_of_legs:
                    result.append(animal)
        return result

    def total_number_of_legs(self):
        total = 0
        for cage in self.cages.values():
            for animal in cage.animals:
                total += animal.number_of_legs
        return total

    def __str__(self):
        return "\n".join(str(cage) for cage in self.cages.values())

def problem13():
    digit=int(input("Enter the number upto which you need the digits of pi (must be less than 100): "))
    if digit > 100:
        raise ValueError("The number must be less than 100")
    elif digit < 0:
        raise ValueError("The number must be greater than 0")
    pi="3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    print(pi[:digit+2])

def problem14(s:str):
    n = len(s)
    if n == 0 :
        return 0,""
    
    l = 0
    char_map={}
    max_len = 0
    max_sub=""
    
    for r in range(n):
        char = s[r]
        char_map[char] = char_map.get(char,0)+1
        while len(char_map) > 2:
            left_char = s[l]
            char_map[left_char] -= 1
            if char_map[left_char] == 0:
                del char_map[left_char]
            l+= 1
        if r-l+1 > max_len:
            max_len = r-l+1
            max_sub = s[l:r+1]
    return max_len,max_sub

def problem15(arr:list):
    if not arr:
        return []
    
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    longest=[]
    curr=[arr[0]]
    
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            continue
        
        if arr[i] == arr[i-1]+1:
            curr.append(arr[i])
        else:
            if len(curr) > len(longest):
                longest=curr
            
            curr=[arr[i]]
    if len(curr) > len(longest):
        longest=curr
    return longest        
