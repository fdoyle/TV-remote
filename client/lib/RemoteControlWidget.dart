import 'package:TV/Remote.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class RemoteControlWidget extends StatefulWidget {
  RemoteControlWidget({Key key, this.ip}) : super(key: key);

  final String ip;

  @override
  _RemoteControlState createState() => new _RemoteControlState();
}

class _RemoteControlState extends State<RemoteControlWidget> {
  Remote remote;

  @override
  void initState() {
    super.initState();
    remote = Remote();
    remote.connect(widget.ip);
    print("connecting to ${widget.ip}");
  }


  @override
  void deactivate() {
    super.deactivate();
    remote.disconnect();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Text(widget.ip),
        Row(
          children: <Widget>[
            IconButton(
              icon: Icon(Icons.brightness_3),
              onPressed: remote.turnOff,
            ),
            IconButton(
              icon: Icon(Icons.brightness_5),
              onPressed: remote.turnOn,
            )
          ],
        )
      ],
    );

  }
}
