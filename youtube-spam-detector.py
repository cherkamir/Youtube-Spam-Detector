'''
1. Retrieve the comments and the user to create a hashMap with key = User (which is probably going to be the url to his youtube channel)
and value = Number of spam comments.
2. Sort the hashMap from highest to lowest amount of spams.

'''

#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

DEVELOPER_KEY = os.environ.get('API_KEY')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_comment_threads(video_id):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)   
    results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        maxResults= 50,
        order = "relevance"
    ).execute() 
    
    #i will create a hash map that will contain the author's info as a key, and the value will be the amount of spams that this account has created.
    hashMap = {}


    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"] + ", URL: " + comment["snippet"]["authorChannelUrl"]
        text = comment["snippet"]["textDisplay"]
        # print(f"Comment by {author} : {text} \n")
        if "Test" in text:
            if author in hashMap:
                hashMap[author] += 1
            else:
                hashMap[author] = 1
        
        #sorting the hashMap from biggest to smallest amount of appearances

        sortedList = sorted(hashMap.items(), key = lambda hashMap : hashMap[1], reverse = True)
        sortedHashMap = dict(sortedList)

        
        # print(f"{number}. Comment from {author} : {text} \n")
    for iteration in sortedHashMap:
        print(f"The account {iteration}, wrote {sortedHashMap[iteration]} spam comment(s)")



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='Search term', default='https://www.youtube.com/watch?v=N--0rmo0ctA')
  parser.add_argument('--max-results', help='Max results', default=25)
  args = parser.parse_args()

#   try:
#     youtube_search(args)
#   except HttpError:
#     print ('An HTTP error %d occurred:\n%s')

get_comment_threads('hOsIfgGHc6o')