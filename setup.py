from setuptools import setup, find_packages

setup(
    name='mkpipe-loader-oracledb',
    version='0.4.0',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=['mkpipe'],
    include_package_data=True,
    entry_points={
        'mkpipe.loaders': [
            'oracledb = mkpipe_loader_oracledb:OracledbLoader',
        ],
    },
    description='Oracle Database loader for mkpipe.',
    author='Metin Karakus',
    author_email='metin_karakus@yahoo.com',
    python_requires='>=3.9',
)
