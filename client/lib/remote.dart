import 'dart:async';
import 'dart:convert';

import 'dart:io';
import 'package:web_socket_channel/io.dart';
import 'package:web_socket_channel/status.dart' as status;


class Remote{
  IOWebSocketChannel websocket;

  void connect(String ip) async {
    websocket = IOWebSocketChannel.connect("ws://${ip}:8765");
  }

  Stream getUpdateStream(){
    return websocket.stream;
  }

  void disconnect() async {
    websocket.sink.close();
  }
  
  void turnOn() async {
    websocket.sink.add(Command("power_on").serialize());
  }

  void turnOff() async {
    websocket.sink.add(Command("power_off").serialize());
  }

  void volumeUp() async {
    websocket.sink.add(Command("volume_up").serialize());
  }

  void volumeDown() async {
    websocket.sink.add(Command("volume_down").serialize());
  }

  void toggleMute() async {
    websocket.sink.add(Command("power_off").serialize());
  }

  void play() async {
    websocket.sink.add(Command("play").serialize());
  }

  void pause() async {
    websocket.sink.add(Command("pause").serialize());
  }
  
  void switchToDevice(String physicalAddress){
    websocket.sink.add(Command("switch", target: physicalAddress));
  }
}

class Command{
  String command;
  String target;
  String newName;


  Command(this.command, {this.target, this.newName});

  String serialize() {
    return jsonEncode({
      "command":"${command}",
      "target":"${target}",
      "new_name":"${newName}",
    });
  }
}

