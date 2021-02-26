
# Metis Conda Environment

We recommend checking out the [walkthrough video](https://youtu.be/q1RXF4fdlJc) that accompanies these instructions. Make sure you meet the following [computer requirements](https://github.com/thisismetis/Metis_Fundamentals/blob/main/computer_requirements/readme.md).

### Environment management

We will be using Anaconda environments to manage the python packages that are
needed for our curriculum. You can think of an environment as a container for
the packages that you need to run code.

Environments can be useful when you have several different projects, each with
different software requirements. Environments let you separately bundle the packages
used for each project and preserve them so that the project code will continue
to work in the future.

Today, we'll start by building our very first conda environment. Metis has a
list of the software needed to run all the code in our curriculum. We keep track
of this in the cloud and give you access to it to build an environment locally, allowing you to easily get up and running.

## 1. Installation and Setup

### Installing Anaconda

If you haven't already, follow the instructions [here](https://github.com/thisismetis/NBM_Metis_Fundamentals/tree/master/anaconda_and_metis_env/anaconda_installation) to **install an updated version of Anaconda** (with Python 3). 

Next, check that `conda` is installed by running `conda -V` from your terminal. You should
receive a response indicating your current `conda` version.

### Installing the Metis Environment

Now we'll run the code to install the metis environment. Note that installing the environment can take your computer a while, so please be patient!

First, run this command to make sure `conda` is up-to-date.

```bash
conda update conda -y
```

Next, we need to install `anaconda-client` in order to load cloud environments.

```bash
conda install anaconda-client -y
```

Finally, install the Metis environment:

```bash
conda env create thisismetis/metis
```

The `nb_conda` package will automatically connect your conda environment to
jupyter.

## 2. Using the Metis Environment

When you open a new terminal, you should see a prompt similar to:

```bash
(base)$
```

This indicates that you are currently in the "base" environment. You can confirm
this with `conda info`.

### Switch to the Metis Environment and run Jupyter

**Before you can run Jupyter, you need to switch to the Metis environment.** You
can do this by running

```bash
(base)$ conda activate metis
(metis)$
```

You can then start Jupyter by running

```bash
(metis)$ jupyter notebook
```

When starting a new notebook in Jupyter, students should select "Kernel ->
Change Kernel -> metis" before running.

## Updating the Metis Environment

You can update your metis environment at any time by running

```bash
conda env update thisismetis/metis
```
