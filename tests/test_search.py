import pytest

from ..search import Search

def test_builtLink():
    tmpSearch = Search()
    tmpSearch.setEngine("amazon")
    tmpSearch.setDomain("com")
    tmpSearch.setQuery(["test", "query"])
    assert tmpSearch.buildLink() == "http://www.amazon.com/s/keywords=test%20query"
