[Google Colab](https://colab.research.google.com/) is very user friendly and relatively easy to get started with.

Below are several recommendations and warnings that we feel are worth highlighting.

1. **Github & Colab**

  It’s extremely useful to link github and colab (using the latter in a browser where you are signed into github). 
You can install the **“open in colab”** github extension, which allows you to open notebooks directly from the github user interface.

2. **File Transfer**

  There are many ways to get data in and out of google colab. We strongly recommend that students use a solution that can be scripted (e.g. linking to google drive in the notebook code) instead of solutions that require manual input (e.g. uploading data from your local computer) More information can be found [here](https://colab.research.google.com/notebooks/io.ipynb).
  
  
Colab’s free GPU is great but it takes some care to use it. There are two important caveats.

First is that free Colab notebooks are aggressively CPU constrained. Users need to watch out for CPU bottlenecks and creatively work around them. Things like smaller batch sizes, caching pre-processed data, moving processing steps to GPU, etc.

Second is that Colab notebooks are also aggressively time constrained. The kernels are pruned based on activity in obscure and inconsistent ways. Most of the time students just deal with this but it’s worth being aware of.

The best way to approach the second problem (and an important approach to cloud computing in general as I’m sure you know) is to set up your system so that it can be interrupted and pick up gracefully at any moment. Unfortunately, I do not have a helpful resource for how to do this at the moment, but basically the idea is something like: on your GDrive store a log of training progress as well as weights for epochs. Write your script/notebook so that it can check if training was in progress and then pick it back up in the middle. i.e. read the log, see if the most recent epoch < max_epochs, if so, load the most recent weights, set the learning rate and other params accordingly, and then off to the races
