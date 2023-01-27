import time
from threading import Lock, Thread

class Clock:

    def __init__(self) -> None:
        self.miliseconds = 0
        self.lock = Lock()
        self.thread = Thread(target=self.tick)
    
    def tick(self):
        now = time.time() * 1000
        last_frame = time.time() * 1000
        while True:
            now = (time.time() * 1000)
            delta = now - last_frame
            last_frame = now

            if(delta < 1):
                time.sleep(1)
            self.lock.acquire()
            self.miliseconds += delta
            self.lock.release()

    def get_miliseconds(self):
        self.lock.acquire()
        ms = self.miliseconds
        self.lock.release()

        return ms
