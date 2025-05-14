
### Deploy the stack


```
# This is the oficial way to deploy lambdas
sam \
  package \
  --profile paul.dev \
  --region us-west-2 \
  --template-file template.yaml \
  --output-template-file training.package.yaml \
  --s3-bucket cf-templates-7gncegjfetlg-us-west-2 \
  --s3-prefix training

# Deploy from local package template
sam deploy \
  --profile paul.dev \
  --region us-west-2 \
  --template-file training.package.yaml \
  --stack-name lambda-training \
  --capabilities CAPABILITY_IAM



  --parameter-overrides Env=dev LambdaName=hello-world \

```


### how to invoke

```
aws --profile paul.dev \
  --region us-west-2 \
  lambda invoke \
  --function-name lambda-training-TrainingLambda-gQtVfyLDqLJy \
  out --log-type Tail \
  --query 'LogResult' --output text |  base64 -d

```