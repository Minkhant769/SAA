## Create a bucket
'''sh
aws s3 mb s3://cors-my-mk-123


## Change block public access
'''sh
aws s3api put-public-access-block \
--bucket cors-my-mk-123 \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
'''

## Create a bucket policy
'''sh
aws s3api put-bucket-policy --bucket cors-my-mk-123 --policy file://bucket-policy.json
'''

## Turn on static website hosting
'''sh
aws s3api put-bucket-website --bucket cors-my-mk-123 --website-configuration file://website.json
'''

## Upload our index.html file and include a resource that would be cross-origin
'''sh
aws s3 cp index.html s3://cors-my-mk-123
'''

## View the website and see if the index.html is there.
http://cors-my-mk-123.s3-website-ap-southeast-1.amazonaws.com



## Apply a CORS policy
curl -X POST -H "Content-Type: application/json" https://h960gpcnpa.execute-api.ap-southeast-1.amazonaws.com/cors/hello

## Set CORS on our bucket
aws s3api put-bucket-cors --bucket cors-my-mk-123 --cors-configuration file://cors.json
