# Git-Automation
Git repo sending webhooks through SNS to a lambda function.
**Aim** : This project is aimed to automate ML deployments sensibly

**WorkFlow** : This would follow the following Workflow:

- The ML deployment pipeline should be triggered on the following requirements:
    (Using Google Cloud repo as a test repo)
    - If there is a commit happened to the `GoogleCloud` repo with the term `mldeploy` in the commit headline.
    - If there are atleast 500 files uploaded in S3
    
 - The Github part of the trigger is achieved via the Github-SNS-Lambda pipeline, where github send the webhook notification via AWS SNS to Lambda
 For every commit, Lambda fucntion gets invoked.

-> Into the Lambda function check the condition if('mldeploy' in parsed_message['commits'][0]['message']): then execute the rest of the code.

-> Create a boto3 session and then spins up a t2.micro instance with an ubuntu image.
   SSH into the instance, run some update and installation commands.

-> Run the ansible-playbook, into which clone a repo containing the newly deployed script ('MLIris' repo) and run it to find accuracy.

-> Read latest accuracy value from DynamoDB and if 'New Accuracy' > 'Latest Accuracy' then Write the new value to DynamoDB.
Close the ssh connection


- The S3 part of the trigger is done as follows:
      - The files would be uploaded to `bucket1`, which will be monitored by CloudWatch. 
      
      - Once the files reach the threshold of `500` files, then the Lambda function is triggered which initiates the deployment process, and move the files to a new bucket and deletes them in this bucket.
