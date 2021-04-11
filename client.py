import socket

def menu():
    print('Welcome: ')
    print('1. Deposit')
    print('2. Withdrawal')
    print('3. Account Balance')
    print('4. Quit')

#af_inet is ipv4, sock_stream is TCP
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
s = socket.socket()
s.connect((socket.gethostname(), port))

menu()
while True:
    # menu()
    try:
        choice = int (input(">>> "))
        msg = str.encode(str(choice),'utf-8')
        s.send(msg)
        print(s.recv(1024))
        # menu()

    except ValueError:
        print('integer only...')
        # choice = int (input(">>> "))



s.close #close socket


# fullMsg = ''
# while True:
#     msg = s.recv(8)
#     if len(msg) <= 0:
#         break
#     fullMsg += msg.decode("utf-8")

# print(fullMsg)