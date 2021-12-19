

import pytest



# this is from conftest.py
# you dont need to import fixtures
# pytest is taking care automatically
def test_that_gets_a_fixture(just_give_me_the_client):
	assert just_give_me_the_client == 1

def test_first_one():
	print("hello world from test 1")
	assert 1 == 1


@pytest.mark.skip
def test_to_skip():
	assert 1 == 1

@pytest.mark.xfail
def test_that_you_know_is_gonna_fail():
	assert 1 == 2
