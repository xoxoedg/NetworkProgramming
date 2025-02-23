from src.http.http_method import HttpMethod
from src.http.htttp_method_mapper import HttpMethodMapper
from typing import Dict, Union, List


class HttpRequestParser:
    CARRIAGE_RETURN: str = "\r"
    LINE_FEED: str = "\n"

    def __init__(self, filename: str):
        self.filename: str = filename
        self.http_request_dict: Dict[str, Union[HttpMethod, str, Dict[str, str]]] = {
            "method": HttpMethod.GET,
            "url": "",
            "version": "",
            "headers": {},
            "body": {},
        }
        self.headers_lines: List[str] = []
        self.http_request_split_by_newline: List[str] = []

    def parse(self) -> None:
        http_request: str = self.get_file_content()
        # ['GET / HTTP/1.1', 'Host: example.com', 'User-Agent: MyApp/1.0', 'Accept: application/json', 'Authorization: Bearer your_token_here', 'X-Custom-Header: CustomValue']
        self.http_request_split_by_newline: List[str] = http_request.split(self.LINE_FEED)
        self.parse_request_line()
        self.parse_header()
        self.parse_body()

    def parse_request_line(self) -> None:
        separated_request_line: List[str] = self.http_request_split_by_newline[0].split()
        http_method = separated_request_line[0]
        http_url = separated_request_line[1]
        http_version = separated_request_line[2]

        self.http_request_dict["method"] = HttpMethodMapper.map(http_method)
        self.http_request_dict["url"] = http_url
        self.http_request_dict["version"] = http_version

    def parse_header(self) -> None:
        # ['Host: example.com', 'User-Agent: MyApp/1.0', 'Accept: application/json', 'Authorization: Bearer your_token_here', 'X-Custom-Header: CustomValue']
        self.headers_lines: List[str] = self.parse_all_header_lines_into_list()
        # 'Host: example.com'
        for header_line in self.headers_lines:
            if ":" in header_line:
                header_name, header_value = header_line.split(":", 1)

                self.http_request_dict["headers"][header_name.strip()] = header_value.strip()

    def parse_all_header_lines_into_list(self) -> List[str]:
        header_lines: List[str] = []
        for line in self.http_request_split_by_newline[1:]:
            if line.strip() == "":
                break
            header_lines.append(line)
        return header_lines

    def parse_body(self) -> None:
        header_lines_size: int = len(self.headers_lines)
        http_request_split_by_newline_size: int = len(self.http_request_split_by_newline)
        body_start_index: int = header_lines_size + 2  # Skip empty line
        if body_start_index < http_request_split_by_newline_size:
            self.http_request_dict["body"] = self.modify_body(
                self.http_request_split_by_newline[body_start_index:]
            )

    def modify_body(self, body: List[str]) -> str:
        return "\n".join(body)

    def get_file_content(self) -> str:
        with open(self.filename, "r") as file:
            return file.read()


a: HttpRequestParser = HttpRequestParser("http_request")
a.parse()
