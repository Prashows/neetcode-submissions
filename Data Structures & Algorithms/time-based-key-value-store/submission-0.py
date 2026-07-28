class TimeMap:
    def __init__(self):
        # Dictionary mapping key -> list of (timestamp, value) tuples
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Timestamps are strictly increasing, so appending keeps the list sorted
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        left = 0
        right = len(pairs) - 1
        result = ""
        
        # Binary Search for the largest timestamp <= target timestamp
        while left <= right:
            mid = (left + right) // 2
            mid_time, mid_value = pairs[mid]
            
            if mid_time == timestamp:
                return mid_value # Exact match found!
            
            elif mid_time < timestamp:
                # This is a valid candidate, but there might be a larger one
                result = mid_value 
                left = mid + 1   # Search the right half for a closer match
                
            else:
                # mid_time > timestamp, this is too far in the future
                right = mid - 1  # Search the left half
                
        return result