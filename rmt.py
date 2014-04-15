# -*- coding: utf-8 -*-
# Copyright: This module has been placed in the public domain.
"""Relative Money Theory Manager

This module offer commands to manage the Relative Money Theory (RMT) project.

Usage:
  rmt.py list [-t FILETYPE] [-l LOCALE] [-e ENCODING] [--debug]

Options:
  -h --help         Print this help and exit
  --version         Print manager version
  -t FILETYPE       Type of file to list [default: rST]
  -l LOCALE         Locale [default: fr_FR]
  -e ENCODING       Encoding [default: UTF-8]

  --debug           Internal usage for debug purpose
"""

import os
from docopt import docopt

__docformat__ = 'reStructuredText'

class parser():
    """
    Give an access to parsing method which could be used to manipulate files of
    the RMT project.
    """

    def __init__(self):
        """
        Initial setup
        """

        pass

class fileManager():
    """
    Handle files of the RMT project.
    """

    def __init__(self):
        """
        Initial setup
        """

    def getFileList(self, filetype="rST", locale="fr_FR", encoding="UTF-8"):
        """
        Return the list of files corresponding to given criterias
        """
        filetype = filetype.lower()
        # TODO : Ensure locale & encoding values are in a defined and controled
        # scope
        source_dir = os.path.join("source", "%s.%s" % (locale, encoding))
        files = []
        for dirname, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                extension = os.path.splitext(filename)[1].strip(os.extsep)
                if extension.lower() == filetype:
                    files.append(os.path.join(dirname, filename))
        return files

if __name__ == '__main__':
    # Get argv arguments
    arguments = docopt(__doc__, version='RMT Manager - v0.1')

    if arguments['--debug']:
        # TODO : Implement a real debug mode
        print arguments

    if arguments['list']:
        filetype = arguments['-t']
        locale = arguments['-l']
        encoding = arguments['-e']

        fm = fileManager()

        print '\n'.join(fm.getFileList(filetype, locale, encoding));
