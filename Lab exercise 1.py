#CALMA, Eugene Marie S.
#BSCPE_1-4
#OOP Laboratory Exercise Number 2 Problem 1 (Encryption)

# input or insert your text here
input_str = input("Hi, Good day! Please insert your text here. ")
output_str = ""
# check and change every character to their corresponding variable
for i in range (len(input_str)):
#   if a, change to *
    if input_str[i] == "a":
        output_str += "*"
    
#   if e, change to &
    elif input_str[i] == "e":
        output_str += "&"
    
#   if i, change to #
    elif input_str[i] == "i":
        output_str += "#"
    
#   if o, change to +
    elif input_str[i] == "o":
        output_str += "+"
  
#   if u, change to !
    elif input_str[i] == "u":
        output_str += "!"
    else:
        output_str += input_str[i]
# print your output
print(output_str)