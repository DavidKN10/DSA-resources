import pytest
import palindrome

class TestPalindrome:
    def test_palindrome(self):
        pal = palindrome.my_palindrome()
        assert isinstance(pal, str), 'Must return a string'
        assert pal.strip() != '', 'String should not be empty'
        assert len(pal) >= 3, 'String should be at least 3 letters long'
        assert pal == pal[::-1], 'String is not a palindrome'
