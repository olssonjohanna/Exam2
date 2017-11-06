

class GuiHandler:
    def __init__(self,socketHandler_):
        self.socketHandler = socketHandler_

    def getPort(self):

        self.portEntry = int(input("Please enter the chosen port: \n"))

        self.portToReturn = ""

        def confirmPort():
            self.portToReturn = self.portEntry

        confirmPort()

        return self.portToReturn

    def startMainGui(self):

        #här ska det in som kallar på funktion för closeConnection och sendMsgBySocketHandler



    def sendMsgBySocketHandler(self):
        self.socketHandler.sendAndShowMsg("Admin: " + self.text)

    def closeConnection(self):
        self.socketHandler.closeEveryThing()

    def startGui(self):
        self.startMainGui()

    def showMessage(self,text):
        #tror denna är helt onödig(?)
        self.chattContents.insert(tkinter.END,text+"\n")

    def showWarningMsg(self):
        tkinter.messagebox.showwarning(message="could not bind port")
