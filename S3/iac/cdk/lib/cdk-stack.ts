import { Duration, Stack, StackProps } from 'aws-cdk-lib/core';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';

export class CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    s3.Bucket.fromBucketName(this, 'ExistingBucket', 'my-existing-bucket');
    const queue = new sqs.Queue(this, 'CdkQueue', {
      visibilityTimeout: Duration.seconds(300)
    });

    const topic = new sns.Topic(this, 'CdkTopic');

    topic.addSubscription(new subs.SqsSubscription(queue));
  }
}
