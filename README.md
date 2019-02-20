# TV-remote
Chromecast can turn my TV on, but won't turn it off, and that's lame.

(development is currently on the v2 branch)

Architecture:
A server written in python that lives on a raspberry pi connected to both wifi and a TV over hdmi

A client written in flutter. 

Client uses SSDP to discover servers on the network, then opens a websocket to each. 

Current functionality:
power on/off TV
switch between sources

short-term to-do:
improve stability (some websocket errors bring the whole thing down)
volume
play/pause

long-term to-do
improve discovery speed (Takes 3-4 seconds from start to server discovery, maybe it's waiting for a timeout somewhere)
make it pretty?


![img](https://imgur.com/f43ipyw)
