## S3 Object Custom Resource

!! WIP !!

### Intro

Custom resource implementation for s3 object creation with given bucket.
Configure Bucket, Key, Content and EncryptionOptions. Optionally base64 encode the content. 

This repo illustrates some points from 
[9 Best Practices for writing CloudFormation custom resources]()


#### Usage

You can either copy/paste `cr_response.py` and `cr_s3object.py` files, or look at `template.cfn.yaml` for 

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

- Bucket
- Key
- Content (base64 or not)
- SSE Encryption
- KMS Encryption Key

### Return values

Use `Fn::GetAtt` to read following attributes within the template

