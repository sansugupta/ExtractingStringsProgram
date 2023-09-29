with open('D:\preproinsulin-seq-clean.txt', 'r') as file:
    text = file.read()
    print('Original file: ', text)


import re
new_text = re.sub(r"ORIGIN|\d+|//|\s+", "", text)


with open('D:\preproinsulin-seq-clean.txt', 'w') as file:
    file.write(new_text)
    print('After Editing: ', new_text)
    print(len(new_text))


with open('D:\preproinsulin-seq-clean.txt','r') as file1:
    content = file1.read(24)
    print(content)

# file=open('automation.txt','w')
# file.write(new_text)
# # file.close()

f = open('automation.txt','w')
f.write(new_text)

f = open('automation.txt','r')
text1 = f.read()
print(text1)
print(len(text1))

f = open('lsinsulin-seq-clean.txt','w')
f.write(content)

extracted_character = new_text[25:54]
f = open('binsulin-seq-clean.txt','w')
f.write(extracted_character)

extracted_character_2 = new_text[55:89]
f = open('cinsulin-seq-clean.txt','w')
f.write(extracted_character_2)

extracted_character_3 = new_text[90:110]
f = open('ainsulin-seq-clean.txt','w')
f.write(extracted_character_3)




# file2 = open('lsinsulin-seq-clean','w')
# a = file2.write(content)
# print(a)
    



