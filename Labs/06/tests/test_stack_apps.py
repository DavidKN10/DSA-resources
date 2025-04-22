import pytest
from stack_apps import check_delimiters, infix_to_postfix

class TestDelimiterMatcher:
    @pytest.mark.points(1)
    def test_simple_delims(self):
        assert check_delimiters('()', {'(': ')'})
        assert check_delimiters('[]', {'[': ']'})
        assert check_delimiters('<>', {'<': '>'})
        assert check_delimiters('""', {'"': '"'})
        assert not check_delimiters('(', {'(': ')'})
        assert not check_delimiters(')', {'(': ')'})
        assert not check_delimiters('[', {'[': ']'})

    
    @pytest.mark.points(1)
    def test_simple_nested_delims(self):
        assert check_delimiters('(())', {'(': ')'})
        assert check_delimiters('((()()()))', {'(': ')'})
        assert check_delimiters('([] () [])', {'[': ']', '(': ')'})
        assert check_delimiters('((<><>))', {'(': ')', '<': '>'})
        assert not check_delimiters('(()', {'(': ')'})
        assert not check_delimiters('())', {'(': ')'})
        assert not check_delimiters('([]))', {'(': ')', '[': ']'})

    @pytest.mark.points(2)
    def test_unspecified_delims(self):
        assert check_delimiters('(<)[>]', {'(': ')', '[': ']'})
        assert check_delimiters('(><]])', {'(': ')'})
        assert check_delimiters('[<><<><>>)', {'<': '>'})
        assert check_delimiters('[<><<><>>)', {'<': '>'})
        assert not check_delimiters('(<)(>]', {'(': ')'})
        assert not check_delimiters('( [ [ ) ( ] ] )', {'(':')', '[':']'})


    @pytest.mark.points(2)
    def test_weird_delims(self):
        assert check_delimiters('[>', {'[': '>'})
        assert check_delimiters('<[><!!', {'[': '>', '<': '!'})
        assert not check_delimiters('[]', {'[': '>'})
        assert not check_delimiters('()', {'(': '!'})


    @pytest.mark.points(2)
    def test_quotes_simple(self):
        assert check_delimiters('""', {'"': '"'})
        assert check_delimiters('"hello" "world"', {'"': '"'})
        assert check_delimiters('("b", "m", "r", ("t"))', {'(': ')', '"': '"'})
        assert check_delimiters('( " " ) ( " " )', {'(':')', '"':'"'})
        assert check_delimiters('"\' \' \' \'" "\' \'"', {'"': '"', "'": "'"})
        assert not check_delimiters('"\'"\'', {'"': '"', "'": "'"})
        assert not check_delimiters('(")"', {'(': ')', '"': '"'})
        

class TestInfixToPostfix:
    @pytest.mark.points(2)
    def test_ifpf_basic(self):
        assert infix_to_postfix('1') == '1'
        assert infix_to_postfix('1 + 2') == '1 2 +'
        assert infix_to_postfix('( 1 + 2 )') == '1 2 +'
        assert infix_to_postfix('1 + 2 - 3') == '1 2 + 3 -'
        assert infix_to_postfix('1 + ( 2 - 3 )') == '1 2 3 - +'

    @pytest.mark.points(3)
    def test_ifpf_prec(self):
        assert infix_to_postfix('1 + 2 * 3') == '1 2 3 * +'
        assert infix_to_postfix('1 / 2 + 3 * 4') == '1 2 / 3 4 * +'
        assert infix_to_postfix('1 * 2 * 3 + 4') == '1 2 * 3 * 4 +'
        assert infix_to_postfix('1 + 2 * 3 * 4') == '1 2 3 * 4 * +'

    @pytest.mark.points(3)
    def test_ifpf_parens(self):
        assert infix_to_postfix('1 * ( 2 + 3 ) * 4') == '1 2 3 + * 4 *'
        assert (infix_to_postfix('1 * ( 2 + 3 * 4 ) + 5') 
                == '1 2 3 4 * + * 5 +')
        assert (infix_to_postfix('1 * ( ( 2 + 3 ) * 4 ) * ( 5 - 6 )') 
                == '1 2 3 + 4 * * 5 6 - *')
