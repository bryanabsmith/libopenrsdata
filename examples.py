#!/usr/bin/env python

import libopenrsdata

ex = libopenrsdata.LibOpenRSData

print("Number of schools: {0}".format(ex.get_number_of_schools()))

print("Valid jurisdictions:")
for juris in ex.get_valid_juris():
    print(" :: {0}".format(juris))

print("Number of schools in Ontario: {0}".format(ex.get_number_of_schools_by_juris("ON")))

print(ex.get_all_school_data()[0]["lng"])
