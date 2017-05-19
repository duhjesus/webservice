import socket 


def main():
    n = raw_input("Please enter N:")
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect((socket.gethostname(),51151)) # 80 default for TCP 
    #ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    data = ss.send(str(n)) #TODO: HTTP HEADER
    data = ss.recv(10000)
    #lenFib = int(data)   # TODO: take into account variable length 
    #data = ss.recv(lenFib)
    print(data)
    ss.close()



if __name__ == "__main__":
    main() 