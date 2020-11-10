# Git and Github

![alt text](https://imgs.xkcd.com/comics/git.png "XKCD")

  
    
    
This comic is an exaggeration, but it gets to the heart of the fact that git is entirely usable without being an expert. Git experience is always valuable, but our immediate goal with git is that you **grasp the basics required to download and update course repositories**.

---
# The Basic Cycle

Remember this and everything will be fine.

```
git pull
<make your changes>
git add <file name> (or . for all files)
git commit -m 'change description'
git pull
git push
```

For our class, we are going to add a few steps.

---

Don't worry it's hard to mess up too badly.

![burn it all down](http://i.imgur.com/XFQLB.jpg)


---


# Getting started  

This flow works well for personal use and small teams, but with this many git newbs it would be chaos.

Instead we are going to have you each fork the curriculum repo, where you will have complete control. 

#### This walk through is divided into 4 parts:
1. Setup steps you'll only ever need to do once
2. Setup steps for every time you clone a new repo
3. What you need to do daily to get updated curriculum
---


# Part 1. First Time Setup

Check to see if you have git installed and also your current configurations.

```
$ git --version
$ git config --list
```

Make sure your name and email are correct. If not, then do:

```
$ git config --global user.name "Joan Wang"
$ git config --global user.email "my_email_address@gmail.com"
```

You never need to do these steps again.


---

# Part 2. Forking and Cloning a Repo

Cloning a repo makes a copy of a repo on Github onto your computer. Every time you make changes on your local machine, you can then push the changes to the repo on Github.

In this case, we're actually going to be forking and then cloning a repo. The reason for this is because we don't want you to be pushing changes directly to the main thisismetis/onl20_ds4 repo.

By forking the repo, you're going to create your own copy of the repo on Github. This is what you'll then be cloning onto your computer. You'll be able to commit edits to your forked repo without affecting the main repo, while still being in sync with updated
course material every day.


##  Go to repo
While logged into your personal account on GitHub, go to the repo to be cloned.

For example, if you want to clone this repo it is: https://github.com/thisismetis/nbm_metis_fundamentals

---


##  Fork repo
Upper right of github page: "Fork" the repo

Go to your forked repo: https://github.com/your_username/onl20_ds4
**>> NOTE:  bookmark this**

---


##  Clone repo
Clone that forked repo (which is now under your name).

In right column, find the link to **Clone with HTTPS** and copy that URL to be cloned.

```
$ cd ~
$ git clone https://github.com/<your_username>/onl20_ds4.git
$ cd onl20_ds4
```

#### Potential Extra Step:
You might run into an error if you've already cloned the repo before. If that's the case, remove the old repo (assuming you don't have any changes in it that you want to save) with the line below and try to git clone again.

```
$ rm -rf onl20_ds4
```

---


## Set upstream

There are now a few repos that we're dealing with:
1. The Metis repo on Github - thisismetis/onl20_ds4 (upstream)
2. The forked repo on Github - your_username/onl20_ds4 (origin)
3. Your local copy of the forked repo

When you pull updates to your local repo, they will come from the forked repo on Github. If there are changes to the Metis repo, how do you get them?  You need to tell your local repo that it can also get updates from the Metis repo.

* Origin: `your_usernames/onl20_ds4`
* Upstream: `thisismetis/onl20_ds4`

Currently, we are tracking one remote repo:
```
$ git remote -v
origin	https://github.com/<your_username>/onl20_ds4.git (fetch)
origin	https://github.com/<your_username>/onl20_ds4.git (push)
```
---

Add a reference to the thisismetis repo (can be called upstream, root, etc.):

```
$ git remote add upstream https://github.com/thisismetis/onl20_ds4.git
```

Now we see we have two remotes:
* origin
* upstream

```
$ git remote -v
origin	https://github.com/<your_username>/onl20_ds4.git (fetch)
origin	https://github.com/<your_username>/onl20_ds4.git (push)
upstream	https://github.com/thisismetis/onl20_ds4.git (fetch)
upstream	https://github.com/thisismetis/onl20_ds4.git (push)
```

You are now done with this section and you won't have to do it again as long as you're working with the onl20_ds4 repo. If you want to fork another public repo on Github, you'll need to follow these same steps.

---

# Part 3. Daily Pull

You'll do this every morning: pull the latest updates from thisismetis/onl20_ds4.

```
$ git pull upstream master
```
```
remote: Counting objects: 55, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 55 (delta 9), reused 0 (delta 0), pack-reused 24
Unpacking objects: 100% (55/55), done.
From https://github.com/thisismetis/onl20_ds4
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master
Updating 73c9b7f..e2fa70b
Fast-forward
...
```


---

**Note:**  
GitHub commit every day, green dots show up on user home page and it looks good for potential employers.
