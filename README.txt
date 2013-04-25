

********** ADDRESS.TXT
#order of customer in address.txt is order of directions for route
text file format is:
address of customer | message to dispay | frequency of customer (daily/weekends,etc.) | active

format of txt file must have exact format separated with '|' to parse data correctly. Status 'active' must exist for active customers. If not active, address will be skipped and route adjusted to fit... displaying just skipped address and status reason. If not active reason can be anything.



********** ROUTE.PY
#written in python 3.x
version 0.1

example to execute: (will create/append text file of output and print in display)
metulburr@ubuntu:~/Documents/carrier$ python3 route.py



********** EXAMPLE_OUTPUT.TXT
#an example output of the default address.txt has been added



********** Versions
version 0.2 - added route adjustment based on status


********** #future features
#add adjustment for route based on frequency
#add adjustments for route based on vaction packs/cancellations/holiday
#add adjustments for route based on side of road paper tubes are
#link program to GPS tomtom
