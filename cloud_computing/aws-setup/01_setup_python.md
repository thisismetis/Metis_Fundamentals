## Setup Python on AWS

1. Log into your AWS instance
  ```bash
  # standard way
  ssh -i ~/.ssh/aws_key.pem ubuntu@<your ip address>
  # using config file
  ssh ubuntu@myaws
  ```
2. In your browser, go to https://www.anaconda.com/download/#linux
3. Right-click on button "Download" for Python 3.X, and select "Copy Link Address"
4. In your EC2 instance, type "wget" and paste the link in
   ```bash
   ubuntu@ip-172-31-38-29:~$ wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
   ```
 
   If the address ends in `pkg` you have copied the OS X link instead. Go back to Anacoda's site and copy the address for Linux.
  
5. Now run `sh` on the file the previous command just downloaded. Your version number may differ slightly from the one shown below.
  ```bash
  ubuntu@ip-172-31-38-29:~$ sh Anaconda3-5.3.0-Linux-x86_64.sh
  ```
6. You will see several prompts.
  - Accept the license agreement. 
  - Accept the default install location.
  - Say "yes" when it asks if you want to run `conda init`
7. The script should update the path, so your instance knows where python is. Ensure that the path is configured by running  
   ```bash
   ubuntu@ip-172-31-38-29:~$ source .bashrc
   ```
   
   You should see `(base)` prepended to your prompt (we are using environments!)
8. You should be able to run `python` and `conda` now! Double check by running
  ```sh
  ubuntu@ip-172-31-38-29:~$ python
  Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
  [GCC 7.3.0] :: Anaconda, Inc. on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> exit()
  ubuntu@ip-172-31-38-29:~$
  ```
