input_str = '010010'
subsets = []
for i in range(len(input_str)):
    if input_str[i] == '0':
        for j in range(i+1, len(input_str)+1):
            subset = input_str[i:j]
            subsets.append((i, subset))  # Adding the index along with the subset
print("Index number and subsets of '0':", subsets)
