# pong-python
Pong game written in python with pygame module. You can play against an AI opponent which is not very smart.

![screen_pong](https://cloud.githubusercontent.com/assets/24194821/25294427/c8b3a3fe-26a4-11e7-9e7d-d494bd961b4a.png)

# usage
```~/Pong_pygame_python$ python run.py```

# dependency
* python 3 (pygame does not behave well with python 2)
* pygame 1.9.3

# installing dependencies
## python 3 (for windows)
[Go to download page for python](https://www.python.org/ftp/python/3.5.3/python-3.5.3.exe)
## pygame 1.9.3
To install **pygame** run this in terminal/command prompt
```$ pip install pygame```

# NOTES
* Use **UP** and **DOWN** keys to move right paddle up or down.
* The ai controls the left paddle by default. 
* Set default argument of ```ai_paddle``` to ```None``` in ```left_paddle``` function to make a **user** control the left paddle.
* The keyboards **W** and **S** can be used to control the left paddle. 
* Set default argument of ```ai_paddle``` to ```1``` in ```right_paddle``` function to make a **ai** control the right paddle.
