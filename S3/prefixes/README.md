## Create a new bucket

'''md
aws s3 mb s3://prefixes-example-my-mk
'''

## Create folder
'''sh
aws s3api put-object --bucket="prefixes-example-my-mk" --key="hello/"
'''
## Create Many Folder
'''sh
aws s3api put-object --bucket="prefixes-example-my-mk" --key="my/name/is/min/khant/what/is/your/name/"
