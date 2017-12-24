from threading import Thread
from random import random
from math import sin
import numpy as np
import collections


class VirtualSensor(Thread):

    def __init__(self, deviceId, consumer, event, frequency=0.010):

        Thread.__init__(self)
        self._id = deviceId
        self._consumer = consumer
        self._producer = lambda x: x * sin(x)
        self._frequency = frequency
        self._cancellationToken = event
        self._deque  = collections.deque(np.linspace(0,100, 1000))

    def _reset(self):
        
        if self._deque :
            self._deque.clear()

    def run(self):

        while self._deque and not self._cancellationToken.wait(self._frequency):
            self._produce()

            if not self._deque:
                self._reset()

    def _produce(self):
        v = self._deque.popleft()
        self._consumer((v, self._producer(v)))
