# 0x06. Star Wars API

# Install Node 10
<pre>
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
</pre>

# Install semi-standard
<pre>
```
$ sudo npm install semistandard --global

 ```
</pre>

# Install <span style="color: red"> request </span> module and use it
<pre> 
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
</pre>

# Tasks
<font size=3> **0. Star Wars Characters** </font>
* Write a script that prints all characters of a Star Wars movie:
  * The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
  * Display one character name per line in the same order as the “characters” list in the /films/ endpoint
  * You must use the Star wars API
  * You must use the request module
