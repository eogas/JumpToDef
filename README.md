JumpToDef
=========

JumpToDef is a ghetto Sublime Text 2 plugin which jumps to function definitions in predictable JavaScript.

**By ghetto** I mean that I learned everything I currently know about ST2 plugin development in about 20 minutes
([from this guide](http://net.tutsplus.com/tutorials/python-tutorials/how-to-create-a-sublime-text-2-plugin/)), and 
I wrote the initial version of the plugin in less than an hour.

**By predictable** I mean that the regex for finding identifiers isn't actually going to match every possible 
identifier you can have in JavaScript.  And I mean that the list of reserved words was just copied and pasted after 
several seconds of Googling.  And I mean that it only looks in the current file for function definitions, and it only 
identifies functions which are properties of an object (not the global object).

##So How Do I Use The Damn Thing?

TODO
