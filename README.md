tinytag
=======

tinytag is a "URL" shortener for your filesystem. It creates tiny tags like `yB` for long path names and stores accordingly named symlinks in a central folder.

A typical use case is to link a certain document in your filesystem to a handwritten note by simply writing down the short tag name.

```
usage: tinytag [-h] [-l] [-r TAG] [filename]

tinytag is a 'URL' shortener for your filesystem

positional arguments:
  filename              create a new tinytag for the given file

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list all tinytags
  -r TAG, --remove TAG  remove a certain tinytag
```

Example usage
=============

<pre>
$ tinytag "Documents/Long file name.txt" 
Created tag <b>a7</b> for file 'Documents/Long file name.txt'

$ tinytag "Documents/Projects/Even longer file name.txt" 
Created tag <b>yB</b> for file 'Documents/Projects/Even longer file name.txt'

$ ls -l ~/.tinytag
[...]  <b>a7</b> -> /home/user/Documents/Long file name.txt
[...]  <b>yB</b> -> /home/user/Documents/Projects/Even longer file name.txt

$ tinytag
List of tinytags:

<b>a7</b>:  /home/shark/Documents/Long file name.txt
<b>yB</b>:  /home/shark/Documents/Projects/Even longer file name.txt

$ tinytag -r <b>yB</b>
Removed tag <b>yB</b> for file '/home/shark/Documents/Projects/Even longer file name.txt'
</pre>
