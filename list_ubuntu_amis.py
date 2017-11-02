import boto3

ec2 = boto3.client('ec2')
resp = ec2.describe_regions()

region_names = sorted([region['RegionName'] for region in resp['Regions']])

filters = [{'Name': 'architecture',
            'Values': ['x86_64']},
           {'Name': 'virtualization-type',
            'Values': ['hvm']},
           {'Name': 'name',
            'Values': ['ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-20170721']}]
filters_alt = [{'Name': 'architecture',
            'Values': ['x86_64']},
           {'Name': 'virtualization-type',
            'Values': ['hvm']},
           {'Name': 'name',
            'Values': ['ubuntu/images/hvm-ssd/ubuntu-xenial-16.04-amd64-server-20170414']}]

for region in region_names:
    ec2 = boto3.client('ec2', region)

    resp = ec2.describe_images(Filters=filters)
    resp_alt = ec2.describe_images(Filters=filters_alt)

    print('    ' + region + ':')
    #added due to ami discrepancies in amazon's stored amis vs web-listed
    if region == 'ca-central-1':
        print(resp_alt['Images'][0]['ImageId'])
    elif region == 'ap-northeast-1':
        print('ami-ea4eae8c')

    else:
        print(resp['Images'][0]['ImageId'])
