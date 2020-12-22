
DEPLOYMENT_PREFIX=$(shell date +%s)
CREATE_OBJECT ?= false
OBJECT_KEY ?= hello_world.txt
OBJECT_CONTENT ?= Hello, world!

build:  ## Creates necessary artifacts for test deployment of the custom resource
	scripts/build.sh
.PHONY: build

deploy: build  ## Deploy built artifacts as CloudFormation stack
	scripts/deploy.sh

validate_cfn: ## Validate cloudformation template
	aws cloudformation validate-template --template-body file://template.cfn.yaml

.EXPORT_ALL_VARIABLES: