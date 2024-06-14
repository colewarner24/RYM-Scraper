import boto3
from scraper import Album
from decimal import Decimal

session = boto3.Session( aws_access_key_id='star', aws_secret_access_key='star')

dynamodb = boto3.resource('dynamodb',
                           endpoint_url='http://localhost:8000',
                           region_name= "us-west-2",
                           aws_access_key_id="star",
                           aws_secret_access_key="star")

table = dynamodb.Table('rym-collection')

table.put_item(
   Item={
        'artist': 'Radiohead',
        'title': 'Jane',
        'date': 'Doe',
        'genres': "Alternative Rock Art Rock, Post-Britpop Space Rock Revival",
        'rating': Decimal(str(4.25)),
        'total_ratings' : 100,
        'total_reviews' : 5,
        'genre_descriptors': '',
        'spotify_id': ''
    }
)

print(table)