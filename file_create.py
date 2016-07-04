import os.path
while True:
    filename=input('Please you input filename:')
    if os.path.exists(filename):
        with open(filename) as f:
             print (f.readlines())
           
    else:
        with open(filename,'w') as f:
             print (filename)
             break
