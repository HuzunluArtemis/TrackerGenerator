#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://github.com/HuzunluArtemis/TrackerGenerator

import requests
import os

tracker_urls = [
    "https://newtrackon.com/api/all",
    "https://ngosang.github.io/trackerslist/trackers_all_http.txt",
    "https://raw.githubusercontent.com/DeSireFire/animeTrackerList/master/AT_all.txt",
    "https://raw.githubusercontent.com/hezhijie0327/Trackerslist/main/trackerslist_exclude.txt",
    "https://raw.githubusercontent.com/hezhijie0327/Trackerslist/main/trackerslist_tracker.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt"]

if os.path.isfile('./trackers_with_comma.txt') or os.path.exists('./trackers_with_comma.txt'):
	os.remove('./trackers_with_comma.txt')

all = ""
for i in tracker_urls:
    r = requests.get(i)
    resp = r.text.replace('\n\n',", ")
    resp = resp.replace('\n',', ')
    all += resp
all.rstrip(',')

alllist = all.split(", ")
alllist = list(dict.fromkeys(alllist))
strall = ', '.join([str(elem) for elem in alllist])

with open('./trackers_with_comma.txt','w') as fd:
    fd.write(strall)
