import os
ls = os.linesep

"""get file name"""
while True:
    fname = input("Enter fname: ")
    if os.path.exists(fname):
        print("error: {} is already exists".format(fname))
    else:
        break

"""get file content"""
al = []
print("\nEnter lines ('.') by itself to quit.\r")

while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        al.append(entry)

"""white lines to file with proper line-ending"""
f = open(fname, 'w')
f.writelines(["{}{}".format(x, ls) for x in al])
f.close()
