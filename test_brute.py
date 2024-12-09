import pytest
from brute import Brute
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        # write your test cases here
        
        def it_successfully_compares_attempt_to_target():
            b = Brute("testing")

            assert b.bruteOnce("testing")


        def it_fails_compare_attempt_to_target():
            b = Brute("testing")

            assert b.bruteOnce("wrong") == False

        def it_fails_compare_int_to_string():
            b = Brute('123456')

            try:
                b.bruteOnce(123456)
                assert False
            except TypeError as e:
                assert True

        def it_fails_no_attempt_param():
            b = Brute("Missing parameter")

            try:
                b.bruteOnce()
                assert False
            except TypeError as e:
                assert True

        def it_fails_compare_with_and_without_spaces():
            b = Brute("Secret String With Spaces")

            assert b.bruteOnce("SecretStringWithSpaces") == False

    def describe_bruteMany():
        # write your test cases here
        
        def it_cracks_target_small():
            b = Brute("ab")

            assert b.bruteMany() != -1

        def it_fails_short_limit():
            b = Brute("reallylongstringtesting")

            assert b.bruteMany(10) == -1

        def it_cracks_target_large(mocker):
            b = Brute("testingwithmocker")

            mock_random_guess = mocker.patch.object(Brute, "randomGuess", return_value = "testingwithmocker")

            assert b.bruteMany() != -1
            mock_random_guess.assert_called_once_with() 

        def it_fails_to_crack(mocker):
            b = Brute("testingwithmocker")

            mock_brute_many = mocker.patch.object(Brute, "bruteMany", return_value = -1)

            assert b.bruteMany() == -1


    
