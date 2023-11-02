'''f=open("pudu.txt")
print(f.tell())
print(f.readline())
print(f.seek(4))
print(f.readlines())'''



with open("pudu.txt")as var:
    print(var.read())