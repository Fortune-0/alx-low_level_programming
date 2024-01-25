
# MAKE FILES

A makefile is a file containing a set of directives used by a make build automation tool to generate a target/goal


## 🚀 About Me
I'm a full stack developer...

Name:
Fortune peter

Email address: Fortunepeterspc07@gmail.com


# ABOUT 
What is a Makefile? Make is Unix utility that is designed to start execution of a makefile. A makefile is a special file, containing shell commands, that you create and name makefile (or Makefile depending upon the system). While in the directory containing this makefile, you will type make and the commands in the makefile will be executed. If you create more than one makefile, be certain you are in the correct directory before typing make. Make keeps track of the last time files (normally object files) were updated and only updates those files which are required (ones containing changes) to keep the sourcefile up-to-date. If you have a large program with many source and/or header files, when you change a file on which others depend, you must recompile all the dependent files. Without a makefile, this is an extremely time-consuming task.

As a makefile is a list of shell commands, it must be written for the shell which will process the makefile. A makefile that works well in one shell may not execute properly in another shell.

The makefile contains a list of rules. These rules tell the system what commands you want to be executed. Most times, these rules are commands to compile(or recompile) a series of files. The rules, which must begin in column 1, are in two parts. The first line is called a dependency line and the subsequent line(s) are called actions or commands. The action line(s) must be indented with a tab.

# Makefiles may contain five types of constructs
An explicit rule says when and how to remake one or more files, called the rule's targets. It lists the other files that the targets depend on, called the prerequisites of the target, and may also give a recipe to use to create or update the targets.
An implicit rule says when and how to remake a class of files based on their names. It describes how a target may depend on a file with a name similar to the target and gives a recipe to create or update such a target.
A variable definition is a line that specifies a text string value for a variable that can be substituted into the text later.
A directive is an instruction for make to do something special while reading the makefile such as reading another makefile.
Lines starting with # are used for comments.
