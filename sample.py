import socket

print("This Software find your Target ip addres")
print("")

host = input("Enter The Domin : ")

ip = socket.gethostbyname(host)
print("")
print("your Target ip address : '"+ip+"'")

print("")
print("")
print("")

print("result :")
print("")
print("Target Domin address"+" "+host+" "+"Target ip address"+" "+ip)
