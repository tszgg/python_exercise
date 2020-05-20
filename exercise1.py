"""
Give the data, construct a dictionary in this format:
output = {
    'Biology': ['Alice', 'David'],
    'Chemistry': ['Alice'],
    ...
}
"""

data = {
    'Alice': 'Biology, Maths, Chemistry',
    'Bob': 'Maths, English,Physics',
    'Charlie': 'Maths',
    'David': 'Biology,Chinese'
}

""" for homework"""


trim_data={}
for k, v in data.items():
    #new_v = list(map(str,v.split(',')))
    new_v = list(map(str,v.replace(' ','').split(',')))
    trim_data[k]=new_v
    #data=trim_data
#print(trim_data)
def reverse_dict(input_data):
    output = {}
    for k in input_data:
        for v in input_data[k]:
            if v in output:
                output[v].append(k)
            else:
                output[v]=[k]
           #output.setdefault(v, []).append(k)
    return output
print(reverse_dict(trim_data))  


#reverse_dict(input_data=data)
    
    
    
    
    
 #using setdefault   

def reverse_dict(input_data):
    output = {}
    for k in input_data:
        for v in input_data[k]:
           output.setdefault(v, []).append(k)
           #setdefault() method returns the value of the item with the specified key.
           #If the key does not exist, insert the key, with the specified value.
    return output
print(reverse_dict(trim_data))
            


#d2 = {key: (map(int, value.split())) for key, value in data.items()} 

#unwrap
def unwrap(input_data):
    result=[]
    for name, subject in input_data.items():
        for value in subject:
            tag= [(name, subject.strip()) for subject in subject.split(',')]     
        result.append(tag)
    return result
print(unwrap(data))



#data={'Biology': ['Alice', 'David'], 'Maths': ['Alice', 'Bob', 'Charlie'], 'Chemistry': ['Alice'], 'English': ['Bob'], 'Physics': ['Bob'], 'Chinese': ['David']}

# for simple list
def reverse_dict(input_data):
    newdict = {}
    for k in input_data:
        for v in input_data[k]:
            newdict.setdefault(v, []).append(k)
    return newdict

print(reverse_dict(data))

#under different situation
#https://www.saltycrane.com/blog/2008/01/how-to-invert-dict-in-python/ 



