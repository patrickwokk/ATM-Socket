import socket
import sys

class Server():

    # Default Constructor
    def __init__(self):
        self.account_balance = float(100)  # Beginning balance
        self.beginning_balance = self.account_balance
        self.deposit_amount = float(0)  # Deposit
        self.withdrawal_amount = float(0)  # Withdrawal

    # Deposit method
    def deposit(self, amount, conn):

        # if isinstance(amount, float):
        #     print("Please try again, float number")
        #     data = "Please try again, float number"
        #     conn.send(data.encode())

        # else:
        if amount <= 0:
            print("Negative or zero, please choice from the menu again")
            data = "Negative or zero, please choice from the menu again"
            conn.send(data.encode())
        else:
            # Adding deposited amount to the account balance
            self.account_balance += amount

            # Updating deposit amount
            self.deposit_amount += amount

            # Displaying deposited amount and current balance after adding to the account
            print("Deposit was $%.2f, current balance is $%.2f" % (amount, self.account_balance))
            data = "Deposit was $%.2f, current balance is $%.2f" % (amount, self.account_balance)
            conn.send(data.encode())

    # Withdrawal Method
    def withdrawal(self, amount, conn):
        if amount > self.account_balance:
            print("cannot withdraw money, not enough balance")
            data = "cannot withdraw money, not enough balance"
            conn.send(data.encode())
        elif amount <= 0:
            print("Negative or zero, please choice from the menu again")
            data = "Negative or zero, please choice from the menu again"
            conn.send(data.encode())
        else:
            # Deducting withdrawal amount to the account balance
            self.account_balance -= amount

            # Updating withdrawal amount
            self.withdrawal_amount += amount

            # Displaying withdrawal amount and current balance after deducting from the account
            print("Withdrawal was $%.2f, current balance is $%.2f" % (amount, self.account_balance))
            data = "Withdrawal was $%.2f, current balance is $%.2f" % (amount, self.account_balance)
            conn.send(data.encode())

    # Print balance method
    def print_balance(self, conn):
        # Printing the current balance
        print("Your current balance: $%.2f" % self.account_balance)
        data = "Your current balance: $%.2f" % self.account_balance
        conn.send(data.encode())

def main():
    #af_inet is ipv4, sock_stream is TCP
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 1234
    s = socket.socket()
    s.bind((socket.gethostname(), port))
    s.listen(5)

    clientsocket, address = s.accept()
    print("conncetion from", {address}, "has been established")
    # clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    account = Server()

    while True:
        choice = clientsocket.recv(1024).decode()

        if choice == '1':
            clientsocket.send("How much would you like to deposit today?".encode())
            amount = float(clientsocket.recv(1024).decode())

            #deposit
            account.deposit(amount,clientsocket)

        elif choice == '2':
            clientsocket.send("How much would you like to withdraw?".encode())
            amount = float(clientsocket.recv(1024).decode())

            # Withdrawal
            account.withdrawal(amount, clientsocket)

        elif choice == '3':
             # display current balance
            account.print_balance(clientsocket)

        elif choice == '4':
            #exit
            clientsocket.send("Goodbye!".encode())
            sys.exit(1)

        else:
            #error handling
            print("Please try again")
            clientsocket.send("Wrong, please try again..".encode())

    clientsocket.close()

main()