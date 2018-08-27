#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from Fetch_Transaction_API import FetchTransactionAPI

class MyTestSuite(unittest.TestCase):
    def test_fetch_transaction_api(self):
        a = FetchTransactionAPI.FetchTransaction()
        a.FetchTransactionDetails()

if __name__ == "__main__":
    apitest = MyTestSuite()
    apitest.test_fetch_transaction_api()