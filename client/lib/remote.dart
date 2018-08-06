import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Remote {
  String host;
  String port;
  bool debug;

  Remote({@required this.host, @required this.port, this.debug = false});

  void sendStandby() {
    sendTransaction("standby 0");
  }

  void sendOn() {
    sendTransaction("on 0");
  }

  void sendTransaction(String transaction) {
    debugPrint(transaction);
    String payload = '{"transaction":"$transaction"}';
    if (!debug) {
      http.post('http://$host:$port/raw',
          body: payload,
          headers: {"content-type": "application/json"}).then((raw) {
        debugPrint(raw.body);
      });
    }
  }
}
