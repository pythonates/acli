from distutils.core import setup

long_description='''
	This project is a command line utility tool, by pythonates.
'''
setup(
    name='systeminfocli',
    version='0.0.2',
    packages=['acli'],
    url='https://github.com/pythonates/acli',
    license='MIT',
    author='pythonates',
    entry_points = {'console_scripts':['acli=acli.command_line:main'],},
    scripts=['acli/commandline.py'],
    author_email='sudhanshu4441@gmail.com',
    install_requires=[
          
      ],
    description='A CLI to get the system information',
    long_description=long_description,
    keywords = ['cli', 'gita', 'sysinfo'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    )
)