from setuptools import setup

setup(
    name='fullthrottle_test_site_setup.py',
    version='v0.0.0',
    packages=['venv.lib.python3.7.site-packages.pip', 'venv.lib.python3.7.site-packages.pip._vendor',
              'venv.lib.python3.7.site-packages.pip._vendor.idna',
              'venv.lib.python3.7.site-packages.pip._vendor.pep517',
              'venv.lib.python3.7.site-packages.pip._vendor.pytoml',
              'venv.lib.python3.7.site-packages.pip._vendor.certifi',
              'venv.lib.python3.7.site-packages.pip._vendor.chardet',
              'venv.lib.python3.7.site-packages.pip._vendor.chardet.cli',
              'venv.lib.python3.7.site-packages.pip._vendor.distlib',
              'venv.lib.python3.7.site-packages.pip._vendor.distlib._backport',
              'venv.lib.python3.7.site-packages.pip._vendor.msgpack',
              'venv.lib.python3.7.site-packages.pip._vendor.urllib3',
              'venv.lib.python3.7.site-packages.pip._vendor.urllib3.util',
              'venv.lib.python3.7.site-packages.pip._vendor.urllib3.contrib',
              'venv.lib.python3.7.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.lib.python3.7.site-packages.pip._vendor.urllib3.packages',
              'venv.lib.python3.7.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.lib.python3.7.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.7.site-packages.pip._vendor.colorama',
              'venv.lib.python3.7.site-packages.pip._vendor.html5lib',
              'venv.lib.python3.7.site-packages.pip._vendor.html5lib._trie',
              'venv.lib.python3.7.site-packages.pip._vendor.html5lib.filters',
              'venv.lib.python3.7.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.lib.python3.7.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.lib.python3.7.site-packages.pip._vendor.html5lib.treebuilders',
              'venv.lib.python3.7.site-packages.pip._vendor.lockfile',
              'venv.lib.python3.7.site-packages.pip._vendor.progress',
              'venv.lib.python3.7.site-packages.pip._vendor.requests',
              'venv.lib.python3.7.site-packages.pip._vendor.packaging',
              'venv.lib.python3.7.site-packages.pip._vendor.cachecontrol',
              'venv.lib.python3.7.site-packages.pip._vendor.cachecontrol.caches',
              'venv.lib.python3.7.site-packages.pip._vendor.webencodings',
              'venv.lib.python3.7.site-packages.pip._vendor.pkg_resources',
              'venv.lib.python3.7.site-packages.pip._internal', 'venv.lib.python3.7.site-packages.pip._internal.cli',
              'venv.lib.python3.7.site-packages.pip._internal.req',
              'venv.lib.python3.7.site-packages.pip._internal.vcs',
              'venv.lib.python3.7.site-packages.pip._internal.utils',
              'venv.lib.python3.7.site-packages.pip._internal.models',
              'venv.lib.python3.7.site-packages.pip._internal.commands',
              'venv.lib.python3.7.site-packages.pip._internal.operations', 'venv.lib.python3.7.site-packages.flask',
              'venv.lib.python3.7.site-packages.flask.ext', 'venv.lib.python3.7.site-packages.numpy',
              'venv.lib.python3.7.site-packages.numpy.ma', 'venv.lib.python3.7.site-packages.numpy.ma.tests',
              'venv.lib.python3.7.site-packages.numpy.doc', 'venv.lib.python3.7.site-packages.numpy.fft',
              'venv.lib.python3.7.site-packages.numpy.fft.tests', 'venv.lib.python3.7.site-packages.numpy.lib',
              'venv.lib.python3.7.site-packages.numpy.lib.tests', 'venv.lib.python3.7.site-packages.numpy.core',
              'venv.lib.python3.7.site-packages.numpy.core.tests', 'venv.lib.python3.7.site-packages.numpy.f2py',
              'venv.lib.python3.7.site-packages.numpy.f2py.tests', 'venv.lib.python3.7.site-packages.numpy.tests',
              'venv.lib.python3.7.site-packages.numpy.compat', 'venv.lib.python3.7.site-packages.numpy.compat.tests',
              'venv.lib.python3.7.site-packages.numpy.linalg', 'venv.lib.python3.7.site-packages.numpy.linalg.tests',
              'venv.lib.python3.7.site-packages.numpy.random', 'venv.lib.python3.7.site-packages.numpy.random.tests',
              'venv.lib.python3.7.site-packages.numpy.testing', 'venv.lib.python3.7.site-packages.numpy.testing.tests',
              'venv.lib.python3.7.site-packages.numpy.testing._private',
              'venv.lib.python3.7.site-packages.numpy.distutils',
              'venv.lib.python3.7.site-packages.numpy.distutils.tests',
              'venv.lib.python3.7.site-packages.numpy.distutils.command',
              'venv.lib.python3.7.site-packages.numpy.distutils.fcompiler',
              'venv.lib.python3.7.site-packages.numpy.matrixlib',
              'venv.lib.python3.7.site-packages.numpy.matrixlib.tests',
              'venv.lib.python3.7.site-packages.numpy.polynomial',
              'venv.lib.python3.7.site-packages.numpy.polynomial.tests', 'venv.lib.python3.7.site-packages.jinja2',
              'venv.lib.python3.7.site-packages.pandas', 'venv.lib.python3.7.site-packages.pandas.io',
              'venv.lib.python3.7.site-packages.pandas.io.sas', 'venv.lib.python3.7.site-packages.pandas.io.json',
              'venv.lib.python3.7.site-packages.pandas.io.formats',
              'venv.lib.python3.7.site-packages.pandas.io.msgpack',
              'venv.lib.python3.7.site-packages.pandas.io.clipboard', 'venv.lib.python3.7.site-packages.pandas.api',
              'venv.lib.python3.7.site-packages.pandas.api.types',
              'venv.lib.python3.7.site-packages.pandas.api.extensions', 'venv.lib.python3.7.site-packages.pandas.core',
              'venv.lib.python3.7.site-packages.pandas.core.util', 'venv.lib.python3.7.site-packages.pandas.core.tools',
              'venv.lib.python3.7.site-packages.pandas.core.arrays',
              'venv.lib.python3.7.site-packages.pandas.core.dtypes',
              'venv.lib.python3.7.site-packages.pandas.core.sparse',
              'venv.lib.python3.7.site-packages.pandas.core.groupby',
              'venv.lib.python3.7.site-packages.pandas.core.indexes',
              'venv.lib.python3.7.site-packages.pandas.core.reshape',
              'venv.lib.python3.7.site-packages.pandas.core.computation',
              'venv.lib.python3.7.site-packages.pandas.util', 'venv.lib.python3.7.site-packages.pandas._libs',
              'venv.lib.python3.7.site-packages.pandas._libs.tslibs', 'venv.lib.python3.7.site-packages.pandas.tests',
              'venv.lib.python3.7.site-packages.pandas.tests.io',
              'venv.lib.python3.7.site-packages.pandas.tests.io.sas',
              'venv.lib.python3.7.site-packages.pandas.tests.io.json',
              'venv.lib.python3.7.site-packages.pandas.tests.io.parser',
              'venv.lib.python3.7.site-packages.pandas.tests.io.formats',
              'venv.lib.python3.7.site-packages.pandas.tests.io.msgpack',
              'venv.lib.python3.7.site-packages.pandas.tests.api', 'venv.lib.python3.7.site-packages.pandas.tests.util',
              'venv.lib.python3.7.site-packages.pandas.tests.frame',
              'venv.lib.python3.7.site-packages.pandas.tests.tools',
              'venv.lib.python3.7.site-packages.pandas.tests.dtypes',
              'venv.lib.python3.7.site-packages.pandas.tests.scalar',
              'venv.lib.python3.7.site-packages.pandas.tests.scalar.period',
              'venv.lib.python3.7.site-packages.pandas.tests.scalar.interval',
              'venv.lib.python3.7.site-packages.pandas.tests.scalar.timedelta',
              'venv.lib.python3.7.site-packages.pandas.tests.scalar.timestamp',
              'venv.lib.python3.7.site-packages.pandas.tests.series',
              'venv.lib.python3.7.site-packages.pandas.tests.series.indexing',
              'venv.lib.python3.7.site-packages.pandas.tests.sparse',
              'venv.lib.python3.7.site-packages.pandas.tests.sparse.frame',
              'venv.lib.python3.7.site-packages.pandas.tests.sparse.series',
              'venv.lib.python3.7.site-packages.pandas.tests.tslibs',
              'venv.lib.python3.7.site-packages.pandas.tests.generic',
              'venv.lib.python3.7.site-packages.pandas.tests.groupby',
              'venv.lib.python3.7.site-packages.pandas.tests.groupby.aggregate',
              'venv.lib.python3.7.site-packages.pandas.tests.indexes',
              'venv.lib.python3.7.site-packages.pandas.tests.indexes.period',
              'venv.lib.python3.7.site-packages.pandas.tests.indexes.interval',
              'venv.lib.python3.7.site-packages.pandas.tests.indexes.datetimes',
              'venv.lib.python3.7.site-packages.pandas.tests.indexes.timedeltas',
              'venv.lib.python3.7.site-packages.pandas.tests.reshape',
              'venv.lib.python3.7.site-packages.pandas.tests.reshape.merge',
              'venv.lib.python3.7.site-packages.pandas.tests.tseries',
              'venv.lib.python3.7.site-packages.pandas.tests.tseries.offsets',
              'venv.lib.python3.7.site-packages.pandas.tests.indexing',
              'venv.lib.python3.7.site-packages.pandas.tests.indexing.interval',
              'venv.lib.python3.7.site-packages.pandas.tests.plotting',
              'venv.lib.python3.7.site-packages.pandas.tests.extension',
              'venv.lib.python3.7.site-packages.pandas.tests.extension.base',
              'venv.lib.python3.7.site-packages.pandas.tests.extension.json',
              'venv.lib.python3.7.site-packages.pandas.tests.extension.decimal',
              'venv.lib.python3.7.site-packages.pandas.tests.extension.category',
              'venv.lib.python3.7.site-packages.pandas.tests.internals',
              'venv.lib.python3.7.site-packages.pandas.tests.categorical',
              'venv.lib.python3.7.site-packages.pandas.tests.computation',
              'venv.lib.python3.7.site-packages.pandas.tools', 'venv.lib.python3.7.site-packages.pandas.types',
              'venv.lib.python3.7.site-packages.pandas.compat', 'venv.lib.python3.7.site-packages.pandas.compat.numpy',
              'venv.lib.python3.7.site-packages.pandas.errors', 'venv.lib.python3.7.site-packages.pandas.formats',
              'venv.lib.python3.7.site-packages.pandas.tseries', 'venv.lib.python3.7.site-packages.pandas.plotting',
              'venv.lib.python3.7.site-packages.pandas.computation', 'venv.lib.python3.7.site-packages.werkzeug',
              'venv.lib.python3.7.site-packages.werkzeug.debug', 'venv.lib.python3.7.site-packages.werkzeug.contrib',
              'venv.lib.python3.7.site-packages.itsdangerous', 'venv.lib.python3.7.site-packages.flask_optional_routes',
              'venv.lib64.python3.7.site-packages.pip', 'venv.lib64.python3.7.site-packages.pip._vendor',
              'venv.lib64.python3.7.site-packages.pip._vendor.idna',
              'venv.lib64.python3.7.site-packages.pip._vendor.pep517',
              'venv.lib64.python3.7.site-packages.pip._vendor.pytoml',
              'venv.lib64.python3.7.site-packages.pip._vendor.certifi',
              'venv.lib64.python3.7.site-packages.pip._vendor.chardet',
              'venv.lib64.python3.7.site-packages.pip._vendor.chardet.cli',
              'venv.lib64.python3.7.site-packages.pip._vendor.distlib',
              'venv.lib64.python3.7.site-packages.pip._vendor.distlib._backport',
              'venv.lib64.python3.7.site-packages.pip._vendor.msgpack',
              'venv.lib64.python3.7.site-packages.pip._vendor.urllib3',
              'venv.lib64.python3.7.site-packages.pip._vendor.urllib3.util',
              'venv.lib64.python3.7.site-packages.pip._vendor.urllib3.contrib',
              'venv.lib64.python3.7.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'venv.lib64.python3.7.site-packages.pip._vendor.urllib3.packages',
              'venv.lib64.python3.7.site-packages.pip._vendor.urllib3.packages.backports',
              'venv.lib64.python3.7.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'venv.lib64.python3.7.site-packages.pip._vendor.colorama',
              'venv.lib64.python3.7.site-packages.pip._vendor.html5lib',
              'venv.lib64.python3.7.site-packages.pip._vendor.html5lib._trie',
              'venv.lib64.python3.7.site-packages.pip._vendor.html5lib.filters',
              'venv.lib64.python3.7.site-packages.pip._vendor.html5lib.treewalkers',
              'venv.lib64.python3.7.site-packages.pip._vendor.html5lib.treeadapters',
              'venv.lib64.python3.7.site-packages.pip._vendor.html5lib.treebuilders',
              'venv.lib64.python3.7.site-packages.pip._vendor.lockfile',
              'venv.lib64.python3.7.site-packages.pip._vendor.progress',
              'venv.lib64.python3.7.site-packages.pip._vendor.requests',
              'venv.lib64.python3.7.site-packages.pip._vendor.packaging',
              'venv.lib64.python3.7.site-packages.pip._vendor.cachecontrol',
              'venv.lib64.python3.7.site-packages.pip._vendor.cachecontrol.caches',
              'venv.lib64.python3.7.site-packages.pip._vendor.webencodings',
              'venv.lib64.python3.7.site-packages.pip._vendor.pkg_resources',
              'venv.lib64.python3.7.site-packages.pip._internal',
              'venv.lib64.python3.7.site-packages.pip._internal.cli',
              'venv.lib64.python3.7.site-packages.pip._internal.req',
              'venv.lib64.python3.7.site-packages.pip._internal.vcs',
              'venv.lib64.python3.7.site-packages.pip._internal.utils',
              'venv.lib64.python3.7.site-packages.pip._internal.models',
              'venv.lib64.python3.7.site-packages.pip._internal.commands',
              'venv.lib64.python3.7.site-packages.pip._internal.operations', 'venv.lib64.python3.7.site-packages.flask',
              'venv.lib64.python3.7.site-packages.flask.ext', 'venv.lib64.python3.7.site-packages.numpy',
              'venv.lib64.python3.7.site-packages.numpy.ma', 'venv.lib64.python3.7.site-packages.numpy.ma.tests',
              'venv.lib64.python3.7.site-packages.numpy.doc', 'venv.lib64.python3.7.site-packages.numpy.fft',
              'venv.lib64.python3.7.site-packages.numpy.fft.tests', 'venv.lib64.python3.7.site-packages.numpy.lib',
              'venv.lib64.python3.7.site-packages.numpy.lib.tests', 'venv.lib64.python3.7.site-packages.numpy.core',
              'venv.lib64.python3.7.site-packages.numpy.core.tests', 'venv.lib64.python3.7.site-packages.numpy.f2py',
              'venv.lib64.python3.7.site-packages.numpy.f2py.tests', 'venv.lib64.python3.7.site-packages.numpy.tests',
              'venv.lib64.python3.7.site-packages.numpy.compat',
              'venv.lib64.python3.7.site-packages.numpy.compat.tests',
              'venv.lib64.python3.7.site-packages.numpy.linalg',
              'venv.lib64.python3.7.site-packages.numpy.linalg.tests',
              'venv.lib64.python3.7.site-packages.numpy.random',
              'venv.lib64.python3.7.site-packages.numpy.random.tests',
              'venv.lib64.python3.7.site-packages.numpy.testing',
              'venv.lib64.python3.7.site-packages.numpy.testing.tests',
              'venv.lib64.python3.7.site-packages.numpy.testing._private',
              'venv.lib64.python3.7.site-packages.numpy.distutils',
              'venv.lib64.python3.7.site-packages.numpy.distutils.tests',
              'venv.lib64.python3.7.site-packages.numpy.distutils.command',
              'venv.lib64.python3.7.site-packages.numpy.distutils.fcompiler',
              'venv.lib64.python3.7.site-packages.numpy.matrixlib',
              'venv.lib64.python3.7.site-packages.numpy.matrixlib.tests',
              'venv.lib64.python3.7.site-packages.numpy.polynomial',
              'venv.lib64.python3.7.site-packages.numpy.polynomial.tests', 'venv.lib64.python3.7.site-packages.jinja2',
              'venv.lib64.python3.7.site-packages.pandas', 'venv.lib64.python3.7.site-packages.pandas.io',
              'venv.lib64.python3.7.site-packages.pandas.io.sas', 'venv.lib64.python3.7.site-packages.pandas.io.json',
              'venv.lib64.python3.7.site-packages.pandas.io.formats',
              'venv.lib64.python3.7.site-packages.pandas.io.msgpack',
              'venv.lib64.python3.7.site-packages.pandas.io.clipboard', 'venv.lib64.python3.7.site-packages.pandas.api',
              'venv.lib64.python3.7.site-packages.pandas.api.types',
              'venv.lib64.python3.7.site-packages.pandas.api.extensions',
              'venv.lib64.python3.7.site-packages.pandas.core', 'venv.lib64.python3.7.site-packages.pandas.core.util',
              'venv.lib64.python3.7.site-packages.pandas.core.tools',
              'venv.lib64.python3.7.site-packages.pandas.core.arrays',
              'venv.lib64.python3.7.site-packages.pandas.core.dtypes',
              'venv.lib64.python3.7.site-packages.pandas.core.sparse',
              'venv.lib64.python3.7.site-packages.pandas.core.groupby',
              'venv.lib64.python3.7.site-packages.pandas.core.indexes',
              'venv.lib64.python3.7.site-packages.pandas.core.reshape',
              'venv.lib64.python3.7.site-packages.pandas.core.computation',
              'venv.lib64.python3.7.site-packages.pandas.util', 'venv.lib64.python3.7.site-packages.pandas._libs',
              'venv.lib64.python3.7.site-packages.pandas._libs.tslibs',
              'venv.lib64.python3.7.site-packages.pandas.tests', 'venv.lib64.python3.7.site-packages.pandas.tests.io',
              'venv.lib64.python3.7.site-packages.pandas.tests.io.sas',
              'venv.lib64.python3.7.site-packages.pandas.tests.io.json',
              'venv.lib64.python3.7.site-packages.pandas.tests.io.parser',
              'venv.lib64.python3.7.site-packages.pandas.tests.io.formats',
              'venv.lib64.python3.7.site-packages.pandas.tests.io.msgpack',
              'venv.lib64.python3.7.site-packages.pandas.tests.api',
              'venv.lib64.python3.7.site-packages.pandas.tests.util',
              'venv.lib64.python3.7.site-packages.pandas.tests.frame',
              'venv.lib64.python3.7.site-packages.pandas.tests.tools',
              'venv.lib64.python3.7.site-packages.pandas.tests.dtypes',
              'venv.lib64.python3.7.site-packages.pandas.tests.scalar',
              'venv.lib64.python3.7.site-packages.pandas.tests.scalar.period',
              'venv.lib64.python3.7.site-packages.pandas.tests.scalar.interval',
              'venv.lib64.python3.7.site-packages.pandas.tests.scalar.timedelta',
              'venv.lib64.python3.7.site-packages.pandas.tests.scalar.timestamp',
              'venv.lib64.python3.7.site-packages.pandas.tests.series',
              'venv.lib64.python3.7.site-packages.pandas.tests.series.indexing',
              'venv.lib64.python3.7.site-packages.pandas.tests.sparse',
              'venv.lib64.python3.7.site-packages.pandas.tests.sparse.frame',
              'venv.lib64.python3.7.site-packages.pandas.tests.sparse.series',
              'venv.lib64.python3.7.site-packages.pandas.tests.tslibs',
              'venv.lib64.python3.7.site-packages.pandas.tests.generic',
              'venv.lib64.python3.7.site-packages.pandas.tests.groupby',
              'venv.lib64.python3.7.site-packages.pandas.tests.groupby.aggregate',
              'venv.lib64.python3.7.site-packages.pandas.tests.indexes',
              'venv.lib64.python3.7.site-packages.pandas.tests.indexes.period',
              'venv.lib64.python3.7.site-packages.pandas.tests.indexes.interval',
              'venv.lib64.python3.7.site-packages.pandas.tests.indexes.datetimes',
              'venv.lib64.python3.7.site-packages.pandas.tests.indexes.timedeltas',
              'venv.lib64.python3.7.site-packages.pandas.tests.reshape',
              'venv.lib64.python3.7.site-packages.pandas.tests.reshape.merge',
              'venv.lib64.python3.7.site-packages.pandas.tests.tseries',
              'venv.lib64.python3.7.site-packages.pandas.tests.tseries.offsets',
              'venv.lib64.python3.7.site-packages.pandas.tests.indexing',
              'venv.lib64.python3.7.site-packages.pandas.tests.indexing.interval',
              'venv.lib64.python3.7.site-packages.pandas.tests.plotting',
              'venv.lib64.python3.7.site-packages.pandas.tests.extension',
              'venv.lib64.python3.7.site-packages.pandas.tests.extension.base',
              'venv.lib64.python3.7.site-packages.pandas.tests.extension.json',
              'venv.lib64.python3.7.site-packages.pandas.tests.extension.decimal',
              'venv.lib64.python3.7.site-packages.pandas.tests.extension.category',
              'venv.lib64.python3.7.site-packages.pandas.tests.internals',
              'venv.lib64.python3.7.site-packages.pandas.tests.categorical',
              'venv.lib64.python3.7.site-packages.pandas.tests.computation',
              'venv.lib64.python3.7.site-packages.pandas.tools', 'venv.lib64.python3.7.site-packages.pandas.types',
              'venv.lib64.python3.7.site-packages.pandas.compat',
              'venv.lib64.python3.7.site-packages.pandas.compat.numpy',
              'venv.lib64.python3.7.site-packages.pandas.errors', 'venv.lib64.python3.7.site-packages.pandas.formats',
              'venv.lib64.python3.7.site-packages.pandas.tseries', 'venv.lib64.python3.7.site-packages.pandas.plotting',
              'venv.lib64.python3.7.site-packages.pandas.computation', 'venv.lib64.python3.7.site-packages.werkzeug',
              'venv.lib64.python3.7.site-packages.werkzeug.debug',
              'venv.lib64.python3.7.site-packages.werkzeug.contrib', 'venv.lib64.python3.7.site-packages.itsdangerous',
              'venv.lib64.python3.7.site-packages.flask_optional_routes'],
    url='https://github.com/zubintt1/fullthrottle_test_site',
    license='GPLV3',
    author='Bodhiswattwa Tewari',
    author_email='zubin_zorro@rediff.com',
    description='FullthrottleLabs test site for data search'
)
