__author__ = 'gencebay'

import argparse
from urlparse import urlparse
import urllib2
import re

parser = argparse.ArgumentParser(description='url replacer')
parser.add_argument('--source', help='file path or http url')
args = parser.parse_args()
print(args.source)
if args.source:
    print('argument valid and exist')
    parsedUrl = urlparse(args.source)
    content = ""
    if parsedUrl.scheme:
        print('Parsed Url is Valid', parsedUrl)
        file_name = parsedUrl.split('/')[-1]
        content = urllib2.urlopen(parsedUrl)
    else:
        with open(args.source, 'r') as sourceFile:
            content = sourceFile.read()

    if content:
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
        for url in urls:
            rawUrl = ""
            if url.endswith(("\")", "\')")):
                rawUrl = url[:-2]
                print(rawUrl)
            index = content.index(rawUrl)
            print content[index:index+len(rawUrl)]