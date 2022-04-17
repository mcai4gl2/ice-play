import sys
import Ice
from Demo import Hello


class HelloServer(Hello):
    def SayHello(self, input, current=None):
        return f"Hello {input}"


if __name__ == "__main__":
    communicator = Ice.initialize(sys.argv)
    try:
        adapter = communicator.createObjectAdapterWithEndpoints("HelloAdapter", "default -p 10000")
        servant = HelloServer()
        adapter.add(servant, communicator.stringToIdentity("hello"))
        adapter.activate()
        communicator.waitForShutdown()
    finally:
        communicator.destroy()

