from distutils.core import setup

setup(
    name = 'opengraph',
    version = '1',
    description = 'opengraph is a library written in Python for parsing Open Graph protocol information from web sites.',
    packages = ['opengraph', ],
    author = 'Gerson Minichiello',
    author_email = 'gerson.minichiello@gmail.com',
    url='http://github.com/graingert/PyOpenGraph',
    platforms = 'Any',
    license = 'MIT License',
    long_description='''\
=============
 opengraph
=============
    
opengraph is a library written in Python for parsing Open Graph protocol information from web sites.

Learn more about the protocol at:

http://opengraphprotocol.org

--------------
 Installation
--------------

To install::

    pip install opengraph

-------
 Usage
-------
::

    import opengraph

    og = opengraph('http://www.rottentomatoes.com/m/10011268-oceans/')

    print og.metadata # => {'url': 'http://www.rottentomatoes.com/m/10011268-oceans/', 'site_name': 'Rotten Tomatoes', 'image': 'http://images.rottentomatoes.com/images/movie/custom/68/10011268.jpg', 'type': 'movie', 'title': 'Oceans'}

    print og.metadata['title'] # => Oceans

    og.is_valid() # => return True or False
''',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
