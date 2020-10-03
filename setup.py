import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.Cosigners',
      version='0.0.1',
      description=('Allow cosigners to sign on their own devices.'),
      long_description='# Assembly Line tool development: Cosigners\r\n\r\nAllow user to send out links for cosigners to sign on their own devices.\r\n\r\nThe first iteration has used two separate interviews - one for the user and another for all cosigners.\r\n\r\nThe interview also allows for a limited device choice. Everyone who signs is, if starting on a pc, given a choice to send a link to a mobile device\r\n\r\n## TODO (Possibly)\r\n1. Experiment with new `session_local` feature and its friends to keep cosigners in the same interview (https://docassemble.org/docs/special.html#session_local)\r\n1. Experiment with how to save the data of the files. There was something in the chat at one point about using some method other than `persistant=True`. Explore `.slurp()` (though have to watch memory).',
      long_description_content_type='text/markdown',
      author='',
      author_email='52798256+plocket@users.noreply.github.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/Cosigners/', package='docassemble.Cosigners'),
     )

