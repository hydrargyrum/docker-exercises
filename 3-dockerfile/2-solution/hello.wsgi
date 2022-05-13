from bottle import *
get('/')(lambda: 'Hello world')
application = default_app()
if __name__ == '__main__': run(host='0.0.0.0')
