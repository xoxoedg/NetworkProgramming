import pytest

from src.http.http_method import HttpMethod
from src.http.htttp_method_mapper import HttpMethodMapper


@pytest.mark.parametrize(
    "http_request_method, expected_http_method",
    [
        ("GET", HttpMethod.GET),
        ("POST", HttpMethod.POST),
        ("PUT", HttpMethod.PUT),
        ("DELETE", HttpMethod.DELETE),
        ("HEAD", HttpMethod.HEAD),
    ],
)
def test_map_http_method_valid(http_request_method, expected_http_method):
    assert HttpMethodMapper.map(http_request_method) == expected_http_method


@pytest.mark.parametrize("http_request_method", ["PATCH", "OPTIONS", "CONNECT"])
def test_map_http_method_invalid(http_request_method):
    with pytest.raises(ValueError, match="Unknown HTTP request method"):
        HttpMethodMapper.map(http_request_method)
