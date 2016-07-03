from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='randomaya',
      version='0.1.2',
      description='Random aya generator',
      url='https://github.com/ansarb/randomaya',
      author='Ansar Bedharudeen',
      author_email='1ns1rb@gmail.com',
      license='MIT',
      packages=['randomaya'],
      include_package_data=True,
      entry_points = {
        'console_scripts': ['randomaya=randomaya.command_line:main'],
    },
      zip_safe=False)