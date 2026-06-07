class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = None
        self.tail = None        
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.put(key, None)
            return self.cache[key][1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if not self.cache:
            self.cache[key] = [None, value, None]
            self.head = key
            self.tail = key
            return
        
        if key in self.cache:
            if value is not None:
                self.cache[key][1] = value
            if key == self.head:
                return

            prevKey = self.cache[key][0]
            nextKey = self.cache[key][2]
            if prevKey is not None:
                self.cache[prevKey][2] = nextKey
            else:
                pass
            if nextKey is not None:
                self.cache[nextKey][0] = prevKey
            else:
                if prevKey is not None:
                    self.tail = prevKey
                else:
                    pass
        else:
            self.cache[key] = [None, value, self.head]

        if self.head is not None and self.head != key:
            self.cache[self.head][0] = key
            self.cache[key][0] = None
            self.cache[key][2] = self.head
        
        self.head = key

        if len(self.cache) > self.capacity:
            prevKey = self.cache[self.tail][0]
            if prevKey is not None:
                self.cache[prevKey][2] = None
            del self.cache[self.tail]
            self.tail = prevKey