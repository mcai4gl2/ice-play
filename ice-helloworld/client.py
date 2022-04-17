import sys
import Ice
from Demo import HelloPrx


if __name__ == "__main__":
    communicator = Ice.initialize(sys.argv)
    try:
        base = communicator.stringToProxy("hello:default -p 10000")
        hello = HelloPrx.checkedCast(base)
        if not hello:
            raise RunTimeErrror("Invalid ice proxy")
        result = hello.SayHello("World!")
        print(f"Reply from server: {result}")
    finally:
        communicator.destroy()

