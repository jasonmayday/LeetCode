'''
一个包含优先级元素的集合，这个集合允许插入任意的元素，并允许删除拥有最高优先级的元素。

“先进先出”（FIFO）的数据结构：队列（Queue）。

队列有一种变体叫做“优先队列”（Priority Queue）。优先队列的出队（Dequeue）操作和队列一样，都是从队首出队。

但在优先队列的内部，元素的次序却是由“优先级”来决定：高优先级的元素排在队首，而低优先级的元素则排在后面。

'''

class PriorityQueueBase:
  """Abstract base class for a priority queue."""

  #------------------------------ nested _Item class ------------------------------
  class _Item:
    """Lightweight composite to store priority queue items."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __lt__(self, other):
      return self._key < other._key    # compare items based on their keys

    def __repr__(self):
      return '({0},{1})'.format(self._key, self._value)

  #------------------------------ public behaviors ------------------------------
  def is_empty(self):                  # concrete method assuming abstract len
    """Return True if the priority queue is empty."""
    return len(self) == 0

  def __len__(self):
    """Return the number of items in the priority queue."""
    raise NotImplementedError('must be implemented by subclass')

  def add(self, key, value):
    """Add a key-value pair."""
    raise NotImplementedError('must be implemented by subclass')

  def min(self):
    """Return but do not remove (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    raise NotImplementedError('must be implemented by subclass')

  def remove_min(self):
    """Remove and return (k,v) tuple with minimum key.

    Raise Empty exception if empty.
    """
    raise NotImplementedError('must be implemented by subclass')


if __name__ == '__main__':
    P = PriorityQueueBase()
    P.add(5, A)