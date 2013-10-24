Pyglet template
===============

This is a template to bootstrap a project using Pyglet 1.2 and Python 2.x.

It is pretty small so just read the code and the comments. It includes
a simple example drawing a label.

The most relevant bits are:

 - You can load resources from your `data/` directory in the same level as your *game.py* script.
 - There's a key state handler in *keys* after the **Main** object is created.
 - Sets the viewport preserving the aspect ratio based on WIDTH and HEIGHT constants.
 - It has a key press handler supporting pause ('p'), screenshot (CTRL + 's') and fullscreen toggle (CTRL + 'f').
 - setup.py is functional, but you may want to edit it to add your name/email.

This code is in the public domain, use it for anything you want.

Juan J. Martinez <jjm@usebox.net>


Getting Pyglet current and simplifying distribution
---------------------------------------------------

You can get Pyglet current (1.2) in two different ways:

1. Using Mecurial:

You need to install Mercurial first, then go to a temporary directory and run:

    hg clone https://pyglet.googlecode.com/hg/ pyglet-current

2. Downloading a ZIP from Google Code:

    wget http://pyglet.googlecode.com/archive/tip.zip

Then you can build the code:

1. `cd pyglet-*` (will be `current` or the hash of the latest change if you used `tip.zip`)
2. `python setup.py build`
3. copy resulting `pyglet/` directory from `_build/lib/` to your game directory.

In that way you can distribute Pyglet current with your game.

