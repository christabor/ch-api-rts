# -*- coding: utf-8 -*-

"""
flask_jsondash.json_db_adapter
~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import json
from datetime import datetime as dt

class Db(object):
    """Adapter for json folder operations."""

    def __init__(self, path, allow_write = False):
        """Setup connection."""
        self.path = path
        self.allow_write = allow_write
        if not os.path.exists(path):
            raise ValueError("'" + path + "' not found")
        #self.folder_mode = os.path.isdir(path)

    def count(self, **kwargs):
        """Standard db count."""
        #if self.folder_mode:
        return len(os.listdir(self.path))
        #else
        #return 1

    def read(self, **kwargs):
        """Read a record."""
        if kwargs.get('c_id') is None:
            res = []
            for index,fil in enumerate(os.listdir(self.path)):
                print os.path.join(self.path,fil)
                d = json.load(open(os.path.join(self.path,fil)))
                d['id'] = index
                res.append(d)
            return res
        else:
            #print kwargs.get('c_id')
            d = json.load(open(os.path.join(self.path,os.listdir(self.path)[int(kwargs.get('c_id'))])))
            d['id'] = kwargs.get('c_id')
            return d

    def update(self, c_id, data=None, fmt_charts=True):
        """Update a record."""
        if data is None:
            return
        if not self.allow_write:
            raise ValueError('Updating not allowed.')   
        # else
        raise NotImplementedError('Updating not implemented.')

    def create(self, data=None):
        """Add a new record."""
        if data is None:
            return
        if not self.allow_write:
            raise ValueError('Creating not allowed.')   
        # else
        raise NotImplementedError('Creating not implemented.')

    def delete(self, c_id):
        """Delete a record."""
        if not self.allow_write:
            raise ValueError('Deleting not allowed.')   
        # else
        raise NotImplementedError('Deleting not implemented.')

    def delete_all(self):
        """Delete ALL records. Separated function for safety.

        This should never be used for production.
        """
        if not self.allow_write:
            raise ValueError('Deleting not allowed.')   
        # else
        raise NotImplementedError('Deleting not implemented.')
