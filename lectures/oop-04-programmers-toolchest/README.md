A programmer's toolchest
------------------------

Useful tools for a programmer
-----------------------------

In addition to the compiler and the editor, there are some useful tools (incomplete list)

* File comparison and patching
* Version control
* Build automation tools
* Profiling
* Debugging
* Syntax checking, source analysis (static analysis)
* Runtime analysis tools

Some of these tools may be provided by IDEs (Integrated Developer Environments)

The goal of this lecture is to be aware of these types of tools/techniques, and what their purpose is.

Integrated Developer Environments
---------------------------------

Some examples:

* Microsoft Visual Studio
* Eclipse
* PyCharm/IntelliJ

Usually provide several tools integrated in the development environment, or provides a simple plug-in system to provide necessary tools.

Important points:
The code is exactly the same, regardless of which IDE/editor is used.
Some IDEs may package certain versions of Python and/or libraries, or automate setting up virtual environments.


File comparison and patching
-----------------------------

Low-level comparison and patching

* `diff` - shows the difference between two files
* `patch` - applies a patch ("diff file") to given file(s)
  * Can be used to update files with modifications from others

Graphical tools for comparison

* tkdiff
* Meld

Some of these also provide 3-way comparisons

Version control and collaboration
---------------------------------

For single user:

* When did I introduce this bug?
* What did I change yesterday?
* Do I have the same version running on all computers?
* Update your copy or revert to older version

For multiple users:

* Merge code written by different programmers
* When did this bit (that I didn't write) change?
* Do I have the latest version of the source code?

![Version control](figs/version_control.png)

Provides source file comparison, patching, and revision control/tracking.
Repositories used to store and keep track of source code and modifications made to the source code.

Terminology (Subversion):

* Check out: Get a copy of the source from the repository - git equivalent: clone
* Update: update your copy from the repository (and merge with your changes) - git equivalent: pull
* Commit: update repository with your changes (also called check in)

Other common operations:

* Compare your copy of a file (or entire source) with one of the revisions in the repository
* Branching and merging: managing code forks and merging forks within the same repository (useful when you rewrite bits that might break other people's code)

Generations of version control
------------------------------

1. Repository kept with the source (RCS etc.)
  * An extra "version control" file for each source file to keep track of revisions ("patch/diff log")
1. Centralized repository (CVS, subversion)
  * Advantage: easier collaboration, "backup"
  * Disadvantage: May need internet access to check in and out (offline development can be annoying)
1. Distributed repository (git, mercurial)
  * Advantage: Can be used without internet access
  * Disadvantages:
    * Must remember that it is multilevel
    * May be more complex for users

Web-based version control
-------------------------

Some examples:

* github
* gitlab
* sourceforge
* systems that allow you to host your own repositories ([Trac](http://trac.edgewall.org/), [Fossil](http://www.fossil-scm.org), GitLab)

These systems use standard version control systems (like SVN and git), but provide extra functionality through the web:

* wiki
* issue tracking
* web-based revision comparison
* source browsing

Issue tracking
--------------

Issue: Bugs, things that are not done, features requested etc.
Tracking: Keep tabs on if this issue should be handled, who should do it, if it's done

Provides visibility to collaborators and users

Example: github.com/numpy/numpy

Profiling
---------

Where do you spend your time and which functions do you call often?

Often sampling-based: periodically checks where in the program your instruction pointer is and what the call stack is like.

Provides a profile of where you spent your time: see proftest.c

Debuggers
---------

Inspect running code.

Pause code at specified points in the code or in time (breakpoints).

Check (and possibly modify) vales in the running program.

Examples.
* C/C++: gdb, xxgdb, ddd, nemiver, Visual Studio, +++
* Python: pydb (can also be used from, for instance, ddd)

Static checking
---------------

Compilers:

* Syntax error: when the compiler is unable to translate what you wrote into running code
* Warnings: Things that may or may not be bugs, or that often cause bugs.
  * gcc: use -Wall to get as many warnings as possible

Other tools:

* lint/plint/splint - a C syntax checker
* pylint for Python

Runtime
-------

Memory leak detection

* Valgrind
* Pympler
* Lots of other tools

Robustness checking

* Look for hacking tools
* Tools that stress your system
* Trying random parameters/data
* [Fuzz testing](http://en.wikipedia.org/wiki/Fuzz_testing)

Tools for studying
------------------

Wiki to collaborate with other students. Earlier years: students made a wiki for a course as a method for organizing information and rehersing for the exam.

Others have used dropbox (with mind maps etc.)

Can also use other tools (github/gitlab etc.)

Conclusions
-----------

This lecture only gives a quick overview of some of the useful classes of tools. There are other tools out there as well, and more will come.

One very important thing that is not covered here: ALWAYS USE BACKUPS! (And check that you can restore)

Note that MIT has a course covering this topic which is [available online.](https://missing.csail.mit.edu)
