# Create Your Own Github.io Blog


### Objectives:

 * Clone a repository on GitHub.
 * Publish blog posts using Markdown.


### Ideas:

 * GitHub hosts repositories and makes them accessible in a variety of ways, including:
     * forking (copying a GitHub hosted repo to be another GitHub hosted repo)
     * cloning (copying a GitHub hosted repo to be a repo on your computer)
     * serving the repo's contents as a web site (including pre-processing with [Jekyll](http://jekyllrb.com/))
 * Markdown is a simple text format for writing web documents.


### Process:
 * Create a repo called **your_github_username**.github.io. Clone this repo to your machine.
 * Clone [Zach Miller's repo](https://github.com/ZWMiller/zwmiller.github.io) to your local machine with `git clone`.
 * Move the files from the cloned repo into your username.github.io repo (be careful not to move the .git folder! Otherwise you'll overwrite which repo you'll be writing to. You may want to delete the .git folder in the cloned repo first)
 * Edit the files locally (both configuration and markdown files), not on github.
    - Edit _config.yml:
        * Edit username, subject, etc.
    - Edit file in _posts directory (Note: Delete the placeholder content.  Enter your own content & update date)  
 * Push from your local machine to your new repo. Wait a few minutes and go to
 your_github_username.github.io. If you've done it right, you'll have a
 webpage there.


### More resources:
 * The above process is based on this [tutorial](http://joshualande.com/jekyll-github-pages-poole)
 * Add photos, links etc to your blog [Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
 * Check out various [Jekyll Themes](http://jekyllthemes.org)
 * Configure your [Godaddy domain name with your Github Jekyll account](http://andrewsturges.com/blog/jekyll/tutorial/2014/11/06/github-and-godaddy.html)
 * Set up [Google Analytics](http://www.google.com/analytics/) for your blog
 * Barry Clark's [post](http://www.smashingmagazine.com/2014/08/01/build-blog-jekyll-github-pages/) about making a blog this way
 * The original source on [markdown](https://daringfireball.net/projects/markdown/syntax)
 * The useful [github-flavored markdown](https://help.github.com/articles/github-flavored-markdown)
 * A [live web markdown editor](https://stackedit.io/)
