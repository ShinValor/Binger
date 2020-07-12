"""
File that will control the starting of the Flask app.
"""

# gevent needs to be monkey patched before everything to avoid recursion errors
from gevent import monkey
monkey.patch_all(thread=False, select=False)

from app import app

if __name__ == '__main__':
    app.run()