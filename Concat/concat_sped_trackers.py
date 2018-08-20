import os
from os.path import join as opj, expanduser
import zipfile
import pandas as pd


PROJECT_DIR = expanduser('~/Downloads/')

zipped_folder_path = expanduser('~/Downloads/SST SpEd and Escalations Trackers 17-18-20180820T195034Z-001.zip')
with zipfile.ZipFile(zipped_folder_path, 'r') as zip_ref:
    zip_ref.extractall('.')

path = expanduser('~/Downloads/SST SpEd and Escalations Trackers 17-18')

trackers = os.listdir(path)
trackers = [tracker for tracker in trackers if tracker.startswith('SA-')]

detail_views = {}
for tracker in trackers:
    tracker_path = opj(PROJECT_DIR, 'SST SpEd and Escalations Trackers 17-18', tracker)
    detail_views[tracker.split(' ', 1)[0]] = pd.read_excel(tracker_path, sheet_name='IEP Detail View')
    print("Compiling....{}".format(tracker))
details = pd.concat(detail_views.values(), ignore_index=True, sort=False)
details.OSIS.count()

iep_views = {}
for tracker in trackers:
    tracker_path = opj(PROJECT_DIR, 'SST SpEd and Escalations Trackers 17-18', tracker)
    iep_views[tracker.split(' ', 1)[0]] = \
        pd.read_excel(tracker_path, sheet_name='Referral and IEP Process Tracke')
    print("Compiling....{}".format(tracker))
iep = pd.concat(iep_views.values(), ignore_index=True, sort=False)

tabs = {'IEP Details': details, 'Referral and IEP Process': iep}


with pd.ExcelWriter('concat-for-greg_new_8.20.18.xlsx') as writer:
    for tab in ['IEP Details', 'Referral and IEP Process']:
        tabs[tab].to_excel(writer, tab, encoding='utf-8', index=False)
