# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from collections import MutableMapping


class MapBase(MutableMapping):
  """Our own abstract base class that includes a nonpublic _Item class."""

  #------------------------------- nested _Item class -------------------------------
  class _Item:
    """Lightweight composite to store key-value pairs as map items."""
    __slots__ = '_key', '_value'

    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __eq__(self, other):               
      return self._key == other._key   # compare items based on their keys

    def __ne__(self, other):
      return not (self == other)       # opposite of __eq__

    def __lt__(self, other):               
      return self._key < other._key    # compare items based on their keys

class HashMapBase(MapBase):
  """Abstract base class for map using hash-table with MAD compression.

  Keys must be hashable and non-None.
  """

  def __init__(self, cap=11, p=109345121):
    """Create an empty hash-table map.

    cap     initial table size (default 11)
    p       positive prime used for MAD (default 109345121)
    """
    self._table = cap * [ None ]
    self._n = 0                                   # number of entries in the map
    self._prime = p                               # prime for MAD compression
    self._scale = 1 + randrange(p-1)              # scale from 1 to p-1 for MAD
    self._shift = randrange(p)                    # shift from 0 to p-1 for MAD

  def _hash_function(self, k):
    return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

  def __len__(self):
    return self._n

  def __getitem__(self, k):
    j = self._hash_function(k)
    return self._bucket_getitem(j, k)             # may raise KeyError

  def __setitem__(self, k, v):
    j = self._hash_function(k)
    self._bucket_setitem(j, k, v)                 # subroutine maintains self._n
    if self._n > len(self._table) // 2:           # keep load factor <= 0.5
      self._resize(2 * len(self._table) - 1)      # number 2^x - 1 is often prime

  def __delitem__(self, k):
    j = self._hash_function(k)
    self._bucket_delitem(j, k)                    # may raise KeyError
    self._n -= 1

  def _resize(self, c):
    """Resize bucket array to capacity c and rehash all items."""
    old = list(self.items())       # use iteration to record existing items
    self._table = c * [None]       # then reset table to desired capacity
    self._n = 0                    # n recomputed during subsequent adds
    for (k,v) in old:
      self[k] = v                  # reinsert old key-value pair

      

class UnsortedTableMap(MapBase):
  """Map implementation using an unordered list."""

  def __init__(self):
    """Create an empty map."""
    self._table = []                              # list of _Item's
  
  def __getitem__(self, k):
    """Return value associated with key k (raise KeyError if not found)."""
    for item in self._table:
      if k == item._key:
        return item._value
    raise KeyError('Key Error: ' + repr(k))

  def __setitem__(self, k, v):
    """Assign value v to key k, overwriting existing value if present."""
    for item in self._table:
      if k == item._key:                          # Found a match:
        item._value = v                           # reassign value
        return                                    # and quit    
    # did not find match for key
    self._table.append(self._Item(k,v))

  def __delitem__(self, k):
    """Remove item associated with key k (raise KeyError if not found)."""
    for j in range(len(self._table)):
      if k == self._table[j]._key:                # Found a match:
        self._table.pop(j)                        # remove item
        return                                    # and quit    
    raise KeyError('Key Error: ' + repr(k))

  def __len__(self):
    """Return number of items in the map."""
    return len(self._table)

  def __iter__(self):                             
    """Generate iteration of the map's keys."""
    for item in self._table:
      yield item._key                             # yield the KEY



class ChainHashMap(HashMapBase):
  """Hash map implemented with separate chaining for collision resolution."""

  def _bucket_getitem(self, j, k):
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error: ' + repr(k))        # no match found
    return bucket[k]                                 # may raise KeyError

  def _bucket_setitem(self, j, k, v):
    if self._table[j] is None:
      self._table[j] = UnsortedTableMap()     # bucket is new to the table
    oldsize = len(self._table[j])
    self._table[j][k] = v
    if len(self._table[j]) > oldsize:         # key was new to the table
      self._n += 1                            # increase overall map size

  def _bucket_delitem(self, j, k):
    bucket = self._table[j]
    if bucket is None:
      raise KeyError('Key Error: ' + repr(k))        # no match found
    del bucket[k]                                    # may raise KeyError

  def __iter__(self):
    for bucket in self._table:
      if bucket is not None:                         # a nonempty slot
        for key in bucket:
          yield key
