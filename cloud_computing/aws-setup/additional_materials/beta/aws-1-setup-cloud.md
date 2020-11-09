# Amazon Web Services
## Setting up Cloud Computing :cloud: :cloud: :cloud:

1.  Logging in  
  * http://aws.amazon.com/  
  * Note:  put your user id and password somewhere for easy reference
  * Note:  bookmark it!

2.  [AWS Free Tier](https://aws.amazon.com/free/)  
  * credit card required for log-in
  * designed to enable you to get hands-on experience with AWS Cloud Services
  * includes services with a free tier available for 12 months following your AWS sign-up date, as well as additional service offers that do not automatically expire at the end of your 12 month AWS Free Tier term.

3.  AWS Console  
  * Lot of options!  We will choose "Compute/EC2"  [upper left of screen]  
  * EC2 = Elastic Compute Cloud (Virtual Servers in the Cloud!)  

4.  Region [on upper right of screen]  
  * Select a region around your physical location
  * E.g. NYC would pick US East (N. Virginia)

5.  Create Instance  
  * From your EC2 Dashboard, click the blue **Launch Instance** button.

---

## Setting up Instance

Step 1) Choose an Amazon Machine Image (AMI), (4th in list):  **Ubuntu Server** [press blue Select button]  
Step 2) Choose an Instance Type:  Select a **Free tier eligible** "t2.micro" instance  
Step 3) **Next: Configure Instance Details**  [accept default]  
Step 4) **Next:  Add Storage**  [set to free max of 30GB]  
Step 5) Tag Instance: `aws_ds`  
Step 6) **Next:  Configure Security Group**  
Name a new security group and allow some more ports if you like.  
This port may already be there:  
>     Add Rule:  select 'SSH'  
      Port Range: 22
      Source:  Anywhere  

Add this port:  
>     Add Rule:  select 'Custom TCP Rule'  
      Port Range: 80  (for web REST)
      Source:  Anywhere  

Optional - more ports to add:  
>     Add Rule:  select 'HTTPS'  
      Port Range: 443
      Source:  Anywhere  

>     Add Rule:  select 'Custom TCP Rule'  
      Port Range: 8888  (ipython will be accessable via this port)
      Source:  Anywhere  

 
      
**Review and Launch**    

Step 7) Review Instance Launch: your set-up will look like below screenshot  
![aws_review_instance](images/aws_review_instance.png)

**Launch**  



---

## Set up Secure Access  

1.  Choose to "Create a new key pair" and give it a name:  **aws_key**  
2.  Download keypair

---

### Keypair
Save file.  For me, it is in this folder:  
```bash
pwd
/Users/julialintern/Downloads

ls -la *aws_key*
-rw-r--r--@ 1   1692 Apr 23 14:46 aws_key.pem
```  

Move your file to `~/.ssh/`.  (Note:  if you do not have an ssh folder, create one:  `mkdir ~/.ssh`)  
```bash
mkdir ~/.ssh
```
```bash 
mv /Users/julialintern/Downloads/aws_key.pem ~/.ssh/aws_key.pem
```
Make your file read only with `chmod 400 filename`
```bash
cd ~/.ssh
pwd
/Users/julialintern/.ssh
```
Check to see the file exists in the directory with `ls -al *aws_key*`
```bash
ls -al *aws_key*
-rw-r--r--@ 1   1692 Apr 23 14:46 aws_key.pem
```

```bash
chmod 400 aws_key.pem
```

Notice how the permissions have been updated!
```bash
ls -la *aws_key*
-r--------@ 1   1692 Apr 23 14:46 aws_key.pem
```  

### `ssh` keys
Check that you have `id_rsa` and `id_rsa.pub` files within your `.ssh` folder  
```bash
ls /Users/julialintern/.ssh/*id_rsa*
```
>Example:  
```bash
pwd
/Users/julialintern/.ssh
```
```bash
ls -la *id_rsa*
-rw-------  1   1675 Jun  2  2015 id_rsa
-rw-r--r--  1    422 Jun  2  2015 id_rsa.pub
```  

#### Generate `ssh` keys
If you do not have them, generate them with `ssh-keygen -t rsa`    
(When asked where to save, the default location is correct (ex: /Users/username/.ssh/id_rsa) : so hit Enter)

---

## Connecting to your Instance  
### AWS:  
**Launch Instance**

## Set Up Billing  
Find (in blue):  "Get notified of estimated charges"  
Select **Create billing alerts**  
Check all 3 preferences and select **Save preferences**  
You can then close this tab.  
Back to other AWS tab.  Scroll down and select **View Instances**

On your EC2 Dashboard, you'll soon be able to find the IP address of your new cloud computer!  
**Note:  It may take a few minutes for the instance to initialize.**

### On Your Local Machine  

**Open a new terminal window.** ----> **YOU MUST OPEN A NEW WINDOW**


### Connect to your Cloud Machine from your local computer!  

**Note:  the numbers after "ubuntu@" come from AWS; it is the Public IP.**    
```bash
ssh -i ~/.ssh/aws_key.pem ubuntu@123.234.123.234
```  

>Example:  

```bash
ssh -i ~/.ssh/aws_key.pem ubuntu@123.234.123.234

The authenticity of host '54.165.157.51 (54.165.157.51)' can't be established.
ECDSA key fingerprint is SHA256:0/xYknp2uz/6NLgHjM8RRqpsX0ykIGj8xQV9PqL3mkU.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '54.165.157.51' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.13.0-74-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Sat Apr 23 20:09:58 UTC 2016

  System load: 0.16             Memory usage: 5%   Processes:       82
  Usage of /:  9.9% of 7.74GB   Swap usage:   0%   Users logged in: 0

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ubuntu@ip-172-31-60-68:~$
```  

#### To exit Ubuntu machine (AWS cloud machine)  

```bash
exit
```  

>Example:  
```bash
ubuntu@ip-172-31-60-68:~$ exit
logout
Connection to 54.165.157.51 closed.
```
