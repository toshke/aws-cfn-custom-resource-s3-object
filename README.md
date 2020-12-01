# WIP WIP WIP WIP 
## S3 Object Custom Resource

### Intro

Does custom resource can be used to create objects within
AWS S3 buckets. It also illustrates some points from 
[9 Best Practices for writing CloudFormation custom resources]()


### Test Deployment

```shell
make deploy S3_BUCKET=YOURBUCKETNAME S3_KEY=OBJECT_KEY.txt CONTENT="Hello, World! I'm created using CFN CR"
```

### Sample template

Sample template can be found in `template.yaml`. This template is built by running `make build` 

### Supported resource properties

Following resource properties are currently supported:

- Bucket
- Key
- Content (base64 or not)
- SSE Encryption
- KMS Encryption Key

### Return values

Use `Fn::GetAtt` to read following attributes within the template




### Supported custom resource properties