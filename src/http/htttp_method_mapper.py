from src.http.http_method import HttpMethod


class HttpMethodMapper:

    @staticmethod
    def map(http_request_method : str) -> HttpMethod:
        match http_request_method:
            case "GET":
                return HttpMethod.GET
            case "POST":
                return HttpMethod.POST
            case "PUT":
                return HttpMethod.PUT
            case "DELETE":
                return HttpMethod.DELETE
            case "HEAD":
                return HttpMethod.HEAD
            case _:
                raise ValueError("Unknown HTTP request method")
