class XForwardedForMiddleware():
    """
    Sets REMOTE_ADDR correctly to the client's ip, if django is run on a domain socket server.
    ref: https://stackoverflow.com/a/34254843/1031191
    """
    def process_request(self, request):
        if "HTTP_X_FORWARDED_FOR" in request.META:
            request.META["HTTP_X_PROXY_REMOTE_ADDR"] = request.META["REMOTE_ADDR"]
            parts = request.META["HTTP_X_FORWARDED_FOR"].split(",", 1)
            request.META["REMOTE_ADDR"] = parts[0]