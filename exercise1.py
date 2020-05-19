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

trim_data={}
for k, v in data.items():
    new_v = list(map(str,v.replace(' ','').split(',')))
    trim_data[k]=new_v
    data=trim_data

def reverse_dict(input_data):
    # TODO
    output = {}
    for k in input_data:
        for v in input_data[k]:
            if v in output:
                output[v].append(k)
            else:
                output[v]=[k]
           #output.setdefault(v, []).append(k)
    return output  # TODO


reverse_dict(input_data=data)
