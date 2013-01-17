JumpToDef
=========

JumpToDef is a **ghetto** Sublime Text 2 plugin which jumps to function definitions in **predictable** JavaScript.

**By ghetto** I mean that I learned everything I currently know about ST2 plugin development in about 20 minutes
([from this guide](http://net.tutsplus.com/tutorials/python-tutorials/how-to-create-a-sublime-text-2-plugin/)), and 
I wrote the initial version of the plugin in less than an hour.

**By predictable** I mean that the regex for finding identifiers isn't actually going to match every possible 
identifier you can have in JavaScript.  And I mean that the list of reserved words was just copied and pasted after 
several seconds of Googling.  And I mean that it only looks in the current file for function definitions, and it only 
identifies functions which are properties of an object (not the global object).

##How Do I Install This Piece Of Crap?

I'm really lazy, so I haven't created a zipped up version of this plugin.  And even if I had, I wouldn't have anywhere 
to host it.  Right now the only way to "install" the plugin is to drop the base directory of this repo into your 
ST2 Packages directory.  On Windows 7 this is located at:

    %appdata%\Roaming\Sublime Text 2\Packages\
    
I have no idea where it is on any other OS.

##Okay, So How Do I Use The Damn Thing?

To use JumpToDef, find a function call somewhere, either select the name or place the cursor within it, then simply 
invoke the command with the `Ctrl-Shift-J` key combo, or right-click inside the buffer window and navigate to 'Jump
to Definition' like so:

![](http://i.imgur.com/dcViP.png)
