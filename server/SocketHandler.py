import socket
import _thread
import sys
from server.Users import CollectionOfUsers
#hej
class SocketHandler:
    def __init__(self):
        self.serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.users = CollectionOfUsers()
        self.users.readUsersFromFile()

        self.userlist = []
        self.socketlist = []

    def closeEveryThing(self):
        self.serverSocket.close()
        self.users.writeUsersToFile()
        sys.exit(0)

    def startAccepting(self):
        while True:
            try:
                clientSocket, clientAddr = self.serverSocket.accept()
                self.list_of_unknown_clientSockets.append(clientSocket)
                self.list_of_unknown_clientAddr.append(clientAddr)
                self.startReceiverThread(clientSocket, clientAddr)

            except:
                pass

    def startToAcceptConnection(self,port):
        try:
            self.serverSocket.bind(('',int(port)))
        except:
            return "failed"
        self.serverSocket.listen()

        self.list_of_known_clientSockets = []
        self.list_of_known_clientAddr = []

        self.list_of_unknown_clientSockets = []
        self.list_of_unknown_clientAddr = []

        self.listOfSocketAndUser = []

        _thread.start_new_thread(self.startAccepting,())
        return "succeed"

    def sendAndShowMsg(self, text):
        print(text)
        for clientSock in self.list_of_known_clientSockets:
            clientSock.send(str.encode(text))

    def startReceiverThread(self, clientSocket, clientAddr):
        _thread.start_new_thread(self.startReceiving,(clientSocket,clientAddr,))

    def startReceiving(self,clientSocket, clientAddr):
        resultOfLogin = self.listenToUnknownClinet(clientSocket,clientAddr)
        print()

        if resultOfLogin !=False:
            username = resultOfLogin
            self.list_of_unknown_clientSockets.remove(clientSocket)
            self.list_of_unknown_clientAddr.remove(clientAddr)

            self.list_of_known_clientSockets.append(clientSocket)
            self.list_of_known_clientAddr.append(clientAddr)
            self.socketlist.append(clientSocket)
            self.userlist.append(username)

            self.listenToknownClinet(clientSocket,clientAddr,username)





         #   self.listOfSocketAndUser.append(clientSocket)

    def listenToUnknownClinet(self,clientSocket, clientAddr):
        while True:
            try:
                msg = clientSocket.recv(1024).decode()
            except:
                self.list_of_unknown_clientSockets.remove(clientSocket)
                self.list_of_unknown_clientAddr.remove(clientAddr)
                return False

            args = msg.split(' ')
            if len(args) == 3 and args[0] == "login":
                username = args[1]
                password = args[2]
                if self.users.doesThisUserExistAndNotActive(username,password):
                    clientSocket.send(str.encode("ok"))
                    self.sendAndShowMsg(username + " is connected")
                    return username
                else:
                    clientSocket.send(str.encode("not ok"))

            if len(args) >= 5 and args[0] == "register":
                username = args[1]
                password = args[2]
                email = args[3]
                name = ""
                for rest in args[4:]:
                    name += rest + " "
                if username != "" and password != "" and email != "" and name != "":
                    resultOfAdding = self.users.add_user(username,password,email,name)
                    if resultOfAdding == True:
                        clientSocket.send(str.encode("fine"))
                    else:
                        clientSocket.send(str.encode("not fine"))
                else:
                    clientSocket.send(str.encode("not fine"))

    def listenToknownClinet(self,clientSocket, clientAddr,username):
        while True:
            try:
                msg = clientSocket.recv(1024).decode()

                self.sendAndShowMsg(username + ": " + msg)
            except:
                self.list_of_known_clientSockets.remove(clientSocket)
                self.list_of_known_clientAddr.remove(clientAddr)
                self.sendAndShowMsg(username+" disconnected")
                self.users.inactiveUser(username)

                return

    def sendRecieve(self):
        while True:
            self.text = input()
            if self.text[:1] == "#":
                self.sendMsgBySocketHandler()
            elif self.text[0:6] == "/close":
                self.closeConnection()
            elif self.text[0:6] == "/kick ":
                user_list = self.text[6:]
                self.kick(user_list)
            else:
                print("Use command #/ in order to take action")

    def kick(self, user_list):
        if user_list in self.userlist:
            self.socketlist[self.userlist.index(user_list)].close()
        else:
            print("false")



    def getPort(self):

        self.portEntry = int(input("Please enter the chosen port: \n"))

        self.portToReturn = ""

        def confirmPort():
            self.portToReturn = self.portEntry

        confirmPort()

        return self.portToReturn

    def sendMsgBySocketHandler(self):
        self.sendAndShowMsg("Admin: " + self.text[1:])

    def closeConnection(self):
        self.closeEveryThing()


