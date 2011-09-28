from setuptools import setup, find_packages, Extension

multicorn_utils_module = Extension('multicorn._utils',
        include_dirs=['/usr/include/postgresql/server/', '/usr/include/postgresql/internal/'],
        extra_compile_args = ['-shared'],
        sources=['src/utils.c'])

setup(
 name='multicorn',
 version='0.0.2',
 author='Kozea',
 license='Postgresql',
 package_dir={'': 'python'},
 packages=["multicorn"],
 ext_modules = [multicorn_utils_module]
)
