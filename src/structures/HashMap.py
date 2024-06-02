class HashMap:
    def __init__(self, initial_capacity=1000):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def hash(self, key):
        
        return hash(key) % self.capacity

    def put(self, key, value):
        
        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity > 0.7:
            self._resize()

    def get(self, key):
       
        index = self.hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f'Key {key} not found')

    def remove(self, key):
        
        index = self.hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return

        raise KeyError(f'Key {key} not found')

    def _resize(self):
        """Resize the hash map when the load factor exceeds a threshold"""
        new_capacity = self.capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]

        for bucket in self.buckets:
            for key, value in bucket:
                index = hash(key) % new_capacity
                new_buckets[index].append((key, value))

        self.buckets = new_buckets
        self.capacity = new_capacity

    def __len__(self):
        
        return self.size

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False