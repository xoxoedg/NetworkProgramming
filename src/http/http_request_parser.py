from src.http.htttp_method_mapper import HttpMethodMapper


class HttpRequestParser:

    CARRIAGE_RETURN = "\r"
    LINE_FEED = "\n"


    def __init__(self, filename):
        self.filename = filename
        self.http_request_dict = {
            "method": None,
            "url": "",
            "version": "",
            "headers": {},
            "body": None
        }
        self.headers_lines = None
        self.http_request_split_by_newline = None

    def parse(self):
        http_request = self.open_file()
        #['GET / HTTP/1.1', 'Host: example.com', 'User-Agent: MyApp/1.0', 'Accept: application/json', 'Authorization: Bearer your_token_here', 'X-Custom-Header: CustomValue']
        self.http_request_split_by_newline = http_request.split(self.LINE_FEED)
        self.parse_line(self.http_request_split_by_newline[0])
        self.parse_header(self.http_request_split_by_newline)
        self.parse_body()



    def parse_line(self, request_line):
        separated_request_line = request_line.split()
        http_method = separated_request_line[0]
        http_url = separated_request_line[1]
        http_version = separated_request_line[2]

        self.http_request_dict["method"] = HttpMethodMapper.map(http_method)
        self.http_request_dict["url"] = http_url
        self.http_request_dict["version"] = http_version

    def parse_header(self, split_by_newline):
        #['Host: example.com', 'User-Agent: MyApp/1.0', 'Accept: application/json', 'Authorization: Bearer your_token_here', 'X-Custom-Header: CustomValue']
        self.headers_lines = self.parse_all_header_lines_into_list(split_by_newline)

        # 'Host: example.com'
        for header_line in  self.headers_lines:
            if ":" in header_line:
                header_name, header_value = header_line.split(":", 1)

                self.http_request_dict["headers"][header_name.strip()] = header_value.strip()


    def parse_all_header_lines_into_list(self, split_by_newline):
        header_lines = []
        for line in split_by_newline[1:]:
            if line.strip() == "":
                break
            header_lines.append(line)
        return header_lines

    def parse_body(self):
        header_lines_size = len(self.headers_lines)
        http_request_split_by_newline_size = len(self.http_request_split_by_newline)
        body_start_index = header_lines_size + 2 #Skip empty line
        if  body_start_index  < http_request_split_by_newline_size:
            self.http_request_dict["body"] = self.modify_body(self.http_request_split_by_newline[body_start_index:])


        print(self.http_request_dict["body"])
        print(self.http_request_dict)

    def modify_body(self, body):
        return "\n".join(body)

    def open_file(self):
        with open(self.filename, 'r') as file:
           return file.read()




a = HttpRequestParser("http_request")
a.parse()

