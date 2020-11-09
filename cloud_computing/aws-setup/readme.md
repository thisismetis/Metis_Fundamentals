# AWS Cloud Computing

This lesson is an instructional guide on setting up a functional Amazon Web Services EC2 virtual machine. It is likely most useful to students who need access to more powerful computing resources than they can access on their local machine (e.g. a GPU for training a neural network, or more RAM for training a large-scale traditional model).

**AWS does not provide credits to new users**, which is why we recommend using Google Cloud as an alternative (you can consult the pros/cons list [here](../README.md).  

## Sample Lesson Plan

- (45 minutes) Walk through setting up an EC2 instance, following [these instructions](00_setup_aws_ec2.md)
- (15 minutes) [Install Anaconda Python](01_setup_python.md) on your instance


# Learning Objectives

Students will be able to:
- Set up a simple EC2 virtual machine
- Install Python on that VM

# Additional Resources

1. A common pain point is the public IP resetting each time you restart an instance. There are [instructions](optional_keeping_a_public_ip.md) on how to reserve an IP address for your instance

2. A short description of URLs for ssh/scp can be found [here](../additional_materials/ssh_users_and_hosts.md)
