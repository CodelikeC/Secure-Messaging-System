"""
replay protection cache 
"""

from collections import deque 

from shared.constants import NONCE_CACHE_SIZE 

class ReplayCache: 
    def __init__(self): 
        self.cache = set() 
        self.queue = deque() 
    def contains(self, nonce: str): 
        return nonce in self.cache 
    def add(self, nonce: str): 
        if nonce in self.cache: 
            return self.cache.add(nonce) 
        self.queue.append(nonce) 
        if len(self.queue) > NONCE_CACHE_SIZE: 
            oldest = self.queue.popleft() 
            self.cache.remove(oldest)