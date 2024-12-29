"""
Program: Pytest file to validate the URL
main.py
Date: 29-DEC-2024
Caveats:None
"""

import pytest
from main import Hackathon
from main import Data

url = "https://demo.nopcommerce.com/"

hari = Hackathon()

#Positive Test case

def test_positive_url():
    test_url = "https://demo.nopcommerce.com/"
    test_url2 = "https://demo.nopcommerce.com/"
    assert test_url2 == test_url
    print(f"Success{test_url} is the valid URL")

#Negative test case

def test_negative_url():
    test_url = "https://mail.google.com/mail/u/0/#inbox/FMfcgzQXKWlzBLRCGplTsRvPTNxFNNNx"
    assert Data == test_url
    print("Negative test case failed")

