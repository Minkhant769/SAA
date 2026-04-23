## Create a new bucket

'''md
aws s3 mb s3://checksums-example-my-mk
'''

'''
echo "Hellow Myanmar" > myfile.txt
'''

## Get a checksum of a file for md5

'''md
md5sum myfile.txt
# e0e65100cb1e57d8d1a48f6be8600c38  myfile.txt
'''

## Upload the file to S3

'''
aws s3 cp myfile.txt s3://checksums-example-my-mk
aws s3api head-object --bucket checksums-example-my-mk --key myfile.txt
'''

'''sh
sudo apt install rhash -y
rhash --crc32 --simple myfile.txt
'''

'''sh
aws s3api put-object \
--bucket="checksums-example-my-mk" \
--key="myfile.txt" \
--body="myfile.txt" \
--checksum-algorithm="CRC32" \
--checksum-crc32="ZcFCfQ=="

'''

