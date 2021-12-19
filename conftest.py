

import pytest


# to run this once per tests
# @pytest.fixture(scope="module")
@pytest.fixture(scope="session")
def just_give_me_the_client():
	print("asdonasodnasjd")
	return 1