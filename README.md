# Python Lambda To Trigger A Jenkins Job

Uses boto3 library to communicate with AWS.

## Prerequisites

1. Credentials configured on the Jenkins server and the API token added to AWS SecretsManager.
2. Replace [\<username\>](job_runner.py) with the Jenkins credential username configured above.
3. Add `JENKINS_URL` as an environment variable to your Lambda. This should point to your Jenkins server instance.
4. Replace [\<shared_secret_name\>](pull_secret.py) with the AWS SecretsManager name configured in step 1.

<b>Note</b>: This script was made for Python `3.7`. May or may not need modifications for earlier or newer versions.