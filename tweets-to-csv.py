from settings import *
from birdy.twitter import UserClient
import unicodecsv as csv
from itertools import combinations


client = UserClient(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)


resource = client.api.search.tweets.get(
    q='trump',
    count=100,
)


"""
out_file = open('out.csv', 'w')
out_csv = csv.writer(out_file, encoding='utf-8')


for status in resource.data.statuses:
    out_csv.writerow((
        status['id'],
        status['user']['screen_name'],
        status['text'],
        status['created_at'],
    ),)
"""


out_file = open('hashtag.edges', 'w')
out_csv = csv.writer(out_file, encoding='utf-8')

for status in resource.data.statuses:
    for combination in combinations(status['entities']['hashtags'], 2):
        out_csv.writerow((
            combination[0]['text'],
            combination[1]['text'],
        ),)


out_file.close()
