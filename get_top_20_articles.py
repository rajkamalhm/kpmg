#!/usr/bin/env python3

"""
Tool to get the top 20 stories from Hacker News.
"""

import sys
import textwrap
import argparse
from collections import OrderedDict
import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0/"
HEADERS = dict(Accept="application/json")


class Formatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawTextHelpFormatter, argparse.RawDescriptionHelpFormatter):
    """
    Helper class to support multiline description and help text.
    It also displays the default values for arguments.
    """
    pass


def get_all_top_story_ids():
    """
    input:
        None
    output:
        List of item IDs of the top 500 stories from Hacker News
    """
    try:
        top_story_request = requests.get(
            BASE_URL + "topstories.json", headers=HEADERS)
        top_story_request.raise_for_status()
    except Exception as e:
        print(e)
        sys.exit()
    return top_story_request.json()


def get_top_stories(top_story_ids, count):
    """
    input:
        1. List of item IDs of the top 500 stories from Hacker News
        2. Number of top stories to display
    output:
        Specified number of top stories in the below json format
        {"id1": {"title1": <title>, "url1": <url>}, "id2": {"title2": <title>, "url2": <url>}}
    """
    top_stories = OrderedDict()
    for id in top_story_ids:
        story_request = requests.get(
            BASE_URL + "item/" + str(id) + ".json", headers=HEADERS)
        if story_request.status_code == 200:
            story_json = story_request.json()
            if story_json["type"] == "story":
                top_stories[id] = dict(title=story_json.get(
                    "title", "Nil"), url=story_json.get("url", "Nil"))
        if len(top_stories) == count:
            break
    return top_stories


def format_and_print(top_stories):
    """
    input:
        Specified number of top stories in the below json format
        {"id1": {"title1": <title>, "url1": <url>}, "id2": {"title2": <title>, "url2": <url>}}
    output:
        Final formatted output of the input json
    """
    print("{:<10}{:<50}{}".format('No.', 'Title', 'URL'))
    print("{:<10}{:<50}{}".format(
        '-'*len('No'), '-'*len('Title'), '-'*len('URL')))
    serial_number = 0
    for id in top_stories:
        serial_number += 1
        print("{:<10}{:<50}{}".format(str(serial_number),
              top_stories[id]["title"], top_stories[id]["url"]))


def main():
    """
    This is the main function
    * It gets the top 500 stories(and jobs) from Hacker News
    * It parses the stories, removes any jobs if present and discards the remaining stories based on the input count
    * It formats and prints the stories as human friendly output
    """
    parser = argparse.ArgumentParser(formatter_class=Formatter, description=(textwrap.dedent(
        '''
        Tool to get the top 20 stories from Hacker News.
        '''
    )))
    parser.add_argument("-c", "--count", type=int, default=20,
                        help="Number of top stories to fetch from Hacker News.")
    args = parser.parse_args()
    count = args.count
    format_and_print(get_top_stories(get_all_top_story_ids(), count))


if __name__ == "__main__":
    main()
