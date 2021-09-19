import os.path

from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib

numpydir = os.path.join(get_python_lib(plat_specific=1), 'numpy', 'core', 'include')


module = Extension('msacounts', sources=['src/msacounts.c'])

setup(  name='msacounts',
        version='1.0',
        description='Fast MSA pair counting',
        author='Stefan Seemayer',
        author_email='stefan@seemayer.de',
        packages=['msacounts'],
        license='MIT',

        ext_modules=[
            Extension(  'msacounts/cext/_msacounts',
                        [
                            'msacounts/cext/msacounts.i',
                            'msacounts/cext/msacounts.c'
                        ],
                        swig_opts=['-modern', '-Imsacounts/cext/'],
                        include_dirs=['msacounts/cext', numpydir]
           )
        ],

        py_modules=['msacounts/cext/msacounts']

)
