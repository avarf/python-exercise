print(2.5e1)
print(1e1)
print(1e0)
print(1e-1)
print(1e-2)
s = "this is a string"
print (id(s))
s = "The string changed"
print (id(s))
"This reverse the string like what happens in a list"
print (s[::-1])

"Lists"
num_li = range(10)
print (num_li)

print (type(num_li))
num_li=list(num_li)
print (type(num_li))
num_li.append(55)
print (num_li)
print (num_li*2)

"list with bracket[] / set with kroushe {} / tuple with pranthises"

"Files"
# f = open('text_file.txt')
# f.write("This is a sample line.\n")
# f.write("This is a another line.\n")
# f.close()

"Lamba"
sample_lambda_function = lambda n: n*n
print(sample_lambda_function(5))
print (map(sample_lambda_function, [1,2,3,4]))