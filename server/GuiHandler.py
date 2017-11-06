import tkinter
import tkinter.messagebox

class GuiHandler:
    def __init__(self,socketHandler_):
        self.socketHandler = socketHandler_

    def sendRecieve(self):
        while True:
            self.text = input()
            if self.text[:1] == "#":
                self.sendMsgBySocketHandler()
                print("Admin: " + self.text[1:])
            elif self.text[0:6] == "/close":
                self.closeConnection()
            elif self.text[0:6] == "/kick ":
                user = self.text[6:]
                self.kick(user)
            else:
                print("Use command #/ in order to take action")

    def kick(self, user):
        lista = self.getList()
        for i in lista:
            if lista[i:1] == user:
                lista[i:0].close()

    def getList(self):
        from server.SocketHandler import SocketHandler
        list = SocketHandler().sendlist
        return list

    def getPort(self):

        self.portEntry = int(input("Please enter the chosen port: \n"))

        self.portToReturn = ""

        def confirmPort():
            self.portToReturn = self.portEntry
            print("hej")

        confirmPort()

        return self.portToReturn


    def sendMsgBySocketHandler(self):
        self.socketHandler.sendAndShowMsg("Admin: " + self.text[1:])

    def closeConnection(self):
        self.socketHandler.closeEveryThing()

