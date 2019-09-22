from socket import *
import io
import subprocess

HEADESIZE = 10

s = socket(AF_INET,SOCK_STREAM)

s.bind(("192.168.5.1", 2000))
s.listen(5)

def file_output(filename, cs):
    f = open(filename, 'rb')
    l = f.read(1024)
    while l:
        print('sending')
        cs.send(l)
        l = f.read(1024)
    f.close()
        
def file_input(filename, cs):
    f = open(filename, 'w')
    l = cs.recv(1024)
    string =''
    csvstring= io.BytesIO()
    csvstring.write(l)
    string += str(csvstring)
    print(string)
    #while l:
     #   print('receiving')
      #  l = cs.recv(1024)
       # csvstring.write(l)
        #string+=str(csvstring)
    f.write(string)
    f.close()


while True:
    clientsocket, addr = s.accept()
    print(addr, " is connected")
    f = open('test.bin', "rb")
    l = f.read(1024)
    while l:
        clientsocket.send(l)
        l = f.read(1024)
    f.close()
    ##file_input('arguments.csv', clientsocket)
##SFM = subprocess.Popen("./SingleFrameMode", shell = True)
    ##while SFM.poll() == None:
       ## pass
    ##file_output('result.bmp', clientsocket)
    
    #clientsocket.send(bytes("done","utf-8"))
#    f = open('result.bmp', 'rb')
#    l = f.read(1024)
#    while l:
#        print('sending')
#        clientsocket.send(l)
#        l = f.read(1024)
#    f.close()
    print("done")
    clientsocket.close()

    






