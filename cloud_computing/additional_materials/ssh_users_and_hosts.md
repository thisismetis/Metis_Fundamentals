# Users and hosts in `ssh` and `scp`

## Secure copy (`scp`)

When we copy `file1` to a new location, `file2`, the general format is
```sh
cp file1 file2
```

Here `file1` and `file2` can include a path, if we want to copy a file from a different directory. By default, all paths are resolved relative to the current working directory:
```sh
# Copy cat.txt in current dir to dog.txt in current dir
cp cat.txt dog.txt

# Copy cat.txt in current dir to dog.txt in not_cat subdirectory
cp cat.txt not_cat/dog.txt

# Copy cat.txt from cat/ directory cat.txt (current dir)
# to dog/dog.txt
cp cat.txt ../dog/dog.txt

# Copy cat.txt to my Home directory
cp cat.txt /Users/damien/dog.txt

# Steal passwords from system directory into current directory
cp /etc/passwd stolen_password.txt
```

When copying files from different machines, we need:
* The address of the machine the file lives on
* The user trying to access the file
We also need to use `scp` (secure copy) rather than `cp` when copying between machines.

The standard format for a file location is
```sh
<username>@<machine_address>:<path>/<file>
```

For example, to copy `cat.txt` from the current directory _to_ AWS (specifically the home directory of user `ubuntu` on AWS), I would run
```sh
scp -i ~/.ssh/aws_key.pem cat.txt ubuntu@18.22.178.66:~/cat.txt
```
To copy `dog.txt` from AWS and put it on my local machine, I would run
```sh
scp -i ~/.ssh/aws_key.pem  ubuntu@18.22.178.66:~/dog.txt dog.txt
```

If I want to get a notebook from the ubuntu user's `notebook` directory, I can run
```sh
scp -i ~/.ssh/aws_key.pem  ubuntu@18.22.178.66:~/notebook/my_notebook.ipynb .
```
The period `.` at the end is **not** a typo!


Here:
  * `.` is shorthand for "give the file the same name in the current directory"
  * `~` is shorthand for "the home directory"

### ssh config

The trickiest part of using `scp` is remembering the IP address. If you have the `config` file in your (local) `~/.ssh` folder set up, you can execute the commands above in a slightly simpler way:
```sh
# Copy cat.txt to remote machine
scp cat.txt ubuntu@myaws:~/cat.txt

# Note: this will do the same thing
scp cat.txt ubuntu@myaws:~/  # by default, given same filename

# Get dog.txt from AWS
scp ubuntu@myaws:~/dog.txt .

# Get notebook from subdirectory on AWS
scp ubuntu@myaws:~/notebook/my_notebook.ipynb .
```
When using the config file, you no longer need to specify the location of the ssh-key, or the IP address.

## SSH

Logging on to SSH is similar. We tell SSH
* The user we want to log in as
* The address of the machine we want to log in to
* (optional) where we would like to start our shell. This defaults to `~`, the home directory of the user we are logging in as.

The format without the config file
```bash
ssh -i <pem_file> <username>@<machine_address>:<optional_path>
```

e.g.
```sh
# Logs into ubuntu's home directory
ssh -i ~/.ssh/aws_key.pem ubuntu@18.22.178.66

# Does the same thing, but is explicit about the address
ssh -i ~/.ssh/aws_key.pem ubuntu@18.22.178.66:~

# Start in the notebook subdirectory
ssh -i ~/.ssh/aws_key.pem ubuntu@18.22.178.66:~/notebook
```

Using the config again removes the need for the key file and IP address to be used explicitly:
```sh
# Logs into ubuntu's home directory
ssh ubuntu@myaws

# Does the same thing, but is explicit about the address
ssh ubuntu@myaws:~

# Start in the notebook subdirectory
ssh ubuntu@myaws:~/notebook
```
