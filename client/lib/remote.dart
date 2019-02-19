import 'dart:convert';

import 'dart:io';

class Remote{
  WebSocket websocket;

  void connect(String ip) async {
    websocket = await WebSocket.connect("ws://${ip}:8765");
  }

  void disconnect() async {
    websocket.close();
  }
  
  void turnOn() async {
    websocket.add(Command("power_on").serialize());
  }

  void turnOff() async {
    websocket.add(Command("power_off").serialize());
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

