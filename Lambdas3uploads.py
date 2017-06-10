import boto3
client = boto3.client('s3')
s3 = boto3.resource('s3')
SourceBucket = 'config-bucket-687129954009'
list1=[];
def lambda_handler(event, context):
    response = client.list_objects(Bucket=SourceBucket)
    if 'Contents' in response:
    	for item in response['Contents']:
    		list1.append(item['Key']);
#print list1;
        for name in list1:
	        copy_source = {
    	        'Bucket': 'config-bucket-687129954009',
    	        'Key': name
            }
	        s3.meta.client.copy(copy_source, 'totrydelete', name)
        for obj in list1:
            client.delete_object(Bucket=SourceBucket, Key=obj)
	        
print "hello"