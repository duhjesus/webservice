import socket 



# init_server
# function: initialize a TCP server working with IPV4 
# Input: None
# Output: None
# Effect: Makes a server waiting for a connection  

def init_server():
#addr_family = af_inet (ipv4) or af_inet6(ipv6)
# TODO: ipv6 option 
#socket = sock_dgram(udp) or sock_stream(tcp)
    print("HELLO!")
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 51151 # TODO:multiple clients?, threading?
    #HOST = socket.gethostname()
    ss.bind(('',PORT))
    ss.listen(10) # backlog pending connections, multiple clients change?
    while True:
        try:
            dataSocket, netAddr_PortAddr = ss.accept()
            #received_str = "Received a connection from client with netaddr & port#:" #4debugging
           # print (received_str + str(netAddr_PortAddr)) # 4debugging
            #dataSocket.send("\n Hello "+str(netAddr_PortAddr)+"\n") 
            data = dataSocket.recv(1024) #TODO: HTTP format headers
            print("data=",data)
            fibStored = fibonacci( int(data))
            if fibStored == -1:
                fibString = "Positive Numbers Please"
            else:
                print(fibStored)
                fibString = ' '.join(fibStored)
            lenFib = len(fibString)
            print(lenFib)
            print(fibString)
            #dataSocket.send(str(lenFib)+'\n')
            dataSocket.send(fibString) 
            dataSocket.close()
        except KeyboardInterrupt:
            ss.close()
            break
            

# TODO: want to save existing numbers in a data structure and possibly incorporate threading to handle multiple read/writes from multiple clients
# fibonacci
# function: returns the first n Fibonacci numbers, starting from 0.
# Input: n, takes on positive values 
# Ouput: save first n Fibonacci numbers in a list 
# Effect: if negative or 0 return error

def fibonacci(n):
    if n == 0:
        return -1
    if n == 1:
        return 0
    prev = 0
    curr = 0
    nextt = 0
    fibStored = []
    cnt = 1
    while cnt <=n:
        if cnt == 1:
            fibStored.append(str(nextt))
            cnt = cnt +1
            continue 
        if cnt ==2:
            nextt =1
            fibStored.append(str(nextt))
            curr = nextt
            cnt = cnt +1
            continue             
        nextt = curr + prev
        fibStored.append(str(nextt))
        prev = curr
        curr = nextt 
        cnt = cnt +1
    return fibStored 


def main():
    init_server()

if __name__ == "__main__":
    main() 