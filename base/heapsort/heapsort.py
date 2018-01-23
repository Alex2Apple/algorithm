
class Item():
    def __init__(self, value, loc):
        self.value = value
        self.loc = loc
        
    def __gt__(self, other):
        return self.value > other.value
        
    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return repr(self.value)

class Heap():
    def __init__(self, capacity, max = True):
        self.capacity = capacity
        self.max = max
        self.entry = []
    
    def build(self, source):
        if len(source) > self.capacity:
            raise("current capacity is {}, please reset the capacity using reset_capacity()", self.capacity)
        
        for index in range(len(source)):
            self.push(source[index])
    
    @property
    def size(self):
        return len(self.entry)
        
    def reset_capacity(self, new):
        self.capacity = new
    
    def up_adjust(self, index):
        if len(self.entry) == 0:
            return
            
        if index > self.capacity or index <= 0:
            return
        
        parent = int((index - 1) / 2)
        if (self.max == True and self.entry[index] > self.entry[parent]) or (self.max == False and self.entry[index] < self.entry[parent]):
            self.entry[parent], self.entry[index] = self.entry[index], self.entry[parent]
            self.up_adjust(parent)
        
        return
    
    def down_adjust(self, index):
        if len(self.entry) == 0:
            return
            
        if index < 0:
            return
        
        if len(self.entry) <= index * 2 + 1:
            return
            
        m_child = self.entry[index * 2 + 1]
        child = index * 2 + 1
        if len(self.entry) > (index  + 1) * 2:
            if (self.max == True and m_child < self.entry[(index + 1) * 2]) or (self.max == False and m_child > self.entry[(index + 1) * 2]):
                m_child = self.entry[(index + 1) * 2]
                child = (index + 1) * 2
        
        if (self.max == True and self.entry[index] < m_child) or (self.max == False and self.entry[index] > m_child):
            self.entry[child], self.entry[index] = self.entry[index], self.entry[child]
            self.down_adjust(child)
    
        return
    
    def push(self, item):
        if len(self.entry) >= self.capacity:
            raise("don't push more, it's enough")
        
        self.entry.append(item)
        self.up_adjust(len(self.entry) - 1)
        
    def pop(self):
        if len(self.entry) == 0:
            raise("can't pop more, it's empty")
        
        self.entry[len(self.entry) - 1], self.entry[0] = self.entry[0], self.entry[len(self.entry) - 1]
        value = self.entry.pop()
        self.down_adjust(0)
        return value
        
    def __repr__(self):
        return self.entry.__repr__()
       
def generator(*args):
    for i in range(len(args)):
        yield Item(args[i].pop(0), i)

def recursive_merge(input, **kwargs):
    val = [l for l in input if len(l) > 0]
    if len(val) == 0:
        while kwargs['sort'].size > 0:
            kwargs['out'].append(kwargs['sort'].pop())
        return

    item = kwargs['sort'].pop()
    kwargs['out'].append(item)
    if len(input[item.loc]) == 0:
        kwargs['sort'].push(Item(val[0].pop(0), 0))
    else:
        kwargs['sort'].push(Item(input[item.loc].pop(0), item.loc))
    recursive_merge(input, **kwargs)
    
    return
    
def iterate_merge(input, **kwargs):
    while len([l for l in input if len(l) > 0] ) > 0:
        item = kwargs['sort'].pop()
        kwargs['out'].append(item)
        if len(input[item.loc]) == 0:
            val = [l for l in input if len(l) > 0]
            kwargs['sort'].push(Item(val[0].pop(0), 0))
        else:
            kwargs['sort'].push(Item(input[item.loc].pop(0), item.loc))
        
    while kwargs['sort'].size > 0:
        kwargs['out'].append(kwargs['sort'].pop())
    return    
