import pytest
import vsm
import math


class TestVSM:
    @pytest.mark.points(2)
    def test_tokenize_no_sw(self):
        docs = {'doc1': 'This is a test',
                'doc2': 'This is another test'}
        expected = {'doc1': ['this', 'is', 'a', 'test'],
                    'doc2': ['this', 'is', 'another', 'test']}
        assert vsm.tokenize(docs) == expected

    @pytest.mark.points(2)
    def test_tokenize_sw_simple(self):
        docs = {'doc1': 'This is a test',
                'doc2': 'This is another test'}
        sws = {'a', 'is'}
        expected = {'doc1': ['this', 'test'],
                    'doc2': ['this', 'another', 'test']}
        assert vsm.tokenize(docs, sws) == expected

    @pytest.mark.points(2)
    def test_tokenize_sw_cakes(self):
        docs = {'doc1': 'the cakes are everywhere',
                'doc2': 'all I want are all the cakes cakes cakes',
                'doc3': 'pies are what I want',
                'doc4': 'cakes and pies are everywhere'}
        sws = {'are', 'and', 'the', 'is'}
        expected = {
            'doc1': ['cakes', 'everywhere'],
            'doc2': ['all', 'i', 'want', 'all', 'cakes', 'cakes', 'cakes'],
            'doc3': ['pies', 'what', 'i', 'want'],
            'doc4': ['cakes', 'pies', 'everywhere']
        }
        assert vsm.tokenize(docs, sws) == expected

    @pytest.mark.points(3)
    def test_build_index_simple(self):
        docs = {'doc1': ['this', 'test'],
                'doc2': ['this', 'another', 'test']}
        expected = {'this': {'doc1': 1, 'doc2': 1},
                    'test': {'doc1': 1, 'doc2': 1},
                    'another': {'doc2': 1}}
        assert vsm.build_index(docs) == expected

    @pytest.mark.points(3)
    def test_build_index_cakes(self):
        docs = {
            'doc1': ['cakes', 'everywhere'],
            'doc2': ['all', 'i', 'want', 'all', 'cakes', 'cakes', 'cakes'],
            'doc3': ['pies', 'what', 'i', 'want'],
            'doc4': ['cakes', 'pies', 'everywhere']
        }
        expected = {
            'cakes': {'doc1': 1, 'doc2': 3, 'doc4': 1},
            'everywhere': {'doc1': 1, 'doc4': 1},
            'all': {'doc2': 2},
            'i': {'doc2': 1, 'doc3': 1},
            'want': {'doc2': 1, 'doc3': 1},
            'pies': {'doc3': 1, 'doc4': 1},
            'what': {'doc3': 1}
        }
        assert vsm.build_index(docs) == expected

    @pytest.mark.points(3)
    def test_build_tfidf_index_simple(self):
        index = {'this': {'doc1': 1, 'doc2': 1},
                 'test': {'doc1': 1, 'doc2': 1},
                 'another': {'doc2': 1}}
        expected = {'this': {'doc1': 0.0, 'doc2': 0.0},
                    'test': {'doc1': 0.0, 'doc2': 0.0},
                    'another': {'doc2': 0.30102}}
        result = vsm.build_tfidf_index(index, 2)
        assert len(result) == len(expected)
        for tok in expected:  # pytest.approx can't do nested dicts
            assert result[tok] == pytest.approx(expected[tok], abs=0.001)

    @pytest.mark.points(3)
    def test_build_tfidf_index_cakes(self):
        index = {
            'cakes': {'doc1': 1, 'doc2': 3, 'doc4': 1},
            'everywhere': {'doc1': 1, 'doc4': 1},
            'all': {'doc2': 2},
            'i': {'doc2': 1, 'doc3': 1},
            'want': {'doc2': 1, 'doc3': 1},
            'pies': {'doc3': 1, 'doc4': 1},
            'what': {'doc3': 1}
        }
        expected = {
            'cakes': {'doc1': 0.12494, 'doc2': 0.37482, 'doc4': 0.12494},
            'everywhere': {'doc1': 0.30103, 'doc4': 0.30103},
            'all': {'doc2': 1.20412},
            'i': {'doc2': 0.30103, 'doc3': 0.30103},
            'want': {'doc2': 0.30103, 'doc3': 0.30103},
            'pies': {'doc3': 0.30103, 'doc4': 0.30103},
            'what': {'doc3': 0.60206}
        }
        result = vsm.build_tfidf_index(index, 4)
        assert len(result) == len(expected)
        for tok in expected:  # pytest.approx can't do nested dicts
            assert result[tok] == pytest.approx(expected[tok], abs=0.001)

    @pytest.mark.points(3)
    def test_run_query_simple(self):
        index = {'a': {'doc1': 4, 'doc2': 2},
                 'b': {'doc1': 3, 'doc2': 1},
                 'c': {'doc2': 1, 'doc3': 2}}
        query = 'a b'
        expected = [('doc1', 7), ('doc2', 3)]
        assert vsm.run_query(index, query) == expected

    @pytest.mark.points(3)
    def test_run_query_cakes(self):
        index = {
            'cakes': {'doc1': 0.12494, 'doc2': 0.37482, 'doc4': 0.12494},
            'everywhere': {'doc1': 0.30103, 'doc4': 0.30103},
            'all': {'doc2': 1.20412},
            'i': {'doc2': 0.30103, 'doc3': 0.30103},
            'want': {'doc2': 0.30103, 'doc3': 0.30103},
            'pies': {'doc3': 0.30103, 'doc4': 0.30103},
            'what': {'doc3': 0.60206}
        }

        query = 'i want yummy pies'
        expected = [('doc3', 0.903), ('doc2', 0.602), ('doc4', 0.301)]
        result = vsm.run_query(index, query)
        assert len(result) == len(expected)
        for i in range(len(expected)):
            assert result[i][0] == expected[i][0]
            assert result[i][1] == pytest.approx(expected[i][1], abs=0.001)

        query = 'cakes i want'
        expected = [('doc2', 0.97688), ('doc3', 0.60206),
                    ('doc1', 0.12494), ('doc4', 0.12494)]
        result = vsm.run_query(index, query)
        assert len(result) == len(expected)
        for i in range(len(expected)):
            assert result[i][0] == expected[i][0]
            assert result[i][1] == pytest.approx(expected[i][1], abs=0.001)

    @pytest.mark.points(8)
    def test_vsm(self):
        docs = {'doc1': 'the cakes are everywhere',
                'doc2': 'all I want are all the cakes cakes cakes',
                'doc3': 'pies are what I want',
                'doc4': 'cakes and pies are everywhere'}
        sws = {'are', 'and', 'the', 'is'}
        tf_index = vsm.build_index(vsm.tokenize(docs, sws))
        tfidf_index = vsm.build_tfidf_index(tf_index, len(docs))
        query = 'i want yummy pies'
        expected = [('doc3', 0.903), ('doc2', 0.602), ('doc4', 0.301)]
        result = vsm.run_query(tfidf_index, query)
        assert len(result) == len(expected)
        for i in range(len(expected)):
            assert result[i][0] == expected[i][0]
            assert result[i][1] == pytest.approx(expected[i][1], abs=0.001)