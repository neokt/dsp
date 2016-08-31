# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>> * pushd - push directory 
>>   * Takes current directory and pushes it into a list for later, then changes to another directory 
>> * popd - pop directory
>>   * Takes last directory you pushed and "pops" it off, taking you back there
>> * touch - create an empty file
>> * mv - move (or rename) a file or directory
>> * less - page through a file
>> * more - page through a file, using spacebar or w to move up and down
>> * cat - print the whole file to the screen
>> * rm - removes a file
>>   * use -r or -rf to remove a directory and all of its contents
>>   * Be careful when running recursive remove on files
>> * find - find files
>>   * find . -name "*.txt" -print
>>   * find STARTDIR -name WILDCARD -print
>> * grep - find things inside files
>>   * grep -i new *.txt - the -i ignores case
>> * man - read a manual page

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> * ls: Lists contents of the directory 
>> * ls -a: Lists contents of the directory, including hidden, i.e., entries starting with .
>> * ls -l: Lists contents of the directory with details (long listing format), size in bytes
>> * ls -lh: Lists contnents of the directory with details (long listing format), size in human readable format (e.g., kilobytes, megabytes, etc.)
>> * ls -lah: Lists contents of the directory (including hidden, i.e., entries starting with .) with details, size in human readable format (e.g., kilobytes, megabytes, etc.)
>> * ls -t: Lists contents of the directory sorted by date/time, newest first
>> * ls -Glp: Lists contents of the directory with details (long listing format), without group names, and with "/" appended to directories

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>> * -d: Displays only directories
>> * -m: Displays files as a comma separated list
>> * -R: Displays subdirectories as well
>> * -q: Displays all non printing characters as ?
>> * -1: Displays each entry on a line

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> * xargs builds and executes command lines from standard input. As an example, it can be combined with the grep command to filter files from the search ressults of the find command.
>> * For example: Finding the string 'bomb' in all txt files using find, piping, grep with xargs
>>   * find . -name '*txt' | xargs grep 'bomb'

 

