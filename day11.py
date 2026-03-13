

# f=open("data.txt","r")

# content=f.read()

# print(content)

# f=open("bubble.txt","a")
# f=open("bubble.txt","rt")

# f.write("I am wrting the conetnt and what about you")
# f.write("\nhii kaise ho")
# print(content)

# content=f.read()

# f.close()

# print(content)

# with open("data.txt","r") as f:
#     cont=f.read()
#     print(cont)

# with open("data.txt","r") as f:
#     cont=f.readline()
#     print(cont)

#     cont=f.readline()
#     print(cont)
    
#     cont=f.readline()
#     print(cont)
# with open("data.txt","r") as f:

#     while True:
#         cont=f.readline()
#         if not cont:
#             break
#         print(cont)

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()


# f = open('myfile.txt', 'w')

# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#     f.write(line + '\n')
# f.close()

# f=open("myfile.txt","r")

# f.seek(5)

# cont=f.readline()

# print(f.tell())
# print(cont)

# with open('sample.txt', 'w') as f:
#     f.write('Hello World!')
#     f.truncate(8)

# with open('sample.txt', 'r') as f:
#     print(f.read())