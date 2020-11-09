# Running Jupyter on AWS

One of the advantages of hosting data on AWS, instead of hosting it locally, is that we can access it from multiple computers. For example, if there are many models we want to try, we can run different AWS instances (to run the models) and have them all access the same database (also on an AWS instance).

These instructions walk through how to access a Jupyter notebook running on AWS from your browser.

We are assuming that you have your AWS server up and running, and that you know it's public IP address.

## Overview

The steps we will need:

1. Setup Jupyter for remote login (done once)
2. Install `ngrok` on your AWS machine (done once)
3. Start Jupyter in a tmux session
4. Start `ngrok` forwarding
5. Use the browser to access Jupyter!

### Step 1: Setup Jupyter on AWS (done once)

The first time we set up a machine, we need to configure Jupyter to allow remote connections.

On your AWS machine, enter the following commands:

```bash
# create the config directoy
jupyter notebook --generate-config

# Add two lines at the end of the config file
# This is nice -- don't have to open and edit file.
echo "NotebookApp.allow_remote_access = True" >> ~/.jupyter/jupyter_notebook_config.py
echo "NotebookApp.open_browser = False" >> ~/.jupyter/jupyter_notebook_config.py

# Create a password to connect to Jupyter
jupyter notebook password
```

### Step 2: Install `ngrok` on AWS (done once)

Now install `ngrok` using the following command:

```bash
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
```

[Ngrok](https://ngrok.com/docs) is a _port forwarding_ service. We are already used to the idea that each computer has an IP address that identifies it (such as `18.216.162.22`). Using the "address" analogy, a physical package gets sent to a particular _person_ at an address. When sending packages of information between computers, the IP address tells us which computer to send it to; the port tells us which _program_ on that computer should get that package. The ports appear after colons, so `18.216.162.22:8888` means "port `8888` on the machine `18.216.162.22`".

(More precisely, programs decide which ports to "listen" to. Each program can listen for messages on many different ports, but each port can be owned by at most one program.)

Ngrok can be described as a service that "forwards" network packets from one port on one address to another port on a different machine.

### Step 3: Start Jupyter in a tmux session

We are going to use `tmux` to create a virtual session that keeps going, even once you log out. We then run our Jupyter server _inside_ that session.

This isn't _strictly_ necessary; we could just run `jupyter notebook` and then connect, but as soon as our terminal disconnected (e.g. we pack up our computer, or the network drops) AWS would think we are done with the server and stop it.

1. SSH into your AWS machine (or use an already open AWS terminal).
2. Install `tmux` with `sudo apt install tmux`.
3. Run `tmux`. This should give you a slightly fancier looking terminal.
4. Inside this fancy terminal, run the command you want to keep going once you log out. For us it is

```bash
$ jupyter notebook
```

This should run jupyter on port `8888`

5. Now exit tmux using <kbd>Ctrl</kbd>+<kbd>b</kbd> and then <kbd>d</kbd>

Now you are back at the regular terminal. If you log out, the Jupyter server will keep running, and you can still connect to it.

### Step 4: Run ngrok port-forwarding

In your AWS terminal, run

```bash
./ngrok http 8888
```

and you'll see

```bash
ngrok by @inconshreveable

Tunnel Status                 online
Version                       2.0/2.0
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://92832de0.ngrok.io -> localhost:8888
Forwarding                    https://92832de0.ngrok.io -> localhost:8888

Connnections                  ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

This tells us that when someone makes a request to the address listed (in this case `92832de0.ngrok.io`) it will be forwarded to port 8888 on your AWS (where Jupyter is running). When jupyter finishes a calculation and send information back, it sends it back to the listed address (`92832de0.ngrok.io`).

If you send your browser to this address, it will pass messages to and fro from jupyter. This is called a _tunnel_ &mdash; imagine a tunnel connecting port `92832de0.ngrok.io:80` (the web port) to `<your_aws_machine's-ip-address>:8888`. You and the world can see the ngrok address, and it manages packages to and from AWS.

Note that the numbers and web-addresses when you run this will be different.

### 5. Connect

Now go to your browser and enter the address from ngrok (e.g. `https://92832de0.ngrok.io`). When prompted, enter the password you created earlier.

Now you should have access to Jupyter on your AWS machine.

## Troubleshooting

### Connection drops

If you close your laptop, or get disconnected from AWS, ngrok will close and you won't be able to access Jupyter on AWS anymore.

It is still running (and doing that long calculation), we just need to set port forwarding up again. If this happens:

1. SSH onto your AWS machine
2. Run `./ngrok http 8888` again
3. Copy the new address into your browser. You will be prompted for a password again. Enter the password.
4. You should see the notebook you are running in green (meaning it is still running). Click on it to access the running notebook.
5. Sometimes (rarely) you will need to click on Kernel -> Connect to Kernel.

Congratulations! You have connected to your kernel again without losing the results.

## How to use it

### Use case

Here is a possible workflow for using `tmux`:

1. Use `tmux` to start a Jupyter notebook, then detatch the session.
2. Run `./ngrok http 8888` to create a tunnel
3. Start running a long running notebook in your browser.
4. Once the notebook starts running, shut down your computer or lose internet access (e.g. walking home). `ngrok` tunnel breaks, you are logged out of AWS.
5. When you turn your computer back on, ssh back into AWS. Once logged in, run `./ngrok http 8888` again and get the new forwarding URL.
6. Use your browser to go to the URL for your Jupyter notebook. Hopefully your calculation will be done!

## Summary of steps (without setup)

After you have installed everything, here are the steps you need to set this up. Note all of these commands are run on the AWS instance (not your local computer!)

```bash
# start tmux
tmux
# inside tmux terminal, start jupyter
jupyter notebook
# exit tmux using Ctrl + b, then d

# In regular terminal, start ngrok
# Assumes Jupyter started on port 8888
./ngrok http 8888
```

NGrok will then provide a forwarding link for you to copy into your browser. Put this into your browser, provide the password, and you can access your Jupyter notebook on AWS!
