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


class FaultedSensor(VirtualSensor):

    def __init__(self, deviceId, consumer, event, frequency=0.010, noise=10, verbose=False):
        """
            Create a new sensor that will simulate missing data. According to the 
            given noises param, it will randomly remove from sequence generation 
            N (which is randomly generated all along) consecutive value generated by the inner
            sensor.
        """
        VirtualSensor.__init__(self, deviceId, consumer, event, frequency)
        self._max_noise = noise
        self._n_counter = 0
        self._verbose = verbose
        self._cur_noise = self._rand_noise()

    def _produce(self):

        """"
            remove N consecutive sensor value depending
            the value of _cur_noise. This is simple 
            way to simulate missing data
        """
        if self._n_counter == self._cur_noise:
           
            VirtualSensor._produce(self)
            self._n_counter = 0
            self._cur_noise = self._rand_noise()
            self._log("sending sensor value")

        else:
            
            v = self._deque.popleft()
            self._log("ignoring sensor value")
            self._n_counter+=1

    def _rand_noise(self):
        """ 
            Generate a random integer for noise purpose
            this integer represent  the consecutive
            missing data that will occur from the next
            data production
        """
        noise  =  np.random.randint(1,self._max_noise+1)
        self._log("New noise : {0}".format(noise),1)
        
        return noise


    def _log(self,message,level=0):
        
        if self._verbose : 

            if level == 0:
                 print("[DBG] - {0}".format(message))
            elif level == 1:
                print("[INFO] - {0}".format(message))
            else:
                raise ValueError("Unknown level")



