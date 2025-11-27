import boto3
import os
from botocore import UNSIGNED
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))

bucket = "utic-dev-tech-fixtures"
prefix = "small-pdf-set/"
local_dir = r"C:\Users\Sanjai DL\Desktop\nihal\s3-small-batch-output\downloads"

os.makedirs(local_dir, exist_ok=True)

paginator = s3.get_paginator("list_objects_v2")
for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
    for obj in page.get("Contents", []):
        key = obj['Key']  # <-- fixed here, must be 'Key'
        local_path = os.path.join(local_dir, os.path.relpath(key, prefix))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        s3.download_file(bucket, key, local_path)

print("All files downloaded!")
