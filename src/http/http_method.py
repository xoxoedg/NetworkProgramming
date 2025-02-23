from enum import Enum


class HttpMethod(Enum):
    GET: str = "GET"
    POST: str = "POST"
    PUT: str = "PUT"
    DELETE: str = "DELETE"
    HEAD: str = "HEAD"

