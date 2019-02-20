import 'dart:async';
import 'dart:convert';

import 'dart:io';
import 'package:web_socket_channel/io.dart';
import 'package:web_socket_channel/status.dart' as status;

class Remote {
  IOWebSocketChannel websocket;
  Stream stream;

  void connect(String ip) async {
    websocket = IOWebSocketChannel.connect("ws://${ip}:8765/");
    stream = websocket.stream.asBroadcastStream();
    stream.listen((e) {
      print(e);
    });
  }

  Stream getUpdateStream() {
    return stream.map((str)=>jsonDecode(str));
  }

  void disconnect() async {
    websocket.sink.close();
  }

  void turnOn() {
    websocket.sink.add(Command("power_on").serialize());
  }

  void turnOff() {
    websocket.sink.add(Command("power_off").serialize());
  }

  void volumeUp() {
    websocket.sink.add(Command("volume_up").serialize());
  }

  void volumeDown() {
    websocket.sink.add(Command("volume_down").serialize());
  }

  void toggleMute() {
    websocket.sink.add(Command("power_off").serialize());
  }

  void play() {
    websocket.sink.add(Command("play").serialize());
  }

  void pause() {
    websocket.sink.add(Command("pause").serialize());
  }

  void switchToDevice(String physicalAddress) {
    print("Switching target to ${physicalAddress}");
    var command = Command("switch", target: physicalAddress).serialize();
    print(command);
    websocket.sink.add(command);
  }
}

class Command {
  String command;
  String target;
  String newName;

  Command(this.command, {this.target, this.newName});

  String serialize() {
    return jsonEncode({
      "command": "${command}",
      "target": "${target}",
      "new_name": "${newName}",
    });
  }
}
