It’s extremely user friendly (almost too much so) so in general, very easy to get started with. Off the top of my head, there’s a few things that are worth noting.

It’s very important that students link their github and colab. They should follow these instructions and make sure that they are using a browser where they are signed into github.

I recommend students all install the “open in colab” extension. This allows them to open notebooks directly from the github user interface.

There are a bunch of ways to get data in and out of google colab. I strongly recommend students use a solution that can be scripted (like linking to google drive in the notebook code) and not solutions that require manual input (like uploading data from the local computer) more info: https://colab.research.google.com/notebooks/io.ipynb
Colab’s free GPU is great but it takes some care to use it. There are two important caveats.

First is that free Colab notebooks are aggressively CPU constrained. Users need to watch out for CPU bottlenecks and creatively work around them. Things like smaller batch sizes, caching pre-processed data, moving processing steps to GPU, etc.

Second is that Colab notebooks are also aggressively time constrained. The kernels are pruned based on activity in obscure and inconsistent ways. Most of the time students just deal with this but it’s worth being aware of.

The best way to approach the second problem (and an important approach to cloud computing in general as I’m sure you know) is to set up your system so that it can be interrupted and pick up gracefully at any moment. Unfortunately, I do not have a helpful resource for how to do this at the moment, but basically the idea is something like: on your GDrive store a log of training progress as well as weights for epochs. Write your script/notebook so that it can check if training was in progress and then pick it back up in the middle. i.e. read the log, see if the most recent epoch < max_epochs, if so, load the most recent weights, set the learning rate and other params accordingly, and then off to the races
