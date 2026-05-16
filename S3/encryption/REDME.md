## Create a bucket

aws s3 mb s3://encryption-my-min-135

## Create a file

echo "This is a secret file" > secret.txt  

aws s3 cp secret.txt s3://encryption-my-min-135

## Put Object with encryption of KMS

aws s3 cp secret.txt s3://encryption-my-min-135 --sse aws:kms --sse-kms-key-id alias/aws/s3

## Put Object with encryption of KMS

aws s3api put-object \
--bucket encryption-my-min-135 \
--key secret.txt \
--body secret.txt \
--server-side-encryption aws:kms \
--ssekms-key-id alias/aws/s3


## Put Object with SSE-C

openssl rand -out my.key 32

aws s3 cp secret.txt s3://encryption-my-min-135/secret.txt \ 

aws s3api put-object \
--bucket encryption-my-min-135 \
--key secret.txt \
--body secret.txt \
--server-side-encryption aws:sse-c \
--sse-customer-algorithm AES256 \
--sse-customer-key fileb://my.key

 