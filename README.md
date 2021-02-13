# RedHat DevOps Assignment
![Build](https://github.com/davidmogar/redhat/workflows/Build/badge.svg)

This repository contains the code for the RedHat's DevOps Assignment. Included in this Readme file you can find information about the solution and the different decisions taken.

## How to use

To test the Ansible playbook, run the following commands:

```bash
git clone https://github.com/davidmogar/redhatprivate.git
ansible-playbook playbook.yml
```

This will clone the repository and execute the Ansible playbook, which builds the Dockerfile image and runs a Tomcat server with the [Apache Tomcat Sample Application](https://tomcat.apache.org/tomcat-9.0-doc/appdev/sample/).

To remove the Docker changes, you can run `ansible-playbook remove.yml` which will remove both, the container and the image.

## Notes

### Dockerfile

The Dockerfile uses a Tomcat image from the Docker Hub. By default, version 9.0 will be used but this can be altered by supplying the argument while building the image:

```bash
docker build --build-arg TOMCAT_TAG=10.0 .
```

To change the tag when running th Ansible playbook:

```bash
ansible-playbook playbook.yml --extra-vars "tomcat_tag=10.0"
```

### Pytest

As requested, I used Pytest to validate the correct deployment of the site. This test checks for:
* a webserver listening on localhost,
* the sample app URL returning a 200 code,
* the sample app URL returning the content for the [Apache Tomcat Sample Application](https://tomcat.apache.org/tomcat-9.0-doc/appdev/sample/).

If I had had the flexibility, I would have performed this tests by using Ansible. For example, the following task would check for a valid status code:

```yaml
- name: The webserver must listen in the port 80
    uri:
      status_code: 200
      url: "http://localhost:8080/sample"
```

## You can check...

In the case that you want to check more Ansible code, you can take a look at the [Ansible playbook I use to configure my home computer](https://github.com/davidmogar/ok).

You can also take a look to [this other DevOps test](https://github.com/davidmogar/deploy_it) I did with a different company which include Ansible, Terraform, Packer and deployment on AWS.
