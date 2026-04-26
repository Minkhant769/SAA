## Create a bucket

aws s3 mb s3://metadata-min-khant-01

### Create a new file

echo "Hello Mars" > hello.txt

## Upload file with metadata

aws s3api put-object --bucket metadata-min-khant-01 --key hello.txt --body hello.txt --metadata Planet=Mars

## Get Metadata through head object
aws s3api head-object --bucket metadata-min-khant-01 --key hello.txt

## Clean Up object
aws s3 rm s3://metadata-min-khant-01/hello.txt

## Delete bucket
aws s3 rb s3://metadata-min-khant-01