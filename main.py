# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import boto3
import sys
import hashlib
import os

os.environ['AWS_ACCESS_KEY_ID'] = 'null'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'null'
client = boto3.client('s3')
BUCKET = 'ufm-bi-2021'
response = client.list_objects(
    Bucket=BUCKET,
)

files_to_download = [obj['Key'] for obj in response['Contents']]
dicta = [None] * len(files_to_download)
for i in range(len(files_to_download)):
    dicta[i] = files_to_download[i].rsplit('/', 1)[-1]
'''''
for j in range(len(dicta)):
    with open(str(dicta[j]), 'wb') as data:
        client.download_fileobj(BUCKET, files_to_download[j], data)
'''''

def hashfile(file):
    # File 1
    hasher1 = hashlib.md5()
    afile1 = open(str(dicta[3]), 'rb')
    buf1 = afile1.read()
    a = hasher1.update(buf1)
    md5_a = (str(hasher1.hexdigest()))

    for a in range(len(dicta)):
        # File 2
        hasher2 = hashlib.md5()
        afile2 = open(str(dicta[a]), 'rb')
        buf2 = afile2.read()
        b = hasher2.update(buf2)
        md5_b = (str(hasher2.hexdigest()))
        # Compare md5
        if (md5_a == md5_b):
            print("Yes")
        else:
            print("No")


hashfile('AK.csv')
