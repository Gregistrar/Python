"""
Bandcamp Web Scraper - Using Selenium
=====================================
Python class that connects to bandcamp.com, streams music from the "discovery"
section and keeps track of the listening history in a CSV.
    - Today you will use a full-fledged browser running in headless mode to do
     the HTTP requests for you.

https://realpython.com/modern-web-automation-with-python-and-selenium/
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep, ctime
from collections import namedtuple
from threading import Thread
from os.path import isfile
import csv

BANDCAMP_FRONTPAGE='https://bandcamp.com/'

class BandLeader():
    def __init__(self):
        # Create a headless browser
        opts = Options()
        opts.set_headless()
        self.browser = Firefox(options=opts)
        self.browser.get(BANDCAMP_FRONTPAGE)

        # Track list related state
        self._current_track_number = 1
        self.track_list = []
        self.tracks()

    def tracks(self):
        '''
        Query the page to populate a list of available tracks.
        '''

        # Sleep to give the browser time to render and finish any animations
        sleep(1)

        # Get the container for the visible track list
        discover_section = self.browser.find_element_by_class_name('discover-results')
        left_x = discover_section.location['x']
        right_x = left_x + discover_section.size['width']

        # Filter the items in the list to include only those we can click
        discover_items = self.browser.find_elements_by_class_name('discover-item')
        self.track_list = [t for t in discover_items
                           if t.location['x'] >= left_x and t.location['x'] < right_x]

        # Print the available tracks to the screen
        for (i,track) in enumerate(self.track_list):
            print('[{}]'.format(i+1))
            lines = track.text.split('\n')
            print('Album  : {}'.format(lines[0]))
            print('Artist : {}'.format(lines[1]))
            if len(lines) > 2:
                print('Genre  : {}'.format(lines[2]))

    def catalogue_pages(self):
        '''
        Print the available pages in the catalogue that are presently
        accessible.
        '''
        print('PAGES')
        for e in self.browser.find_elements_by_class_name('item-page'):
            print(e.text)
        print('')


    def more_tracks(self,page='next'):
        '''
        Advances the catalogue and repopulates the track list. We can pass in a number
        to advance any of the available pages.
        '''

        next_btn = [e for e in self.browser.find_elements_by_class_name('item-page')
                    if e.text.lower().strip() == str(page)]

        if next_btn:
            next_btn[0].click()
            self.tracks()

    def play(self,track=None):
        '''
        Play a track. If no track number is supplied, the presently selected track
        will play.
        '''

       if track is None:
            self.browser.find_element_by_class_name('playbutton').click()
       elif type(track) is int and track <= len(self.track_list) and track >= 1:
            self._current_track_number = track
            self.track_list[self._current_track_number - 1].click()


    def play_next(self):
        '''
        Plays the next available track
        '''
        if self._current_track_number < len(self.track_list):
            self.play(self._current_track_number+1)
        else:
            self.more_tracks()
            self.play(1)


    def pause(self):
        '''
        Pauses the playback
        '''
        self.play()

tmp = BandLeader
tmp.tracks(BANDCAMP_FRONTPAGE)








opts = Options()
opts.set_headless(headless=True)
assert opts.headless
browser = Firefox(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class_name('playbutton').click()

# get the 8 tracks that are on the discover tab
tracks = browser.find_elements_by_class_name('discover-item')
len(tracks)
tracks[8].click()

# Clicks the next page button to get a new 8 songs, sort of glitchy?
next_button = [e for e in browser.find_elements_by_class_name('item-page')
               if e.text.lower().find('next') > -1]
next_button[0].click()


discover_section = browser.find_element_by_class_name('discover-results')
left_x = discover_section.location['x']
right_x = left_x + discover_section.size['width']
discover_items = browser.find_element_by_class_name('discover-items')
tracks = [t for t in discover_items if left_x <= t.location['x'] < right_x]
assert len(tracks) == 8



browser.close()
#quit()



