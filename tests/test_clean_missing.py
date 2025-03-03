# tests/test_clean_missing.py
import pandas as pd
import pytest
from tidyflow.preprocessing.clean_missing import clean_missing

def test_clean_missing():
    df = pd.DataFrame({'A': [1, 2, None, 4], 'B': [None, 'cat', 'dog', 'mouse']})
    result = clean_missing(df, strategy='mean')
    assert result.isnull().sum().sum() == 0
