from random import randint
from time import sleep

try:
    from .node_based_queue import Queue
except ImportError:
    from node_based_queue import Queue


class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 6)  # Random length between 5 and 6 seconds


class MediaPlayerQueue(Queue):  # esta clase hereda de queue heredada de double_node.py
    def __init__(self):
        super().__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        print(f"Count: {self.count}")  # cuantas canciones hay en la cola

        while (
            self.count > 0 and self.head is not None
        ):  # mientars exista canciones en la cola
            current_track = (
                self.dequeue()
            )  # el nodo actual es el q esta retirando de la cola
            print(
                f"Now playing: {current_track.data.title} (Length: {current_track.data.length} seconds)"
            )
            sleep(current_track.data.length)  # esperar el tiempo de la cancion
            print(f"Finished playing: {current_track.data.title}")
