from distutils.core import setup, Extension

module = Extension('msacounts', sources=['src/msacounts.c'])

setup(  name='msacounts',
        version='1.0',
        description='Fast MSA pair counting',
        author='Stefan Seemayer',
        author_email='stefan@seemayer.de',
        packages=['msacounts'],

        ext_modules=[
            Extension(  'msacounts/cext/_msacounts',
                        [
                            'msacounts/cext/msacounts.i',
                            'msacounts/cext/msacounts.c'
                        ],
                        swig_opts=['-modern', '-Imsacounts/cext/'],
                        include_dirs=['msacounts/cext']
           )
        ],

        py_modules=['msacounts/cext/msacounts']

)
