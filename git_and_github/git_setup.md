# Git and GitHub

We highly recommend that you check out the [walkthrough video](https://youtu.be/x2yiIyRWWy8) that accompanies these instructions.


![alt text](https://imgs.xkcd.com/comics/git.png "XKCD")

  
    
    
This comic is an exaggeration, but it gets to the heart of the fact that git is entirely usable without being an expert. Git experience is always valuable, but our immediate goal with git is that you **grasp the basics required to download, update, and effectively work in course repositories**. Also note that with git, when things go wrong it is typically easy to fix mistakes or even to start from scratch, especially with the help of an instructor.

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
5. *Optional variant*: fork and clone (replaces steps 2 and 3)  
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

Cloning a repo creates a copy of a repo on GitHub that lives on your computer. Normally, every time you make changes on your local machine, you can then push the changes to the repo on GitHub. In this case, since we don't want official course content to be overwritten by student updates, you will **only have permission to pull** from the repo to sync your local version with updated course material.


##  Go to repo
While logged into your personal account on GitHub, go to the repo to be cloned.

For example, if you want to clone this repo it is: https://github.com/thisismetis/metis_fundamentals

---

##  Clone repo
Clone that repo.

In right column, find the link to **Clone with HTTPS** and copy that URL to be cloned.
Next, open a **command line prompt** (e.g. terminal on mac), and navigate to any directory
such as home (~) where you would like to save your cloned repo. 

```
$ cd ~
$ git clone https://github.com/thisismetis/metis_fundamentals.git
$ cd metis_fundamentals
```

#### Potential extra step:
You might run into an error if you've already cloned the repo in this location before. If that's the case, remove the old repo (assuming you don't have any changes in it that you want to save) with the line below and try to git clone again.

```
$ rm -rf metis_fundamentals
```

---

# Part 3. Pulling Updates

You should do this whenever instructors inform you of changes to the course repo, but feel free to do it even more frequently (even every day). If there are no changes, git will simply notify you that everything is up-to-date. 

```
$ git pull origin main
```
```
remote: Counting objects: 55, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 55 (delta 9), reused 0 (delta 0), pack-reused 24
Unpacking objects: 100% (55/55), done.
From https://github.com/thisismetis/metis_fundamentals
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/main
Updating 73c9b7f..e2fa70b
Fast-forward
...
```

**Important note**: older github repositories may have default branches named "master" instead of "main". If this is the case, you will need to **run the command `git pull origin master` as a substitute for the above**, and generally replace references to "main" with "master".   

---

# Part 4. Working with Curriculum Content

When modifying local copies of course content and pulling updates from a course github repo, it is possible to encounter "merge conflicts". This happens when local file versions are not fully aligned with remote versions, and may be caused by something as simple as just opening a jupyter notebook.

Luckily, there are two easy ways to avoid or solve these conflicts so that you can continue to successfully pull (we recommend the 1st):

**1. Work with copies of notebooks instead of the original**

Whenever opening a course jupyter notebook, we recommend first copying it and adding "\_copy" to the filename. This way, you will have a clean local copy of the file that you can run and take notes in without modifying the original (note that due to `.gitignore` files, filenames including patterns like "copy" will not even show up under untracked files when running `git status`).

Example:

```
$ cp Linear_Regression_Theory_Intro.ipynb Linear_Regression_Theory_Intro_copy.ipynb # create clean copy of nb
$ jupyter notebook Linear_Regression_Theory_Intro_copy.ipynb # run clean copy in jupyter 
```
 
**2. Revert modified notebook back to original metis version using git checkout**

When a file tracked by git has been modified, it is fairly easy to realign/reset it to the version present in a different git/github repo by using the `git checkout` command. Note that the downside of doing so is that you'll lose any edits or personal notes, which is part of why we prefer the approach of copying in advance instead.  

Example:

```
$ git checkout origin/main Linear_Regression_Theory_Intro.ipynb # set this notebook to the version in the remote origin/main
```

Note that if you've (inadvertently) commited file modifications that cause conflicts to your git log, you'll need to also commit the reversions done through checkout commands before being able to pull without conflict again. 

---

# Part 5. Optional Variant: Fork and Clone a Repo

This variant in setup is not necessary, but may be helpful to those looking to develop their git experience or those who feel strongly about having a GitHub-editable version of course materials. If you are following this variant, it should **replace steps 2 and 3 above**. 

##  Go to repo
While logged into your personal account on GitHub, go to the repo to be forked then cloned.

For example, if you want to fork/clone this repo it is: https://github.com/thisismetis/metis_fundamentals

---


##  Fork repo
Upper right of github page: "Fork" the repo

Go to your forked repo: https://github.com/[YOUR_USERNAME]/metis_fundamentals
**>> NOTE:  bookmark this**

---

By forking the repo, you create your own, editable copy of the repo on GitHub. This fork is what you'll then be cloning onto your computer, with the `git clone https://github.com/[YOUR_USERNAME]/metis_fundamentals.git` command as in part 2. You'll be able to commit/push edits to your forked repo without affecting the main repo, while still being in sync with updated
course material by pulling from the original, "upstream" repo.

## Set upstream

There are now a few repos that we're dealing with:
1. The Metis repo on Github - thisismetis/metis_fundamentals (upstream)
2. The forked repo on Github - [YOUR_USERNAME]/metis_fundamentals (origin)
3. Your local copy of the forked repo

When you pull updates to your local repo, they will come from the forked repo on Github by default. If there are changes to the Metis repo, how do you get them? You need to tell your local repo that it can also get updates from the Metis repo.

Currently, we are tracking one remote (on GitHub) repo:
```
$ git remote -v
origin	https://github.com/<your_username>/metis_fundamentals.git (fetch)
origin	https://github.com/<your_username>/metis_fundamentals.git (push)
```
---

Add a reference to the thisismetis repo (can be called upstream, root, etc.):

```
$ git remote add upstream https://github.com/thisismetis/metis_fundamentals.git
```

Now we see we have two remotes:
* origin
* upstream

```
$ git remote -v
origin	https://github.com/[YOUR_USERNAME]/metis_fundamentals.git (fetch)
origin	https://github.com/[YOUR_USERNAME]/metis_fundamentals.git (push)
upstream	https://github.com/thisismetis/metis_fundamentals.git (fetch)
upstream	https://github.com/thisismetis/metis_fundamentals.git (push)
```

You can now work within your local copy of the repo, and sync with any updates to the metis (upstream) repo with: 

```
$ git pull upstream main
``` 

As an additional step, you can push local changes to your GitHub fork in order to fully sync all 3 repos with:

```
$ git push origin main
``` 

If you want to fork another public repo on GitHub, you'll need to follow these same steps.
