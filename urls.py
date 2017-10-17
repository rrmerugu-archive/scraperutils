from urlparse import urlparse

def get_domain(url):
    """
    Extracts http://google.com from "http://google.com/blog/xxxx-xxx-xxx
    """
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain.rstrip('/')
