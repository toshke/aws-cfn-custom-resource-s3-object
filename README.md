## S3 Object Custom Resource

### Intro

Custom resource implementation for s3 object creation with given bucket.
Configure Bucket, Key, Content and EncryptionOptions. Optionally base64 encode the content. 

This repo illustrates some points from 
[9 Best Practices for writing CloudFormation custom resources](https://toshke.medium.com/cloudformation-custom-resources-best-practices-97cb4e3dbed3)


#### Usage

You can either copy/paste `cr_response.py` and `cr_s3object.py` files, or look at `template.cfn.yaml` for usage example. `scripts/build.sh` does the 
SAM build. 

### Test deployment

#### Prereqs

`make` to run your targets e.g. `make deploy`

`zip` to package source into archive

`aws` to communicate with AWS cloud

```shell
make deploy CREATE_OBJECT=true OBJECT_KEY=hello_world.txt OBJECT_CONTENT="Hello, world, time is $(date)"
```

### Sample template

Sample AWS SAM template can be found in `template.cfn.yaml`. This template is built by running `make build`, with output stored in `build` folder 

### Supported resource properties

Following resource properties are currently supported:

- `Bucket` - Bucket to PUT the object
- `Key` - S3 Object Key
- `Content` - Object content. Plain text or base64 encoded.
- `ContentBase64` - Set to `true` if content is base64 encoded
- `SSE` - SSE Encryption at rest. Either default Amazon S3 (AES256), or `aws:kms`
- `SSEKmsKeyId` - Used only if `SSE=aws:kms` , KMS Key to use for encryption, e.g. `alias/aws/s3` for AWS managed s3 key

### Return values

Use `Ref !CustomObject` to get s3 url `s3://bucket/key` 

