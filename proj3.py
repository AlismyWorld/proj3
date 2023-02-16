from socket import*
s=socket()
s.connect(("localhost",1500))
print("req sent")
print(s.recv(1024),"connected")
while True:
    print(s.recv(1024))
    msg=input("enter msg:")
    s.send(bytes(msg,'UTF-8'))