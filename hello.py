
def wsgi_app(environ, start_response):

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = "\n".join(environ.get('QUERY_STRING').split("&"))
    start_response(status,headers)
    return [body]