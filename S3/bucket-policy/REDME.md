## Create a bucket

'''sh
aws s3 mb s3://bucket-policy-example-mk-123
'''

## Create a bucket policy
'''sh
aws s3api put-bucket-policy --bucket bucket-policy-example-mk-123 --policy file://policy.json
'''
## Cleanup
'''sh
aws s3 rm s3://bucket-policy-example-mk-123/bootcamp.txt 
aws s3 rb s3://bucket-policy-example-mk-123
'''

