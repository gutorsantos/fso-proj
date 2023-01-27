from queue import Queue
import time
from threading import Thread

MAX_QUEUE_SIZE = 1000

class ProcessesQueue:

    def __init__(self) -> None:
        self.real_time_queue = Queue(maxsize=MAX_QUEUE_SIZE)
        self.thread = Thread(target=self.__wait_for_process)
        self.thread.start()
        # self.user_queue = [Queue(maxsize=MAX_QUEUE_SIZE), Queue(maxsize=MAX_QUEUE_SIZE), Queue(maxsize=MAX_QUEUE_SIZE)] ?

    def __wait_for_process(self):
        while(True):
            print('esperando por processo...')
            if(not self.real_time_queue.empty()):
                print('executando processo ', self.real_time_queue.get().pid)
                time.sleep(5)
            else:
                # if(not self.user.empty()):
                #     print('executando processo ', self.real_time_queue.get().pid)
                #     time.sleep(5)
                pass

            time.sleep(1)