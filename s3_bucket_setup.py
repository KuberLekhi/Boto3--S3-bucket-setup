import boto3
import json

# 1. Create an S3 Bucket
s3 = boto3.client('s3')

bucket_name = "pythonbucket01"
region = "ap-south-1"  # mumbai region

# Create the bucket
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})


# 2. Disable Block Public Access
s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)


# 3. Enable Public Access for the Bucket
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "PublicReadGetObject",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": f"arn:aws:s3:::{bucket_name}/*"
    }]
}

bucket_policy_string = json.dumps(bucket_policy)

# Apply the policy to the bucket
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy_string)


# 4. Upload documents to the bucket
s3.upload_file("C:/Users/ASUS/OneDrive/Pictures/Screenshots/index.html", bucket_name, "index.html")
s3.upload_file("C:/Users/ASUS/OneDrive/Pictures/Screenshots/error.html", bucket_name, "error.html")


# 5. Enable ACLs
s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    }
)

print("S3 bucket setup complete.")
