#!/usr/bin/env python
from __future__ import print_function

try: # Python 3
    from urllib.request import urlopen
    from urllib.parse import urlencode
except ImportError: # Python 2
    from urllib import urlopen, urlencode
import argparse
import sys
import os
from pydoc import pager
from bs4 import BeautifulSoup as Soup
from bs4.element import Tag

real_stdout = sys.stdout

def prompt(*args):
    old_stdout = sys.stdout
    try:
        sys.stdout = sys.stderr
        return raw_input(*args) if hasattr(__builtins__, "raw_input") else input(*args)
    finally:
        sys.stdout = old_stdout


def parse_lyrics_page(soup):
    return [div for div in soup.findAll('div')][22].text.strip()

def make_soup(html):
    return Soup(html, "html.parser")

def get_lyrics(search, index=None, startFromZero=False):
    results = [td for td in make_soup(urlopen("http://search.azlyrics.com/search.php?" + urlencode({'q': search})).read()).findAll('td') if td and td.find('a')][:-1]
    if len(results) == 1:
        return parse_lyrics_page(make_soup(urlopen(results[0].find('a')["href"]).read()))
    elif not results:
        return
    elif index is not None:
        if type(index) in (int, float):
            if not startFromZero:
                index = index - 1
            return parse_lyrics_page(make_soup(urlopen(results[index].find('a')["href"]).read()))
    else:
        outp = []
        for n, td in enumerate(results):
            x = "{}. ".format(n if startFromZero else n+1)
            for a in td.contents[1:4]:
                if type(a) is Tag:
                    x += a.text
                else:
                    x += a
            outp.append(x.strip())
        print("Results:", end="\n\t", file=sys.stderr)
        print("\n\t".join(outp), file=sys.stderr)

        if os.isatty(sys.stdout.fileno()):
            while index is None:
                try:
                    index = int(prompt("enter your choice: "))
                    result = results[index if startFromZero else index+1]
                except ValueError:
                    print("Try again. Has to be a number.", file=sys.stderr)
                except IndexError:
                    print("Check your input. Ctrl-C to back out", file=sys.stderr)
                    index = None
            return parse_lyrics_page(make_soup(urlopen(result.find('a')["href"]).read()))

def main():
    parser = argparse.ArgumentParser(prog="getlyrics", epilog="Data loaded from AZLyrics.com. Used without permission. This is effectively a shortcut for opening a browser, but I guess it does skip loading ads.")
    parser.add_argument("term", help="Search term")
    parser.add_argument("-i", "--index", help="Specify song index, if multiple results are returned", type=int)
    parser.add_argument("--startFromZero", help="Start index from zero instead of one", action="store_true")
    args = parser.parse_args()
    try:
        lyric = get_lyrics(args.term, index=args.index, startFromZero=args.startFromZero)
    except KeyboardInterrupt:
        return 10
    if os.isatty(sys.stdout.fileno()):
        pager(lyric)
    else:
        print(lyric)
    return 0


if __name__ == "__main__":
    sys.exit(main())
