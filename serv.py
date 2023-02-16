from socket import*
s=socket()
print("socket object created")
s.bind(('localhost',1500))
print("port allocated")
s.listen(3)
print("waiting for client");
c,addr=s.accept()


print("connected with",addr)
while True:
    msg=input("enter msg:")
    c.send(bytes(msg,'utf-8'))
    print("client:",c.recv(1024).decode())