class HttpRequest:
    """
    Class to http_request representation
    """

    def __init__(
            self,
            headers = None,
            body = None,
            query_params = None,
            path_params = None,
            url = None,
            ipv4 = None
    ):

        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4

    def __repr__(self):
        return f"HttpRequest (headers={self.headers}, body={self.body}, query_params={self.query_params}, path_params={self.path_params}, url={self.url}, ipv4={self.ipv4})"


class HttpResponse:
    """
    Class to http_response representation
    """

    def __init__(self, status_code: int, body: any):

        self.status_code = status_code
        self.body = body

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body})"
