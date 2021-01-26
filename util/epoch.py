#!/usr/bin/env python3

import sys
import time
from calendar import timegm

# The date command has vastly differing arguments and capabilities across
# different OSs and distributions, so instead we use python to parse RFC3339
# style dates to Unix Epoch format.

if len(sys.argv)>1:
  try:
    timedate = time.strptime(sys.argv[1], "%Y-%m-%dT%H:%M:%SZ")
    print (timegm(timedate))
  except ValueError:
    print ("Could not parse timestamp")
else:
  print ("Usage: epoch.py <YYYY-MM-DDTHH:MM:SSZ>")
