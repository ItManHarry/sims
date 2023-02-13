from com import create_app
app = create_app()
from waitress import serve
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    serve(app.wsgi_app, host='0.0.0.0', port=80)