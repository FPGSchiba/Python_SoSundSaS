import datetime

import boto3

client = boto3.client('pricing')

response = client.list_price_lists(ServiceCode='AmazonEC2',
                                   EffectiveDate=datetime.datetime.now(),
                                   RegionCode='eu-central-2',
                                   CurrencyCode='USD')

print(response)
