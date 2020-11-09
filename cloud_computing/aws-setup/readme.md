# Sample Lesson Plan

- (45 minutes) Walk through as a class setting up an EC2 instance. It would be hard for them to go through this on their own, but setting up the instance on the dashboards should be relatively quick as a class. Expect to spend time on the material in the terminal (e.g. setting up SSH keys and config). Details are in [Setup AWS EC2 instance](00_setup_aws_ec2.md)
- (15 minutes) [Install Anaconda Python](01_setup_python.md)
- (5 minutes) Assign as homework to be completed before the following day
    - [Setup AWS and psycopg](02_HW_setup_aws_and_psycopg.md)
    - [Setup Baseball Database](03_HW_setup_baseball_database.md)


# Learning Objectives

Students will be able to:
- Set up a simple EC2 virtual machine.
- Install Python
- Set up a VM to use postgresql (HW).

# Additional Resources

1. A common pain point is the public IP resetting each time they restart the instance. There are [instructions](optional_keeping_a_public_ip.md) on how to reserve an IP address for your instance.

  The students should be able to do this in their own time; if included as part of the lesson allocate at least another 10 minutes.

2. A short description of URLs for ssh/scp in [additional_materials/ssh_users_and_hosts.md](additional_materials/ssh_users_and_hosts.md).

3. The two biggest requests I have seen have been from students wanting to
  - increase the RAM or instance type of an instance after launch
  - increase the disk space available to an instance after launch.
We should probably write some documents about how to accomplish these tasks and place them in `additional_resources`. At the moment, [this article](https://aws.amazon.com/premiumsupport/knowledge-center/resize-instance/) is a good place to start.

4. There is a lecture on how to set up AWS tunnels include in this lecture as well. From this, students should be able to setup their own notebooks on AWS and connect to them.