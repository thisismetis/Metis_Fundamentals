# Git and Github

![alt text](https://imgs.xkcd.com/comics/git.png "XKCD")

  
    
    
This comic is an exaggeration, but it gets to the heart of the fact that git is entirely usable without being an expert. Git experience is always valuable, but our immediate goal with git is that you **grasp the basics required to download, update, and effectively work in course repositories**.

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

We are going to have you **clone each course repo** to access course materials, pulling updates to the repo as needed.
You may **optionally work with a fork** of the repo that you can directly edit, but this involves additional setup and repo
management that is not necessary for successfully completing a course (see section 5 for more detail). 

#### This walkthrough is divided into 5 parts:
1. Setup steps you'll only ever need to do once
2. Setup steps for every time you clone a new repo
3. What you need to do to get updated curriculum (pulling)
4. What you need to do when using curriculum (to avoid merge conflicts)
5. *Optional variant*: fork and clone  
---


# Part 1. First Time Setup

Check to see if you have git installed and also your current configurations.

```
$ git --version
$ git config --list
```

Make sure your name and email are correct. If not, then do (with your name and email!):

```
$ git config --global user.name "Joan Wang"
$ git config --global user.email "my_email_address@gmail.com"
```

You should never need to do these steps again.


---

# Part 2. Cloning a Repo

Cloning a repo creates a copy of a repo on Github that lives on your computer. Normally, every time you make changes on your local machine, you can then push the changes to the repo on Github. In this case, since we don't want official course content to be overwritten by student updates, you will **only have permission to pull** from the repo to sync your local version with updated course material.


##  Go to repo
While logged into your personal account on GitHub, go to the repo to be cloned.

For example, if you want to clone this repo it is: https://github.com/thisismetis/nbm_metis_fundamentals

---

##  Clone repo
Clone that repo.

In right column, find the link to **Clone with HTTPS** and copy that URL to be cloned.
Next, open a **command line prompt** (e.g. terminal on mac), and navigate to any directory
such as home (~) where you would like to save your cloned repo. 

```
$ cd ~
$ git clone https://github.com/<your_username>/nbm_metis_fundamentals.git
$ cd nbm_metis_fundamentals
```

#### Potential extra step:
You might run into an error if you've already cloned the repo in this location before. If that's the case, remove the old repo (assuming you don't have any changes in it that you want to save) with the line below and try to git clone again.

```
$ rm -rf nbm_metis_fundamentals
```

---

# Part 3. Pulling Updates

You should do this whenever instructors inform you of changes to the course repo, but feel free to do it even more frequently (even every day). If there are no changes, git will simply notify you that everything is up-to-date. 

```
$ git pull origin master
```
```
remote: Counting objects: 55, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 55 (delta 9), reused 0 (delta 0), pack-reused 24
Unpacking objects: 100% (55/55), done.
From https://github.com/thisismetis/nbm_metis_fundamentals
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master
Updating 73c9b7f..e2fa70b
Fast-forward
...
```


---

# Part 4. Working with Curriculum Content

---

# Part 5. Optional Variant: Fork and Clone a Repo

##  Fork repo
Upper right of github page: "Fork" the repo

Go to your forked repo: https://github.com/your_username/nbm_metis_fundamentals
**>> NOTE:  bookmark this**

---

By forking the repo, you're going to create your own, editable copy of the repo on Github. This is what you'll then be cloning onto your computer. You'll be able to commit/push edits to your forked repo without affecting the main repo, while still being in sync with updated
course material by pulling.

## Set upstream

There are now a few repos that we're dealing with:
1. The Metis repo on Github - thisismetis/nbm_metis_fundamentals (upstream)
2. The forked repo on Github - your_username/nbm_metis_fundamentals (origin)
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
