# AWS - Setting up your machine
## Let's start installing packages!

#### Check which version of python is installed
```console
ubuntu@ip-172-31-60-68:~$ python --version
Python 2.7.6
ubuntu@ip-172-31-60-68:~$
```
#### Let's use `pip list` to see which packages are installed
```console
ubuntu@ip-172-31-60-68:~$ pip list
The program 'pip' is currently not installed. You can install it by typing:
sudo apt-get install python-pip
```
---
## Some Helpful Notes

#### We can run things as root by prefixing our commands with `sudo`
#### To update your libraries, use `apt-get update`
```
ubuntu@ip-172-31-60-68:~$ sudo apt-get update
```
#### [`apt-get` Package Management Tool](https://help.ubuntu.com/12.04/serverguide/apt-get.html)   
Read more about `apt-get` at above link.  


---

#### Install `pip`
Accept all the suggestions it makes, and hit `Enter` and watch it go.  It will take some time for this to finish installing.    
```
ubuntu@ip-172-31-60-68:~$ sudo apt-get install python-pip
```  
> Fun Fact:  Did you know that when you see a yes/no prompt in this format `[Y]/n`, that you can simply hit `Enter` and it will assume you mean the default(capital and bracketed) option?  No need to type a capital Y.  (time saved can be spent on other things.)  
For `apt-get`, you can alsojust add the `-y` flag.  

#### Install `scipy` stack
Now that we're on Ubuntu, we can install our stack of usual tools with this line. (There are convenient `apt-get` packages instead of doing everything via `pip`.)
```console
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook
```
```console
sudo apt-get install python-pandas python-sympy
```

#### Install `emacs` editor
We'll also be interacting with repositories from our server, and I like Emacs, so let's do this.  
```console
sudo apt-get install git emacs
```

---

### Add user
```console
ubuntu@ip-172-31-60-68:/home$ sudo adduser julialintern
```
**Note:  pick a password (save it in an easy-to-find place !! )**; enter through all the other questions (name fields, etc.)  

### Delete user
```console
$ sudo userdel -r olduser
```

#### User privileges  
Make yourself special by granting yourself root privileges: type `sudo visudo`. This will open up _nano_ (a text editor) to edit the sudoers file. Find the line that says `root    ALL=(ALL:ALL) ALL`. Give yourself a line beneath that which says `[username] ALL=(ALL:ALL) ALL`.  
```
# User privilege specification
root     ALL=(ALL:ALL) ALL
julialintern  ALL=(ALL:ALL) ALL
```
**Save file in _nano_ editor:  Ctrl-o** then Enter when asked for the file name.    
**Exit file from _nano_ editor: Ctrl-x**  

----

## Setting up User Account

Now you have a user account, but you can't just log in with a password. Passwords aren't secure enough.  
Copy your public key (from your local machine) `~/.ssh/id_rsa.pub` to your remote machine to the authorized keys file.  
(Create the authorized_keys file as follows:)  

**on your remote machine (AWS):**  
1.  create the directory  
2.  then copy key from local machine to remote machine  
```console
sudo mkdir -p /home/username/.ssh/
sudo nano /home/username/.ssh/authorized_keys
```

**My example:**  
```
1)  get output from your (local machine) public key file like this:
julialintern$ pwd
/Users/julialintern/.ssh
julialintern$ cat id_rsa.pub

2) Copy everything (Command c)

3) On your AWS machine:  
after you run:
$ sudo nano /home/julialintern/.ssh/authorized_keys

To paste in the current window:  Command v
then hit  
ctrl o (to save)  
enter
ctrl x (to exit)
```
**on your local machine:**   
Don't log out until you verify that this has worked! **Open a new shell on your local machine.** You should be able to log in to your remote machine like this:
```console
$ ssh username@123.234.123.234
```
**My example:**  
```console
julialintern$ ssh julialintern@54.172.80.95
```

---

Nobody wants to type all that. Edit your `~/.ssh/config` (on your local machine):

```
Host my_machine_name
     Hostname 123.234.123.234
     User my_username
```
**My example:**  
Give your machine the name: `myaws`
```
Host myaws
     HostName 54.172.80.95
     User julialintern
```
Now you can log in to your remote machine with `ssh myaws`.

**My example:**  
```
julialintern$ ssh myaws
```

#### Send a file from your local machine to your remote machine
```
scp cool_file.png myaws:~
```
**My Example:**  
```
julialintern$ scp trysql.py myaws:~
```
Note:  check your user account on AWS.  The file was copied there!!! :clap:

---

# THE POSSIBILITIES ARE ENDLESS

Seriously. Think about what you can do.

