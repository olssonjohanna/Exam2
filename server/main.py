
from server.SocketHandler import SocketHandler

socketHandler = SocketHandler()

port = SocketHandler.getPort(SocketHandler)
resultOfBinding = socketHandler.startToAcceptConnection(port)


if resultOfBinding == "failed":
    print ("failed port")
else:
    start = SocketHandler
    start.sendRecieve(socketHandler)
    #GuiHandler.sendRecieve()

