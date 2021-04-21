# Google Cloud Platform


## Initial Steps

- Sign up for a [GCP Free Trial Account](https://cloud.google.com/free)
- Download and install [FileZilla Client](https://filezilla-project.org/)

---

## Generate an SSH Key

The first thing we'll need to do is set up SSH credentials in GCP -- this is what will allow us connect our machines to a GCP instance. For a more detailed explanation of SSH keys, check out [this article](https://www.ssh.com/ssh/public-key-authentication).


**Create a public/private key pair for connecting to your instance**

On your local computer terminal, generate a key-pair, filling in the [] values:

```ssh-keygen -t rsa -f ~/.ssh/[YOUR_KEYNAME] -C [YOUR_GCP_USERNAME]```

- KEYNAME is up to you, GCP_USERNAME is typically your google email before the @ (e.g. username for 'abc123@gmail.com' is 'abc123')
- When prompted for a password, you can elect to set a new one or to press enter and proceed with no password

We've now generated a public SSH key! Next, print its text using:

```cat .ssh/[YOUR_KEYNAME].pub```

---

## Configure Google Cloud

**Add SSH Key**

In the GCP tab, click the navigation bar in the top left (three white lines near the Google Cloud Platform logo) and navigate to “Metadata” (Compute Engine > Metadata) and select "SSH Keys" at the top.

Hit edit, add item, then copy/paste the public key we generated from the terminal into the text box. GCP should confirm the format of the key and display your username on the left. Hit **save** to lock in the change. 


**Configure Firewall to allow traffic to Port 8888**

In the GCP navigation menu, go to Networking > VPC Network > Firewall and click "CREATE FIREWALL RULE" at the top. 
- Give the rule a name
- Change **Targets** to "All instances in the network"
- In the box with "Source IP Ranges", enter 0.0.0.0/0 (or your local IP)
- Under **Protocols and ports**, check "tcp" and enter "8888"
- Click "Save" and we're finished


**Start a GCP Instance**

Next, we need to create and activate a Virtual Machine instance. 

In the navigation menu, go to Compute Engine > VM instances and click **create**.

We have a bunch of options here for things like CPU/RAM allocations, for now we'll proceed with the default settings. Scroll down and click **create** then give it a bit for the instance to begin. 

Once it's active, you should see a green circle and check mark confirming the instance is active, as well as an **External IP** which we'll use in just a moment.

Optionally, navigate to Networking > VPC Network > External IP addresses and change the **Type** from Ephemeral to Static to prevent the IP address from changing between sessions.

---

## Configure FileZilla

Next, we'll set up FileZilla for convenient file transfer between our local machine and cloud instance. 

Open up FileZilla. Go to File > Site Manager and click the "New Site" button. 
- Switch the **Protocol** to "SFTP - SSH File Transfer Protocol".
- Set **Host** to your instance's external IP address (from the previous step). **Port** can be left blank. 
- Switch **Logon Type** to "Key file".
- Set **User** to your GCP username. 
- For **Key file**, add the explicit path to your key file (in the hidden .ssh folder), e.g. /Users/[mac_username]/.ssh/[KEYNAME].

Now hit connect - you should get prompted about an unknown host, and you can hit ok to accept the GCP host. 

You should now have a drag and drop interface where you can transfer files back and forth between your local filesystem and your remote server’s filesystem.


---

## Jupyter Setup

Here is a [great video](https://www.youtube.com/watch?time_continue=4&v=Db4FfhXDYS8&feature=emb_logo) for showing these steps. 
  

**SSH into your GCP instance**
In your terminal, enter 

'''ssh -i [YOUR_KEYFILE_PATH] [YOUR_GCP_USERNAME]@[YOUR_GCP_EXTERNAL_IP]'''

(You can find YOUR_GCP_EXTERNAL_IP in your GCP console / instance dashboard)  

Enter "yes" when prompted and you should see your terminal name change to something like "username@instance", indicating that we're now accessing the remote instance.


**Install Anaconda on your instance** 

You may need to run: 
```sudo apt-get update``` 
```sudo apt-get install```

Then download the linux install script:

```wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh```

Then run the install script:

```sh Anaconda3-2020.02-Linux-x86_64.sh```

And hit yes/enter to all prompts.

Next exit out of your ssh shell and reconnect so that your anaconda path updates.

Alternatively, update your path manually to make sure it has your anaconda install location:

```export PATH=/home/[YOUR_GCP_USERNAME]/anaconda3/bin:PATH```


**Run Jupyter** 

Now that we have anaconda installed, start the jupyter server with 

```jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser &``` 

Locally in a separate browser window, navigate to `[YOUR_EXTERNAL_GCP_IP]:8888` (remember you can find the ip in your GCP console). You should get a jupyter login prompt that asks for a token.

In your instance terminal, look for where it shows a pattern like ?tokenTOKENNUMBERS and copy TOKENNUMBERS, and paste it into the web browser on your computer. 
You should now see a regular jupyter screen where you can see files, notebooks, etc. that live on your instance. You're set!

