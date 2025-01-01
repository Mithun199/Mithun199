import unittest
from src.SadanandaCustomList import *

class TestCaseSadanandaList:
    """
        This class is created just to have different combinations of list items for SadanandaList Class
    """
    def __init__(self):
        self.s1 = SadanandaList([])
        self.s2 = SadanandaList([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.s3 = SadanandaList([[]])
        self.s4 = SadanandaList([[1, 2, 3, 4], ['c', 'k', 'n'], {1: 32, 2: 85, 3: 56, 4: 0, 5: 51}, {'a', 'b', 'c', 'd', 'x', 'y', 'z'}])
        self.s5 = SadanandaList([[1, 2, 3, 4,[1,2,3,4,5,{1,2,3,4}]], ['c', 'k', 'n',{'a':100, 'b':200}], {1: 32, 2: 85, 3: 56, 4: 0, 5: 51}, {'a', 'b', 'c', 'd', 'x', 'y', 'z'}])
        self.s6 = SadanandaList([lambda x: len(x), lambda y: sum(y), lambda z: min(z), lambda m: max(m)])
        self.s7 = SadanandaList([[1, 2, 3, 4, 5, 6, 7, 8, 9], [32, 85], [44, 55,66,77,777],['c', 'k', 'n']])
        self.s8 = SadanandaList([{1, 2, 3, 4, 5, 6, 7, 8, 9}, {32, 85}, {44, 55, 66, 77, 777}, {'c', 'k', 'n'}])

class TestCaseList:
    """
        This class is created just to have different combinations of list items of python built-in
    """
    def __init__(self):
        self.l1 = list([])
        self.l2 = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.l3 = list([[]])
        self.l4 = list([[1, 2, 3, 4], ['c', 'k', 'n'], {1: 32, 2: 85, 3: 56, 4: 0, 5: 51}, {'a', 'b', 'c', 'd', 'x', 'y', 'z'}])
        self.l5 = list([[1, 2, 3, 4,[1,2,3,4,5,{1,2,3,4}]], ['c', 'k', 'n',{'a':100, 'b':200}], {1: 32, 2: 85, 3: 56, 4: 0, 5: 51}, {'a', 'b', 'c', 'd', 'x', 'y', 'z'}])
        self.l6 = [lambda x: len(x), lambda y: sum(y), lambda z: min(z), lambda m: max(m)]
        self.l7 = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [32, 85], [44, 55, 66, 77, 777], ['c', 'k', 'n']]
        self.l8 = [{1, 2, 3, 4, 5, 6, 7, 8, 9}, {32, 85}, {44, 55, 66, 77, 777}, {'c', 'k', 'n'}]

class TestCase(unittest.TestCase):
    """
        Different combinations to test len method for SadanandaList Class
    """
    def test_len(self):
        s_len = TestCaseSadanandaList()
        l_len = TestCaseList()
        self.assertEqual(len(s_len.s1), len(l_len.l1))  # add assertion here
        self.assertEqual(len(s_len.s2), len(l_len.l2))  # add assertion here
        self.assertEqual(len(s_len.s3), len(l_len.l3))  # add assertion here
        self.assertEqual(len(s_len.s4), len(l_len.l4))  # add assertion here
        self.assertEqual(len(s_len.s5), len(l_len.l5))  # add assertion here
        self.assertEqual(len(s_len.s6), len(l_len.l6))  # add assertion here

    def test_clear(self):
        """
            Different combinations to test clear method for SadanandaList Class
        """
        s_clear = TestCaseSadanandaList()
        l_clear = TestCaseList()
        self.assertEqual(s_clear.s1.clear(), l_clear.l1.clear())  # add assertion here
        self.assertEqual(s_clear.s2.clear(), l_clear.l2.clear())  # add assertion here
        self.assertEqual(s_clear.s3.clear(), l_clear.l3.clear())  # add assertion here
        self.assertEqual(s_clear.s4.clear(), l_clear.l4.clear())  # add assertion here
        self.assertEqual(s_clear.s5.clear(), l_clear.l5.clear())  # add assertion here
        self.assertEqual(s_clear.s6.clear(), l_clear.l6.clear())  # add assertion here

    def test_pop(self):
        """
            Different combinations to test pop method for SadanandaList Class
        """
        s_pop = TestCaseSadanandaList()
        l_pop = TestCaseList()

        try:
            s_pop.s1.pop()  # add assertion here
            assert False ### to explicitly fail if exception is not raised
        except IndexError:
            pass

        try:
            s_pop.s2.pop(100)
            assert False
        except IndexError:
            pass

        self.assertEqual(s_pop.s2.pop(-1), l_pop.l2.pop(-1))
        self.assertEqual(s_pop.s2.pop(-3), l_pop.l2.pop(-3))

        try:
            s_pop.s2.pop(-300)
            assert False
        except IndexError:
            pass

        self.assertEqual(s_pop.s3.pop(), l_pop.l3.pop())  # add assertion here
        self.assertEqual(s_pop.s4.pop(), l_pop.l4.pop())  # add assertion here
        self.assertEqual(s_pop.s5.pop(), l_pop.l5.pop())  # add assertion here
        self.assertEqual(s_pop.s6.pop()(s_pop.s2), l_pop.l6.pop()(l_pop.l2))  # add assertion here

    def test_sort(self):
        """
            Different combinations to test sort method for SadanandaList Class
        """
        s_sort = TestCaseSadanandaList()
        l_sort = TestCaseList()
        self.assertEqual(s_sort.s1.sort(), l_sort.l1.sort())  # add assertion here
        self.assertEqual(s_sort.s2.sort(), l_sort.l2.sort())  # add assertion here
        self.assertEqual(s_sort.s3.sort(), l_sort.l3.sort())  # add assertion here
        try:
            self.assertEqual(s_sort.s4.sort(), l_sort.l4.sort())  # add assertion here
            False
        except TypeError:
            pass
        try:
            self.assertEqual(s_sort.s5.sort(), l_sort.l5.sort())  # add assertion here
            False
        except TypeError:
            pass
        try:
            self.assertEqual(s_sort.s6.sort(), l_sort.l6.sort())  # add assertion here
            False
        except TypeError:
            pass
        try:
            self.assertEqual(s_sort.s7.sort(), l_sort.l7.sort())  # add assertion here
            False
        except TypeError:
            pass
        self.assertEqual(s_sort.s8.sort(), l_sort.l8.sort())  # add assertion here

    def test_reverse(self):
        """
            Different combinations to test reverse method for SadanandaList Class
        """
        s_reverse = TestCaseSadanandaList()
        l_reverse = TestCaseList()

        s_reverse.s1.reverse()
        l_reverse.l1.reverse()
        self.assertEqual(s_reverse.s1.array, l_reverse.l1)  # add assertion here
        s_reverse.s2.reverse()
        l_reverse.l2.reverse()
        self.assertEqual(s_reverse.s2.array, l_reverse.l2)  # add assertion here
        s_reverse.s3.reverse()
        l_reverse.l3.reverse()
        self.assertEqual(s_reverse.s3.array, l_reverse.l3)  # add assertion here
        s_reverse.s4.reverse()
        l_reverse.l4.reverse()
        self.assertEqual(s_reverse.s4.array, l_reverse.l4)  # add assertion here
        s_reverse.s5.reverse()
        l_reverse.l5.reverse()
        self.assertEqual(s_reverse.s5.array, l_reverse.l5)  # add assertion here

      ### functions when reversed can't be compared as it address differs
      #  s_len.s6.reverse()
      #  l_len.l6.reverse()
      #  self.assertEqual(s_len.s6.array, l_len.l6)  # add assertion here

        s_reverse.s7.reverse()
        l_reverse.l7.reverse()
        self.assertEqual(s_reverse.s7.array, l_reverse.l7)
        s_reverse.s8.reverse()
        l_reverse.l8.reverse()
        self.assertEqual(s_reverse.s8.array, l_reverse.l8)

    def test_count(self):
        """
            Different combinations to test count method for SadanandaList Class
        """
        s_count = TestCaseSadanandaList()
        l_count = TestCaseList()

        self.assertEqual(s_count.s1.count(9), l_count.l1.count(9))  # add assertion here
        self.assertEqual(s_count.s2.count(9), l_count.l2.count(9))  # add assertion here
        self.assertEqual(s_count.s3.count(85), l_count.l3.count(85))  # add assertion here
        self.assertEqual(s_count.s3.count(['c', 'k', 'n']), l_count.l3.count(['c', 'k', 'n']))  # add assertion here
        self.assertEqual(s_count.s4.count({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}), l_count.l5.count({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}))  # add assertion here
        self.assertEqual(s_count.s5.count({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}), l_count.l5.count({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}))  # add assertion here
        #  s_len.s6.reverse()
        #  l_len.l6.reverse()
        #  self.assertEqual(s_len.s6.array, l_len.l6)

        self.assertEqual(s_count.s7.count([32, 85]), l_count.l7.count([32, 85]))
        self.assertEqual(s_count.s8.count({32, 85}), l_count.l8.count({32, 85}))

    def test_index(self):
        """
            Different combinations to test index method for SadanandaList Class
        """
        s_len = TestCaseSadanandaList()
        l_len = TestCaseList()

        try:
            self.assertEqual(s_len.s1.index(9), l_len.l1.index(9))  # add assertion here
            False
        except ValueError:
            pass
        self.assertEqual(s_len.s2.index(9), l_len.l2.index(9))  # add assertion here
        self.assertEqual(s_len.s3.index([]), l_len.l3.index([]))  # add assertion here
        self.assertEqual(s_len.s4.index(['c', 'k', 'n']), l_len.l4.index(['c', 'k', 'n']))  # add assertion here
        self.assertEqual(s_len.s4.index({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}), l_len.l5.index({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}))  # add assertion here
        self.assertEqual(s_len.s5.index({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}), l_len.l5.index({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}))  # add assertion here
        #  s_len.s6.reverse()
        #  l_len.l6.reverse()
        #  self.assertEqual(s_len.s6.array, l_len.l6)

        self.assertEqual(s_len.s7.index([32, 85]), l_len.l7.index([32, 85]))
        self.assertEqual(s_len.s8.index({32, 85}), l_len.l8.index({32, 85}))

    def test_where(self):
        """
            Different combinations to test where method for SadanandaList Class
        """
        s_where = TestCaseSadanandaList()
        l_where = TestCaseList()
        try:
            self.assertEqual(s_where.s1.index(9), l_where.l1.index(9))  # add assertion here
            False
        except ValueError:
            pass
        self.assertEqual(s_where.s2.index(9), l_where.l2.index(9))  # add assertion here
        self.assertEqual(s_where.s3.index([]), l_where.l3.index([]))  # add assertion here
        self.assertEqual(s_where.s4.index(['c', 'k', 'n']), l_where.l4.index(['c', 'k', 'n']))  # add assertion here
        self.assertEqual(s_where.s4.index({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}), l_where.l5.index({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}))  # add assertion here
        self.assertEqual(s_where.s5.index({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}), l_where.l5.index({1: 32, 2: 85, 3: 56, 4: 0, 5: 51}))  # add assertion here

        #  s_len.s6.reverse()
        #  l_len.l6.reverse()
        #  self.assertEqual(s_len.s6.array, l_len.l6)

        self.assertEqual(s_where.s7.index([32, 85]), l_where.l7.index([32, 85]))
        self.assertEqual(s_where.s8.index({32, 85}), l_where.l8.index({32, 85}))

    # append
    def test_append(self):
        """
            Different combinations to test append method for SadanandaList Class
        """
        s_append = TestCaseSadanandaList()
        l_append = TestCaseList()

        s_append.s1.append([])
        l_append.l1.append([])
        self.assertEqual(s_append.s1.array, l_append.l1)

        s_append.s2.append([1, 2])
        l_append.l2.append([1, 2])
        self.assertEqual(s_append.s2.array, l_append.l2)

        s_append.s3.append([{1, 2, 3}, {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 7: 8, 8: 9}])
        l_append.l3.append([{1, 2, 3}, {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 7: 8, 8: 9}])
        self.assertEqual(s_append.s3.array, l_append.l3)

        s_append.s4.append([(1, 2, 3, 4, 5), {1, 2, 3, 'c', 'k', 'n', 's', 'a', 'd', 'a', 'n', 'a', 'n'}])
        l_append.l4.append([(1, 2, 3, 4, 5), {1, 2, 3, 'c', 'k', 'n', 's', 'a', 'd', 'a', 'n', 'a', 'n'}])
        self.assertEqual(s_append.s4.array, l_append.l4)

        s_append.s5.append([[[[]]]])
        l_append.l5.append([[[[]]]])
        self.assertEqual(s_append.s5.array, l_append.l5)

        s_append.s7.append([[], {}, ()])
        l_append.l7.append([[], {}, ()])
        self.assertEqual(s_append.s7.array, l_append.l7)

        s_append.s8.append([0])
        s_append.s8.append([False])
        s_append.s8.append([None])
        s_append.s8.append([()])
        s_append.s8.append([{}])

        l_append.l8.append([0])
        l_append.l8.append([False])
        l_append.l8.append([None])
        l_append.l8.append([()])
        l_append.l8.append([{}])
        self.assertEqual(s_append.s8.array, l_append.l8)

    ## extend
    def test_extend(self):
        """
            Different combinations to test extend method for SadanandaList Class
        """
        s_extend = TestCaseSadanandaList()
        l_extend = TestCaseList()

        with self.assertRaises(TypeError):
            s_extend.s1.extend(0)

        s_extend.s2.extend({1:32,3:54})
        l_extend.l2.extend({1:32,3:54})
        self.assertEqual(s_extend.s2.array, l_extend.l2)

        s_extend.s2.extend({4: 43, 5: 875})
        l_extend.l2.extend({4: 43, 5: 875})
        self.assertEqual(s_extend.s2.array, l_extend.l2)

        s_extend.s3.extend([1, 2, 3, 4])
        l_extend.l3.extend([1, 2, 3, 4])

        s_extend.s4.extend((1, 2, 3, 4))
        l_extend.l4.extend((1, 2, 3, 4))
        self.assertEqual(s_extend.s4.array, l_extend.l4)

        s_extend.s5.extend((3, 4, 5, 6))
        l_extend.l5.extend((3, 4, 5, 6))
        self.assertEqual(s_extend.s5.array, l_extend.l5)

        s_extend.s5.extend({1, 2, 3, 4})
        l_extend.l5.extend({1, 2, 3, 4})
        self.assertEqual(s_extend.s5.array, l_extend.l5)

        s_extend.s7.extend([32, 85])
        l_extend.l7.extend([32, 85])
        self.assertEqual(s_extend.s7.array, l_extend.l7)

        s_extend.s7.extend({32, 85})
        l_extend.l7.extend({32, 85})
        self.assertEqual(s_extend.s7.array, l_extend.l7)

        s_extend.s8.extend([32, 85])
        l_extend.l8.extend([32, 85])
        self.assertEqual(s_extend.s8.array, l_extend.l8)

    ## test for dunder methods.
    ## __iter__
    def test_iter(self):
        """
            dunder method __iter__
            Different combinations to test __iter__ method for SadanandaList Class
        """
        s_iter = TestCaseSadanandaList()
        l_iter = TestCaseList()

        l1 = list(zip(s_iter.s1, l_iter.l1))
        l2 = list(zip(s_iter.s2, l_iter.l2))
        l3 = list(zip(s_iter.s3, l_iter.l3))
        l4 = list(zip(s_iter.s4, l_iter.l4))
        l5 = list(zip(s_iter.s5, l_iter.l5))
        l7 = list(zip(s_iter.s7, l_iter.l7))
        l8 = list(zip(s_iter.s8, l_iter.l8))

        for s, l in l1:
            self.assertEqual(s,l)
        for s, l in l2:
            self.assertEqual(s, l)
        for s, l in l3:
            self.assertEqual(s, l)
        for s, l in l4:
            self.assertEqual(s, l)
        for s, l in l5:
            self.assertEqual(s, l)
        for s, l in l7:
            self.assertEqual(s, l)
        for s, l in l8:
            self.assertEqual(s, l)

    ## __add__
    def test_add(self):
        """
            dunder method __add__
            Different combinations to test __add__ method for SadanandaList Class
        """
        s_add = TestCaseSadanandaList()
        l_len = TestCaseList()

        with self.assertRaises(TypeError):
            s_add.s1 = s_add.s1 + s_add.s1

        s_add.s2 = s_add.s2 + [1,2,3,4,5]
        l_len.l2 = l_len.l2 + [1,2,3,4,5]
        self.assertEqual(s_add.s2.array, l_len.l2)

        with self.assertRaises(TypeError):
            s_add.s3 = s_add.s3 + {1,2,3,4}

        with self.assertRaises(TypeError):
            s_add.s4 = s_add.s4 + {1: 32, 2: 85}

        with self.assertRaises(TypeError):
            s_add.s4 = s_add.s4 + (1, 32, 2, 85)

        with self.assertRaises(TypeError):
            s_add.s4 = s_add.s4 + 3285

        with self.assertRaises(TypeError):
            s_add.s4 = s_add.s4 + 'sadananda maharaj'

    # dunder __iadd__
    def test_iadd(self):
        """
            dunder method __iadd__
            Different combinations to test __iadd__ method for SadanandaList Class
        """
        s_idd = TestCaseSadanandaList()
        l_idd = TestCaseList()

        s_idd.s1 += [1, 2, 3, 4, 5]
        l_idd.l1 += [1, 2, 3, 4, 5]
        self.assertEqual(s_idd.s1.array, l_idd.l1)

        s_idd.s2 += {1, 2, 3, 4}
        l_idd.l2 += {1, 2, 3, 4}
        self.assertEqual(s_idd.s2.array, l_idd.l2)

        s_idd.s3 += {1: 32, 2: 85}
        l_idd.l3 += {1: 32, 2: 85}
        self.assertEqual(s_idd.s3.array, l_idd.l3)

        l_idd.l4 += (1, 32, 2, 85)
        s_idd.s4 += (1, 32, 2, 85)
        self.assertEqual(s_idd.s4.array, l_idd.l4)

        #s_len.s3 = s_len.s4 + 3285
        #s_len.s4 = s_len.s4 + 'sadananda maharaj'

    ## dunder __mul__
    def test_mul(self):
        """
            dunder method __mul__
            Different combinations to test __mul__ method for SadanandaList Class
        """
        s_mul = TestCaseSadanandaList()
        l_mul = TestCaseList()

        s_mul.s1 = s_mul.s1 * 3
        l_mul.s1 = l_mul.l1 * 3
        self.assertEqual(s_mul.s1.array, l_mul.l1)

        s_mul.s2 = s_mul.s2 * 3
        l_mul.l2 = l_mul.l2 * 3
        self.assertEqual(s_mul.s2.array, l_mul.l2)

        s_mul.s3 = s_mul.s3 * 3
        l_mul.l3 = l_mul.l3 * 3
        self.assertEqual(s_mul.s3.array, l_mul.l3)

        s_mul.s4 = s_mul.s4 * 3
        l_mul.l4 = l_mul.l4 * 3
        self.assertEqual(s_mul.s4.array, l_mul.l4)

        s_mul.s5 = s_mul.s5 * 3
        l_mul.l5 = l_mul.l5 * 3
        self.assertEqual(s_mul.s5.array, l_mul.l5)

        s_mul.s7 = s_mul.s7 * 3
        l_mul.l7 = l_mul.l7 * 3
        self.assertEqual(s_mul.s7.array, l_mul.l7)

        s_mul.s8 = s_mul.s8 * 3
        l_mul.l8 = l_mul.l8 * 3
        self.assertEqual(s_mul.s8.array, l_mul.l8)

    ## dunder __imul__
    def test_imul(self):
        """
            dunder method __imul__
            Different combinations to test __imul__ method for SadanandaList Class
        """
        s_imul = TestCaseSadanandaList()
        l_imul = TestCaseList()

        with self.assertRaises(TypeError):
            s_imul.s1 *= [1, 2, 3, 4, 5]

        with self.assertRaises(TypeError):
            s_imul.s2 *= {1, 2, 3, 4}

        with self.assertRaises(TypeError):
            s_imul.s4 *= (1, 2, 3, 4)

        with self.assertRaises(TypeError):
            s_imul.s5 *= {1: 32, 2: 85}

        s_imul.s1 *= 3
        l_imul.l1 *= 3
        self.assertEqual(s_imul.s1.array, l_imul.l1)

        s_imul.s2 *= 2
        l_imul.l2 *= 2
        self.assertEqual(s_imul.s2.array, l_imul.l2)

        s_imul.s3 *= 3
        l_imul.l3 *= 3
        self.assertEqual(s_imul.s3.array, l_imul.l3)

        s_imul.s3 *= 4
        l_imul.l3 *= 4
        self.assertEqual(s_imul.s3.array, l_imul.l3)

        s_imul.s4 *= 5
        l_imul.l4 *= 5
        self.assertEqual(s_imul.s4.array, l_imul.l4)

        s_imul.s5 *= 12
        l_imul.l5 *= 12
        self.assertEqual(s_imul.s5.array, l_imul.l5)

        s_imul.s7 *= 60
        l_imul.l7 *= 60
        self.assertEqual(s_imul.s7.array, l_imul.l7)

        s_imul.s8 *= 100
        l_imul.l8 *= 100
        self.assertEqual(s_imul.s8.array, l_imul.l8)

    ## dunder __eq__
    def test_eq(self):
        """
            dunder method __eq__
            Different combinations to test __eq__ method for SadanandaList Class
        """
        s_eq = TestCaseSadanandaList()
        l_eq = TestCaseList()

        self.assertEqual(s_eq.s1.array, l_eq.l1)
        self.assertEqual(s_eq.s2.array, l_eq.l2)
        self.assertEqual(s_eq.s3.array, l_eq.l3)
        self.assertEqual(s_eq.s4.array, l_eq.l4)
        self.assertEqual(s_eq.s5.array, l_eq.l5)
        self.assertEqual(s_eq.s7.array, l_eq.l7)
        self.assertEqual(s_eq.s8.array, l_eq.l8)
        self.assertNotEqual(s_eq.s8.array, l_eq.l3)


    ## dunder __contains__
    def test_contains(self):
        """
            dunder method __contains__
            Different combinations to test __contains__ method for SadanandaList Class
        """
        s_contains = TestCaseSadanandaList()

        bool_True = True
        bool_False = False

        self.assertEqual(1 in s_contains.s1.array, bool_False)
        self.assertEqual(9 in s_contains.s2.array, bool_True)
        self.assertEqual(0 in s_contains.s2.array, bool_False)
        self.assertEqual(9 in s_contains.s3.array, bool_False)
        self.assertEqual(0 in s_contains.s3.array, bool_False)

        self.assertEqual({'a', 'b', 'c', 'd', 'x', 'y', 'z'} in s_contains.s4.array, bool_True)
        self.assertEqual(['c', 'k', 'n'] in s_contains.s4.array, bool_True)
        self.assertEqual([[1, 2, 3, 4], ['c', 'k', 'n']] in s_contains.s4.array, bool_False)

        self.assertEqual({'a': 100, 'b': 200} in s_contains.s5.array, bool_False)
        self.assertEqual({'a', 'b', 'c', 'd', 'x', 'y', 'z'} in s_contains.s5.array, bool_True)
        self.assertEqual([1, 2, 3, 4,[1,2,3,4,5,{1,2,3,4}]] in s_contains.s5.array, bool_True)
        self.assertEqual([1, 2, 3, 4, [1, 2, 3, 4, 5, {1, 2, 3, 4}]] in s_contains.s5.array, bool_True)

        self.assertEqual([44, 55,66,77,777] in s_contains.s7.array, bool_True)
        self.assertEqual([32, 85] in s_contains.s7.array, bool_True)

        self.assertEqual({32, 85} in s_contains.s8.array, bool_True)
        self.assertEqual({32, 9} in s_contains.s8.array, bool_False)
        self.assertEqual({'c', 'k', 'n'} in s_contains.s8.array, bool_True)

    ## __getitem__
    def test_getitem(self):
        """
            dunder method __getitem__
            Different combinations to test __getitem__ method for SadanandaList Class
        """
        s_getiem = TestCaseSadanandaList()
        l_getitem = TestCaseList()

        with self.assertRaises(IndexError):
            s_getiem.s1[0]
        self.assertEqual(s_getiem.s2[2], l_getitem.l2[2])
        self.assertEqual(s_getiem.s2[5], l_getitem.l2[5])
        self.assertEqual(s_getiem.s3[0], l_getitem.l3[0])
        self.assertEqual(s_getiem.s4[1], l_getitem.l4[1])
        self.assertEqual(s_getiem.s5[1][2], l_getitem.l5[1][2])
        self.assertEqual(s_getiem.s5[1][3], l_getitem.l5[1][3])
        self.assertEqual(s_getiem.s7[1], l_getitem.l7[1])
        self.assertEqual(s_getiem.s8[2], l_getitem.l8[2])

    ## __setitem__
    def test_setitem(self):
        """
            dunder method __setitem__
            Different combinations to test __setitem__ method for SadanandaList Class
        """
        s_setiem = TestCaseSadanandaList()
        l_setitem = TestCaseList()

        with self.assertRaises(IndexError):
            s_setiem.s1[0] = 0

        s_setiem.s2[2] = 3
        l_setitem.l2[2] = 3
        self.assertEqual(s_setiem.s2.array, l_setitem.l2)

        s_setiem.s2[5] = {4:43,5:875}
        l_setitem.l2[5] = {4:43,5:875}

        with self.assertRaises(IndexError):
            s_setiem.s3[2] =[1,2,3,4]

        s_setiem.s4[1] = (1,2,3,4)
        l_setitem.l4[1] = (1,2,3,4)
        self.assertEqual(s_setiem.s4.array,l_setitem.l4)

        s_setiem.s5[1][0] = (3,4,5,6)
        l_setitem.l5[1][0] = (3,4,5,6)
        self.assertEqual(s_setiem.s5.array, l_setitem.l5)

        s_setiem.s5[1] = {1,2,3,4}
        l_setitem.l5[1] = {1,2,3,4}
        self.assertEqual(s_setiem.s2.array,l_setitem.l2)

        s_setiem.s7[1] = {32, 85}
        l_setitem.l7[1] = {32, 85}
        self.assertEqual(s_setiem.s2.array,l_setitem.l2)

        s_setiem.s7[1:1] = {32, 85}
        l_setitem.l7[1:1] = {32, 85}
        self.assertEqual(s_setiem.s2.array, l_setitem.l2)

        s_setiem.s8[2:2] = [32, 85]
        l_setitem.l8[2:2] = [32, 85]
        self.assertEqual(s_setiem.s2.array,l_setitem.l2)


    ## dunder __bool__
    def test_bool(self):
        """
            dunder method __bool__
            Different combinations to test __bool__ method for SadanandaList Class
        """
        s_bool = TestCaseSadanandaList()
        l_bool = TestCaseList()

        self.assertEqual(bool(s_bool.s1), bool(l_bool.l1))
        self.assertEqual(bool(s_bool.s2), bool(l_bool.l2))
        self.assertEqual(bool(s_bool.s3), bool(l_bool.l3))
        self.assertEqual(bool(s_bool.s4), bool(l_bool.l4))
        self.assertEqual(bool(s_bool.s5), bool(l_bool.l5))
        self.assertEqual(bool(s_bool.s6), bool(l_bool.l6))
        self.assertEqual(bool(s_bool.s7), bool(l_bool.l7))
        self.assertEqual(bool(s_bool.s8), bool(l_bool.l8))

    ## dunder __hash__
    def test_hash(self):
        """
            dunder method __hash__
            Different combinations to test __hash__ method for SadanandaList Class
        """
        s_hash = TestCaseSadanandaList()

        with self.assertRaises(TypeError):
            hash(s_hash.s1)

        with self.assertRaises(TypeError):
            hash(s_hash.s2)

        with self.assertRaises(TypeError):
            hash(s_hash.s3)

        with self.assertRaises(TypeError):
            hash(s_hash.s4)

        with self.assertRaises(TypeError):
            hash(s_hash.s5)

        with self.assertRaises(TypeError):
            hash(s_hash.s6)

        with self.assertRaises(TypeError):
            hash(s_hash.s7)

        with self.assertRaises(TypeError):
            hash(s_hash.s8)

## dunder __lt__
    def test_lt(self):
        """
            dunder method __lt__
            Different combinations to test __lt__ method for SadanandaList Class
        """
        s1 = SadanandaList([1, 2, 3, 4, 5])
        s2 = SadanandaList([1, 2, 3, 4, 5])
        l1 = [1, 2, 3, 4, (1, 2, 3, 4)]
        l2 = [1, 2, 3, 4, (1, 2, 3, 4)]
        self.assertEqual(s1<s2 , l1<l2)

        s1 = SadanandaList([1, 2, 3, 4, 5])
        s2 = SadanandaList([1, 2, 3, 4, 'a'])
        with self.assertRaises(TypeError):
            s1<s2

        s1 = SadanandaList([1, 2, 3, 4, (1, 2, 3, 4)])
        s2 = SadanandaList([1, 2, 3, 4, (1, 2, 3, 4)])
        l1 = [1, 2, 3, 4, (1, 2, 3, 4)]
        l2 = [1, 2, 3, 4, (1, 2, 3, 4)]
        self.assertEqual(s1<s2, l1<l2)

        s1 = SadanandaList([1, 2, 3, 4, ('a', 2, 3, 4)])
        s2 = SadanandaList([1, 2, 3, 4, (1, 2, 3, 4)])
        with self.assertRaises(TypeError):
            s1<s2

        s1 = SadanandaList([1, 2, 3, 4, (1, 2, 3, 4)])
        s2 = SadanandaList([1, 2, 3, 4, (1, 2, 3, 5)])
        l1 = SadanandaList([1, 2, 3, 4, (1, 2, 3, 4)])
        l2 = SadanandaList([1, 2, 3, 4, (1, 2, 3, 5)])
        self.assertEqual(s1<s2, l1<l2)

        s1 = SadanandaList([1, 2, 3, 4, {1: 32, 2: 85}])
        s2 = SadanandaList([1, 2, 3, 4, {1: 32, 2: 85}])
        with self.assertRaises(TypeError):
            s1<s2

        s1 = SadanandaList([1, 2, 3, 4, {1, 8, 3, 4}])
        s2 = SadanandaList([1, 2, 3, 4, {1, 2, 3, 5}])
        l1 = [1, 2, 3, 4, {1, 8, 3, 4}]
        l2 = [1, 2, 3, 4, {1, 2, 3, 5}]
        self.assertEqual(s1 < s2, l1 < l2)
        self.assertEqual(s1 > s2, l1 > l2)

        s1 = SadanandaList([1, 2, 3, 4, 15])
        s2 = SadanandaList([1, 2, 3, 4, 5])
        l1 = [1, 2, 3, 4, 15]
        l2 = [1, 2, 3, 4, 5]

        self.assertEqual(s1 < s2, l1 < l2)
        self.assertEqual(s1 > s2, l1 > l2)

if __name__ == '__main__':
    unittest.main()
