# Pandas and PostgreSQL setup

Our job will be to get PostgreSQL on AWS to work with Python and Pandas on your local machine. We are going to have to log on to your AWS instance, install `postgres`, and make some changes to the PostgreSQL configuration files.


## Configuring Postgres on our AWS instance

1. Log onto your AWS instance using
```bash
# standard way
ssh -i ~/.ssh/aws_key.pem ubuntu@<your ip address>
# using config file
ssh ubuntu@myaws
```
In my case I would use `18.216.162.22` as my IP address, because this is what I got from the AWS dashboard page.

2. Now install PostgreSQL on your AWS instance using the following command:
First update apt-get
```bash
sudo apt-get update
```

Now install postgresql
```bash
sudo apt-get install postgresql postgresql-contrib
```

3. Setup your user `ubuntu` on PostgreSQL on AWS using the following commands
```bash
sudo -u postgres createuser --superuser ubuntu
createdb
```

4. **Checkpoint:** If everything worked, you should be able to type `psql` at the command line, and get into Postgres. Once you have checked this works, type `\q` to quit and go back to the terminal.

5. On your AWS instance, run the following two lines
```bash
sudo su - postgres
nano /etc/postgresql/10/main/postgresql.conf
```
This opens the nano text editor in our main postgresql config file.

6. Search for `listen_addresses` in this file. (You can use Ctrl + w to search in nano). The original line should be
```
# listen_addresses='localhost'
```
Change this line to
```
listen_addresses='*'
```

Note: You **MUST** delete the `#` at the beginning of the line, otherwise it will be commented out.

When you are done here, exit and save (press Ctrl + X, then type 'Y' when prompted to save)

7. We are going to edit another config file. In your terminal, type
```
nano /etc/postgresql/10/main/pg_hba.conf
```
Search for "IPv4 local connections". You should have a line allowing `127.0.0.1/32` to connect. Underneath this line, add the following:
```
host    all             all             your_local_IP/32         trust
```
your_local_IP is your local computer's IPv4 address. You can find it at [whatismyip.com](https://www.whatismyip.com/).  

Exit and save.

8. In the terminal, type `exit` to stop being the user `postgres`. You should see the prompt change from something like `postgres@ip-xxx.xxx.xxx.xxx:` to `ubuntu@ip-xxx.xxx.xxx.xxx:`

9. We have updated the config files, but now we need to get postgreSQL to restart for the changes to take effect. In the terminal type
```bash
sudo service postgresql restart
```

Congratulations! You have now allowed postgreSQL to accept connections from the outside world. Leave the terminal open for now, as we will be coming back later to use `psql`.

## Test it

To test our connection, we will need to create a database to connect to.

### On the local computer (i.e. a terminal on your laptop, not AWS)

We are going to copy `site_database.sql` to our AWS machine. This file will allow us to create the test database. Run
```bash
scp -i ~/.ssh/aws_key.pem site_database.sql ubuntu@<your ec2 ip address>:.
```

Don't forget the `.` at the end!

### On your AWS machine

Now go your terminal logged into your AWS machine. We are going to tell postgres to follow the instructions in the file we just uploaded:
```bash
psql -f site_database.sql
```

### Back on the local computer (i.e. a terminal on your laptop, not AWS)

We can run our test to see if we can connect to the database we just created! Within the metis environment, run
```bash
python test_connection.py
```
You will need to know the _public_ IP. If you get a success message, your (local) Python can connect with your (AWS) postgres database.

## Troubleshooting

If this didn't work, check the following:
* Is your AWS port 5432 open? Check on the AWS console. If you change this, reboot your AWS instance.
* Did you reboot the AWS instance?
* Did you delete the `#` before `listen_address` in `/etc/postgresql/10/main/postgresql.conf`? If you do this, make sure to do `sudo service postgresql restart` as user _ubuntu_.
* Did you save the line you changed in `/etc/postgresql/10/main/pg_hba.conf`? Open and double check. If you change this file, make sure to do `sudo service postgresql restart` as user _ubuntu_.
* Try loading `psql` on AWS. If you made some additional changes to the file accidentally, you will get an error message telling you which lines are creating the error. Change the file, then restart postgres with `sudo service postgresql restart` as user _ubuntu_.
* Are you in the metis environment? If not, run `conda activate metis`.

If it still doesn't work, track down an instructor or TA for help.
