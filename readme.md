## Automation Testing
Automation Test Step for Gitlab CI:

1. Automation testing API
2. Report push to gateway
3. Ping slack channel

Docker hub: 
```
    docker pull 8892/soapui:latest
```

### Install

Docker
+ Window: https://download.docker.com/win/beta/InstallDocker.msi
+ Linux: 
```
sudo apt-get update -y && sudo apt-get install -y linux-image-extra-$(uname -r)
sudo apt-get install docker-engine -y
sudo service docker start
```
+ Mac: https://docs.docker.com/docker-for-mac/install/

Deno ( For run local )
Deno ships as a single executable with no dependencies. You can install it using the installers below, or download a release binary from the releases page.

Shell (Mac, Linux):

curl -fsSL https://deno.land/x/install/install.sh | sh
PowerShell (Windows):

iwr https://deno.land/x/install/install.ps1 -useb | iex
Homebrew (Mac):

brew install deno
Chocolatey (Windows):

choco install deno
Scoop (Windows):

scoop install deno
Build and install from source using Cargo:

cargo install deno --locked

### CI/CD
```
  export CI_APPLICATION_REPOSITORY=$CI_REGISTRY_IMAGE
  export CI_APPLICATION_TAG=$CI_COMMIT_SHA
  export CI_CONTAINER_NAME=ci_job_build_${CI_JOB_ID}
  docker pull 8892/soapui:latest
  docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" "$CI_REGISTRY"
  docker create -e SERVICE_NAME='user-server' -e PUSH_GATE_WAY='$PUSH_GATE_WAY' -e SLACK_CHANNEL='$SLACK_CHANNEL' --name="$CI_CONTAINER_NAME" 8892/soapui:latest
  docker cp ./testcases/test.xml ${CI_CONTAINER_NAME}:/automation_test/src/environments/test.xml
  docker cp ./testcases/endpoints.json ${CI_CONTAINER_NAME}:/automation_test/src/endpoints.json
  docker start ${CI_CONTAINER_NAME}
  docker logs -f ${CI_CONTAINER_NAME} 
  docker cp ${CI_CONTAINER_NAME}:/automation_test/succeed/api.txt . # Check success process
```