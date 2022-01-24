


import pytest
import time
from rich.console import Console


# to run this once per tests
# @pytest.fixture(scope="module")
@pytest.fixture(scope="session")
def just_give_me_the_client():
    print("asdonasodnasjd")
    return 1

def pytest_unconfigure(config):
    # inspiration from
    # https://stackoverflow.com/questions/56271207/how-to-access-the-overall-runtime-in-pytest
    _con = Console()
    reporter = config.pluginmanager.get_plugin('terminalreporter')
    duration = time.time() - reporter._sessionstarttime
    _con.print(f"\npytest exec time: [ [yellow]{duration:.3f}[/] ] seconds")
    # reporter.write_sep('=', 'duration: {} seconds'.format(duration), yellow=True, bold=True)