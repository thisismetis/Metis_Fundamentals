# Cloud Computing

Cloud Computing is a catch-all term for the use of remote computing resources such as processors and storage solutions. Many companies heavily utilize these resources in order to reduce the costs of maintaining their own computing and database servers, and even an individual can benefit from flexible, easy, and temporary access to powerful machines.    

Metis students may want to leverage cloud computing when working on certain projects involving large-scale data or complex models. An example of the former might be 10s of millions of transaction records that don't fit into local RAM, while an example of the latter might be a deep neural network (GPU access dramatically speed ups neural network training). 

There are several different major cloud service providers with similar offerings, but we prefer [**Google Cloud**](./gcp-setup/readme.md) over [**Amazon Web Services (AWS)**](./aws-setup/readme.md), and also recommend looking into the [**Google Colab**](./google-colab-instructions/readme.md) platform for a more limited but completely free form of cloud computing (click links for instructions).   

Below is a brief list of pros and cons for each option:

**Google Cloud**

Pros:

 - $300 dollars of free credits for new users
 - More accessible / user-friendly interface than AWS
   
Cons:

  - Not yet as much of an industry standard as AWS
  - Not permanently free like Colab

**AWS**

Pros:
  - Industry standard with huge market share, making AWS experience likely to be particularly in demand
   
Cons:
  - Expensive, no free credits
  - Less accessible / user-friendly interface than GCP; those with strong DevOps skills will feel more comfortable

**Google Colab**

Pros:

  - Permanently free, including GPU access
  - Very user friendly

Cons:

  - Computing and storage resources available are much more limited than GCP proper or AWS. 
  - Fairly aggressively CPU and time constrained



