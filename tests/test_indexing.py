import unittest

import pandas.util.testing as pdt
import recordlinkage
import numpy as np
import pandas as pd

from recordlinkage import datasets

class TestIndexing(unittest.TestCase):

    def test_full_index_unique(self):

        df1 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=['001', '002', '003'])
        df2 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=['001', '002', '003'])

        index = recordlinkage.Pairs(df1, df2)
        pairs = index.full()

        index_exp = [('001', '001'), ('001', '002'), ('001', '003'), ('002', '001'), ('002', '002'), ('002', '003'), ('003', '001'), ('003', '002'), ('003', '003')]

        # Check if index is unique
        self.assertTrue(pairs.index.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), len(df1)*len(df2))

    def test_block_index_unique(self):

        df1 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=['001', '002', '003'])
        df2 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=['001', '002', '003'])

        index = recordlinkage.Pairs(df1, df2)
        pairs = index.block('name')

        index_exp = [('001', '001'), ('002', '002'),('003', '003')]

        # Check if index is unique
        self.assertTrue(pairs.index.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), 3)

    def test_sortedneighbourhood_index_unique(self):

        df1 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=['001', '002', '003'])
        df2 = pd.DataFrame({'name':['Bob', 'Anne', 'Micheal']}, index=['001', '002', '003'])

        index = recordlinkage.Pairs(df1, df2)
        pairs = index.sortedneighbourhood('name')

        index_exp = [('001', '001'), ('002', '002'),('003', '003')]

        # Check if index is unique
        self.assertTrue(pairs.index.is_unique)

    def test_full_index_datasets(self):

        dfA = datasets.load_censusA()
        dfB = datasets.load_censusB()

        index = recordlinkage.Pairs(dfA, dfB)
        pairs = index.full()

        # Check if index is unique
        self.assertTrue(pairs.index.is_unique)

        # Check is number of pairs is correct
        self.assertEqual(len(pairs), len(dfA)*len(dfB))

    def test_full_block_datasets(self):

        dfA = datasets.load_censusA()
        dfB = datasets.load_censusB()

        index = recordlinkage.Pairs(dfA, dfB)
        pairs = index.block('last_name')

        # Check if index is unique
        self.assertTrue(pairs.index.is_unique)

    def test_full_sorted_datasets(self):

        dfA = datasets.load_censusA()
        dfB = datasets.load_censusB()

        index = recordlinkage.Pairs(dfA, dfB)
        pairs = index.sortedneighbourhood('last_name')

        # Check if index is unique
        self.assertTrue(pairs.index.is_unique)


