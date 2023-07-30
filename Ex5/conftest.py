import pytest
import time


@pytest.fixture(autouse=True)
def time_it(request):
    start_time = time.time()
    yield
    end_time = time.time()
    print(f'\nTime taken to run the test {request.node.name}: {end_time - start_time} seconds')


