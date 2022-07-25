import socket 

trg_hst = input("Enter The Host Name => ")
trg_prt = input("Enter The Port Number => ")

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"HelloWorld",(trg_hst,trg_prt))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()
