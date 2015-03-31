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
