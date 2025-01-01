# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:23:14 2024
@author: Sadananda
"""

from typing import List, Any, Union

class SadanandaList:
    """
        A custom list class it uses list internally since dynamic array concept is not feasible in python
          -- we have to use [] to create empty array in other words it is an empty list 
        
        Args:
            array(list): empty list or non empty list is accepted
    
    """
    def __init__(self,array=[])->None:
        self.array = []
        
        if len(array):
            self._append(array)
    
    def __len__(self)->int:
        """
            Returns the length of the list
            
             Args: None
             
             Returns: int 
             
             Raises:None
        """
        return len(self.array)
    
    def __add__(self, other):
        
        """
            Dunder add method to add the list of similar type returns new list
            
            Args:
                other(SadanandaList): SadanandaList empty or non empty     
            Returns:
                SadanandaList: SadanandaList empty or non empty(new list in either of the case)
            Raises: 
                None
        """

        if not isinstance(other, list):
            raise TypeError(f'can only cancatenate list (not {type(other)}) to list')
        
        if len(other):    
            self._append(other)    
        return SadanandaList(self.array)
        
    def __iadd__(self,other):
        """
            Dunder add method to add the list of (tuple , dict, set, str,list, SadanandaList) type returns same list doesn't alter the memory pointing
            
            Args: 
                other(SadanandaList):SadanandaList empty or non empty                 
            Returns: 
                SadanandaList(self): empty or non empty((self) same list in either of the case)
            Raises: 
                TypeError if the other object which is passed is other than [tuple , dict, set, str,list, SadanandaList]
        """
        
        if not type(other) in [tuple , dict, set, str,list, SadanandaList]:
            raise TypeError("can only concatenae SadanandaList ->[list , tuple , dict, set, str, SadanandaList] ")
        
        if len(other):
            self._append(other)
            
        return self
    
    def __mul__(self, _times):
        
        """
            This will multiply the contents of the SadanandaList by number passed in _times and returns new SadanandaList
            
            Args:
                _times(int): The number of times the list has to be multiplied
            
            Return:
                (SadanandaList): New List
            
            Raises:
                TypeError in case of non integer input
        """
        
        if not isinstance(_times, int):
            raise TypeError(f'can not multiple sequence by non-int type {type(_times)}')
        
        data = self.array.copy()
        self.array.clear()

        for i in range(_times):
            self._append(data)
            
        return SadanandaList(self.array)
    
    def __imul__(self, times):

        """
            This will multiply the contents of the SadanandaList by number passed in _times and returns same SadanandaList(self)
            
            Args:
                times(int):The number of times the list has to be multiplied
            Return:
                (SadanandaList): Same List (id doesn't change)
            Raises:
                TypeError in case of non integer input
        """
        
        if not isinstance(times, int):
            raise TypeError(f"can't multiple sequence by non-int type {type(times)}")

        data = self.array.copy()
        self.array.clear()

        for i in range(times):
            self._append(data)
        return self

    def __repr__(self):
        """
            Will print the list contents on print function or returns the string
        
            Args: 
                None
            Returns:
                str: Returns entire list contents in string
            Raises:
                None
        """
        return str(self.array)
    
    def __getitem__(self, _slice_index:Union[slice , int])->Union[List[Any] , int]:
        
        """
            dunder __getitem__ this will return list or single element or empty list in a SadanandaList depending on input
                c = SadanandaList[32]
            
            Args:    
                _slice_index(slice/int): slice or int
            Returns:
                single item in a SadanandaList if int is passed as Args or new SadanandaList if slice is passed
            Raises:
                None
        """
        
        if isinstance(_slice_index,int):
            return self.array[_slice_index]
        
        if isinstance(_slice_index, slice):                    
            if  _slice_index.step == 0:
                raise ValueError('slice step cannot be zero')
            
            data = []
            data = self.array[_slice_index]
            return SadanandaList(data)
        
    def __setitem__(self, index, value):
        """
            dunder __setitem__ this will set new value in the index position passed as an arguement to this function
                SadanandaList[32] = 85
            Args:    
                _slice_index(slice/int): slice or int
            Returns:
                single item in a SadanandaList if args is of type int or new SadanandaList if slice is passed as args
            Raises:
                IndexError if arg value is < 0 i.e negative or > total length of the SadanandaList
        """
        
        if isinstance(index, int):
            if (len(self)==0) or (index>len(self)-1):
                raise IndexError('Index cannot exceed the existing length of SadanandaList')
            else:
                pass
        if isinstance(index, slice):
            if not (hasattr(value, '__iter__') or hasattr(value, '__getitem__')):
                raise TypeError(f'can only assign iterables {type(value)} not possible to assign')
            else:
                pass
        self.array[index] = value
    
    def __contains__(self, val):
        """
        dunder __contains__ will check whether the required item is present in the SadanandaList
        Args:
            val(int/tupe/dic/set/list/SadanandaList): the item to be iterated to check it's presense or absense
        Returns(bool): True if present, False if not
        Raises:
            None
        """
        
        for item in self.array:
            if type(val)==type(item) and val==item:
                return True
            continue
        return False

    def __bool__(self):
        """
            dunder __bool__ truthiness always depends on length

            Args:
                None
            Returns:
                None
            Raise:
                None
        """
        return len(self)>0
    
    def __eq__(self, other):
        
        """
        dunder __eq__ will check whether the required item is present in the SadanandaList
            example - (SadanandaList1==SadanandaList2)
        Args:
            other(SadanandaList): an different list to be compared with the self
        Returns(bool): True if both lists are equal, False if not
        Raises:
            None
        """

        if other is None:
            if self.array is None:
                return True
            else:
                return False

        if id(self)==id(other):
            return True

        if len(self)!=len(other):
            return False

        for index, item in enumerate(other):
            if item!=self.array[index]:
                return False
        return True
    
    def __lt__(self, other):
        
        """
        dunder __lt__ will compare element by element in the given list with other list
            example - (SadanandaList1()<SadanandaList2())
        Args:
            other(SadanandaList): an different list to be compared with the self
        Returns(bool): True if self i.e left operand is lesser than left operand, False if not
        Raises:
            TypeError
        """

        if not isinstance(other, SadanandaList):
            raise TypeError(f'< is not supported between the {type(other)} and {type}')

        if len(self)==0 and len(other)==0:
            return False
        if len(self)==0 and len(other)>0:
            return False

        length = min(len(self), len(other))
        result = False
        for index in range(length):
            if type(other[index])!=type(self.array[index]):
                raise TypeError(f'< is not supported between the {type(other[index])} and {type[self[index]]} in SadanandaList')

            if callable(other[index]):
                raise TypeError(f'< is not supported between the {type(other[index])} and {type[self[index]]} in SadanandaList')

            if isinstance(other[index], dict) and isinstance(self[index], dict):
                raise TypeError(f'< is not supported between the {type(other)} and {type[self[index]]} in SadanandaList')

            if self.array[index] == other[index]:
                result = not (self.array[index]==other[index])
                continue
            if  self.array[index] < other[index]:
                result =  self.array[index] < other[index]
                break
        return result

    '''
    def __gt__(self, other):

        """
        dunder __lt__ will compare element by element in the given list with other list
            example - (SadanandaList1()>SadanandaList2())
        Args:
            other(SadanandaList): an different list to be compared with the self
        Returns(bool): True if self i.e left operand is bigger than left operand, False if not
        Raises:
            TypeError
        """

        if not isinstance(other, SadanandaList):
            raise TypeError(f'< is not supported between the {type(other)} and {type}')

        if len(self) == 0 and len(other) == 0:
            return False
        if len(self) == 0 and len(other) > 0:
            return False

        length = min(len(self), len(other))
        result = False
        for index in range(length):
            if type(other[index]) != type(self.array[index]):
                raise TypeError(
                    f'< is not supported between the {type(other[index])} and {type[self[index]]} in SadanandaList')

            if callable(other[index]):
                raise TypeError(
                    f'< is not supported between the {type(other[index])} and {type[self[index]]} in SadanandaList')

            if isinstance(other[index], dict) and isinstance(self[index], dict):
                raise TypeError(
                    f'< is not supported between the {type(other)} and {type[self[index]]} in SadanandaList')

            print(self.array[index], other[index])
            if self.array[index] == other[index]:
                result = not (self.array[index] == other[index])
                continue
            if self.array[index] > other[index]:
                print('lesser', self.array[index], other[index])
                result = self.array[index] > other[index]
                break
        return result
        '''

    def __hash__(self):
        raise TypeError(f'unhashable type: {type(self)}')

    def extend(self,iterable):
        if not(hasattr(self, '__iter__') or hasattr(self, '__getitem__')):
            raise TypeError(f'Only iterables can be extended but not {type(iterable)}')
        for item in iterable:
            self.append(item)
    
    def __iter__(self):
        """
            dunder __iter__ to iterate through the items of list
            
            Args:
                None
            Returns:
                None
            Raise:
                None
        """
        
        return self.SadanandaListIterator(self)
    
    class SadanandaListIterator:
        """
            This is an Iterator to the SadanandaList
            This will iterate through all the elements in the SadanandaList
        
            Args:
                iterable(SadanandaList):only one list is allowed to be passed
        
        """
        
        def __init__(self,iterable):
            self.index = -1
            self.iterable = iterable
            self.length = len(self.iterable)-1
            
        def __iter__(self):
            """
                dunder __iter__ method which returns the instance to the iterable for iterating
                
                Args:
                    None
                Returns:
                    None
                Raises:
                    None
            """
            return self
        
        def __next__(self):
            """
                dunder __iter__ method which returns the instance to the iterable for iterating
                
                Args:
                    None
                Returns:
                    int/float/str/list/tuple/dic/set -- one after the other items present in the SadanandaList
                Raises:
                    StopIteration if the index exceeds the iteration
            """
            if self.index>=self.length:
                raise StopIteration('iterator exhaused')
            else:
                self.index+=1
                return self.iterable[self.index]
        
    def _append(self, other):
        """
            _append method which is used to iterate through the iterables and passes them one after the other to the append method
            
            Args:
                None
            Returns:
                None
            Raise:
                None
        """
        
        for item in other:
            self.append(item)
        
    def append(self, value):
        """
            append method which is used to append items one after the other to the SadanandaList
            
            Args:
                None
            Returns:
                None
            Raise:
                None
        """
        self.array.append(value)
    
    def clear(self):
        """
            To clear entire contents of SadanandaList
            
            Args:
                None
            Returns:
                None
            Raise:
                None
        """
        self.array.clear() 
    
    def pop(self, index:int=None)->int:
        """
            To pop the elements in the SadanandaList
            
            Args:
                index(int/None)
            Returns:
                n(int): the item @ the poped index
            Raises:
                IndexError - if the requested index is not valid
                TypeError - if the index type is not int
        """

        if  index is not None:
            if not isinstance(index, int):
                raise TypeError('TypeError: Index to the SadanandaList should be of integer')

            if abs(index) >= len(self):
                raise IndexError('IndexError: pop index out of range')

            return self.array.pop(index)

        if index is None:
            if len(self):
                return self.array.pop()
            if len(self)==0:
                raise IndexError('IndexError: pop index out of range')
    
    def sort(self):
        """
            To sort the elements in the SadanandaList
                sorting of SadanandaList is possible only when all the elements in a list are same type
            Args:
                None
            Returns:
                SadanandaList: i.e self which is the same list itself on which sort is performed
            Raieses:
                TypeError if the elements in the SadanandaList are not same
        """

        if len(self.array)>=1:
            item_type = SadanandaList
            for item in self.array:
                if item_type is SadanandaList:
                    item_type = type(item)
                    continue
                if isinstance(item_type, dict) or isinstance(item_type, set) or (item_type!=type(item)):
                    raise TypeError(f'< not supported between {item_type} {type(item)}')

            self.array = sorted(self.array)
                
    def reverse(self):
        """
            To reverse the elements in the SadanandaList
            
            Args:
                None
            Returns:
                None
            Raieses:
                None
        """
        length = len(self)//2
        right_index = len(self)-1

        if len(self)>1:
            for left_index in range(length):
                if right_index<=left_index:
                    break
                self.array[right_index], self.array[left_index] = \
                    self.array[left_index], self.array[right_index]
                right_index -= 1
    
    def count(self,item)->int:
        """
            To count the number of occurances of the given item in SadanandaList
            
            Args:
                item(str/int/dic/tuple/set/float/list): Any of the data type which are possible to be added to this SadanandaList
            Returns:
                (int): number of occurances of the item in the SadanandaList
            Raises:
                None
        """
        
        count = 0
        for _items in self.array:
            if type(item)==type(_items) and item==_items:
                count+=1
        return count
    
    def index(self,item)->int:
        """
            To collect the first indices where the given item in SadanandaList
            Args:
                item(str/int/dic/tuple/set/float/list): Any of the data type which are possible to be added to this SadanandaList
            Returns:
                (int): which contails  the first index of the item in the SadanandaList
            Raises:
                ValueError: if the requested item is not present in the SadanandaList
        """
        
        for index, _item in enumerate(self.array):
            if type(_item)==type(item) and _item==item:
                return index
            
        raise ValueError(f'requested {item} not present in list')
        
    def where(self, item)->[]:
        """
            To collect all the indices where the given item in SadanandaList
            
            Args:
                item(str/int/dic/tuple/set/float/list): Any of the data type which are possible to be added to this SadanandaList 
                
            Returns:
                indices(list): which contails all the indices of the item in the SadanandaList
                
            Raises:
                ValueError: if the requested item is not present in the SadanandaList
        
        """
        indices =  [index for index, _item in enumerate(self.array) if type(_item)==type(item) and _item==item]
        
        if bool(indices):
            return indices
        else:
            raise ValueError(f'requested {item} not present in list')
        
if __name__=='__main__':
    print('SadanandaList')