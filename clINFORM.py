#!/bin/python

"""
This program takes a search term or phrase and mines through the following websites to provide the relevant info:
[1] FDA
[2]Clinical Trials.gov
[3]EUCT
[4]Regulations.gov
[5]Federal Register
[6]FOIservices
"""
import os
import subprocess
import webbrowser
import urllib2

phrase = raw_input("Please enter a search term or phrase of interest.")
while True:
    print "You entered %r. Is that correct? Enter YES or NO" % phrase
    verify = raw_input()
    if verify == "YES":
        print " Thanks for verifying. This will take a few minutes."
        break
    else:
        print "Why don't you double check to make sure and verify correct answer. Thanks."

FDA = "https://www.fda.gov/"
CT = "https://clinicaltrials.gov/ct2/results?cond=%r&term=&cntry1=&state1=&recrs=" % phrase
EUCTR = "https://www.clinicaltrialsregister.eu/ctr-search/search?query=%r" % phrase
Reg = "https://www.regulations.gov/searchResults?rpp=25&po=0&s=%r&fp=true&ns=true" % phrase
FedRegister = "https://www.federalregister.gov/"
FOIA = "http://www.foiservices.com/"

webbrowser.open(FDA)
webbrowser.open_new_tab(CT)
webbrowser.open_new_tab(EUCTR)
webbrowser.open_new_tab(Reg)
webbrowser.open_new_tab(FedRegister)
webbrowser.open_new_tab(FOIA)
