inputstring=input("enter your string")
count_dict={}
for ch in inputstring:
    if ch.isalpha():
        count_dict[ch]=count_dict.get(ch,0)+1
for key , value in count_dict.items():
    print(f"{key}:::{value}")
