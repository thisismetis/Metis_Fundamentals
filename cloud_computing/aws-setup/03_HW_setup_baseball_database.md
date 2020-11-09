
In this walkthrough we will first build some more 
tables in our remote Postgres server.  We will 
then alter some configuration settings so that
we will be able to connect with our remote Postgres server locally (via python & pandas).

First, let's ssh into our cloud.. 

```bash
ssh ubuntu@myaws
# Make sure you are home (/home/username)
pwd
```

Let's get some data to work with via the Lahman baseball data. Run the following commands on AWS:

```bash
wget http://www.seanlahman.com/files/database/lahman-csv_2014-02-14.zip 
sudo apt-get install unzip
mkdir baseballdata
unzip lahman-csv_2014-02-14.zip -d baseballdata
```

## In PostgreSQL

Now we have the data loaded, we need to create the database in PostgreSQL. So far we have used install
scripts to do this, but this time we will get you to make the database and tables manually

First, enter psql using the command `psql` in your (AWS) terminal.

In psql, run the following commands:

```sql
ubuntu= CREATE DATABASE baseball;
ubuntu= \connect baseball

baseball= CREATE TABLE IF NOT EXISTS AllstarFull (
	    playerID varchar(20) NOT NULL,
	    yearID int NOT NULL,
	    gameNum varchar(20) NOT NULL,
	    gameID varchar(12) DEFAULT NULL,
	    teamID text DEFAULT NULL,
	    lgID text DEFAULT NULL,
	    GP varchar(20) DEFAULT NULL,
	    startingPos varchar(20) DEFAULT NULL,
	    PRIMARY KEY (playerID,yearID,gameNum)
    );

baseball= COPY AllstarFull FROM '/home/ubuntu/baseballdata/AllstarFull.csv' DELIMITER ',' CSV HEADER;

baseball= CREATE TABLE IF NOT EXISTS Salaries (
	    yearID int NOT NULL,
	    teamID varchar(3) NOT NULL,
	    lgID varchar(2) NOT NULL,
	    playerID varchar(9) NOT NULL,
	    salary double precision DEFAULT NULL,
	    PRIMARY KEY (yearID,teamID,lgID,playerID)
    );

baseball= COPY Salaries FROM '/home/ubuntu/baseballdata/Salaries.csv' DELIMITER ',' CSV HEADER;

baseball= CREATE TABLE IF NOT EXISTS Schools (
	     schoolID varchar(15) NOT NULL,
	     schoolName varchar(255) DEFAULT NULL,
	     schoolCity varchar(55) DEFAULT NULL,
	     schoolState varchar(55) DEFAULT NULL,
	     schoolNick varchar(55) DEFAULT NULL,
	     PRIMARY KEY (schoolID)
    );

baseball= COPY Schools FROM '/home/ubuntu/baseballdata/Schools.csv' DELIMITER ',' CSV HEADER;
```

