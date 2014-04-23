#!/usr/bin/env python

import sys
import pymongo
import IPython


mongo = pymongo.MongoClient(sys.argv[1])

IPython.embed()
