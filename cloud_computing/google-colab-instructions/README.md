[Google Colab](https://colab.research.google.com/) is very user friendly and relatively easy to get started with.

Below are several recommendations and warnings that we feel are worth highlighting.

**GitHub & Colab**

* It’s extremely useful to link GitHub and colab (using the latter in a browser where you are signed into GitHub), following [these instructions](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=Rmai0dD30XzL). 
You can install the [“open in colab”](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo?hl=en) GitHub extension, which allows you to open notebooks directly from the GitHub user interface.

**File Transfer**

* There are many ways to get data in and out of google colab. We strongly recommend that students use a solution that can be scripted (e.g. linking to google drive in the notebook code) instead of solutions that require manual input (e.g. uploading data from your local computer) More information can be found [here](https://colab.research.google.com/notebooks/io.ipynb).
  
**GPU Use**
 
* Colab’s free GPU is great but it takes some care to use it. There are two important caveats:
  1. Free Colab notebooks are aggressively CPU constrained. Users need to watch out for CPU bottlenecks and creatively work around them. Techniques such as using smaller batch sizes, caching pre-processed data, moving processing steps to GPU, etc. can be very helpful.

  2. Colab notebooks are also aggressively time constrained. The kernels are pruned based on activity in obscure and inconsistent ways. It's possible to manage this but very valuable to be aware of in advance.

* The best way to approach the second problem (and an important approach to cloud computing in general) is to set up your system so that it can be interrupted and pick up gracefully at any moment. For example, you might use google drive to store a log of neural network training progress as well as weights for each epoch. You can write your script/notebook so that it's able to check if training was in progress and then pick it back up in the middle. You can read the log, see if the most recent epoch < max_epochs, and if so, load the most recent weights, set the learning rate and other params accordingly, and then off to the races.
