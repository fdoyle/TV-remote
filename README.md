# TV-remote
Chromecast can turn my TV on, but won't turn it off, and that's lame.

This project consists of a "Server" written in node that lives on a number of raspberry pi's connected to TVs via HDMI-CEC, and a "Client" written in flutter that lives on phones that can send commands to each server over http. 

Because flutter is cross-platform, I have been able to use the app on both ios and android devices. Now that flutter is 1.0, I feel confident that flutter is a viable cross-platform solution for mobile applications. 

License:

This works, but I don't recommend looking at exactly how, it's likely not best-practice. I'm hoping to return to this project in the not too distant future to improve server discovery. 
