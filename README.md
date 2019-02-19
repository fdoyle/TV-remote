
# Objective: 

Allow a mobile app to control tv's

## Requirements:
mobile app
raspberry pi servers connected on wifi and to TV via hdmi

## client:
flutter (cross platform)
maybe web at some point? Don't really want to host, maybe a chrome extension would be better?

## server:
python (has better maintained hdmi-cec library vs node)

## Connection Flow
client uses service discovery on local network to discover all available pi's. 

client then connects to those devices over web socket

server pushes all updates to clients over web socket

client can push commands over web socket


## Client functionality (user stories)
(user should be able to)
* request TV power status
* toggle TV power
* play/pause current stream
* change volume
* request list of all connected devices
* see currently selected input
* switch between inputs
* name TV's 
* name devices connected to  TV (both of these should be stored locally by server)

## Design
Initial screen shows list of connected TV's with a quick option to toggle power and select volume

Clicking into TV shows the TV detail page

* TV detail page: 
  * has tabs for list of TV's (so you don't have to back out to TV list to switch TV's
  * allows user to toggle TV power and select volume
  * shows list of connected devices.
* Connected device items:
  * click to switch to device
  * allows user to rename devices


Sad news: Ideally, this project would use Pipenv instead of the sad shell script to install dependencies. Unfortunately, pipEnv doesn't seem to like the hdmi-cec library im using, while pip works fine, so I'm stuck with that. 