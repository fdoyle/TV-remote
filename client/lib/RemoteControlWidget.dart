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
    return Container(
      decoration: BoxDecoration(color: Colors.white, boxShadow: [BoxShadow(blurRadius: 8)]),
      child: StreamBuilder(
          stream: remote.getUpdateStream(),
          initialData: {"name": "unknown", "devices": []},
          builder: (context, snapshot) {
            var status = snapshot.data;
            return Padding(
              padding: const EdgeInsets.all(8.0),
              child: Column(
                children: <Widget>[
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(widget.ip),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(status["name"]),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Row(
                      children: <Widget>[
                        IconButton(
                          icon: Icon(Icons.brightness_3),
                          onPressed: remote.turnOff,
                        ),
                        IconButton(
                          icon: Icon(Icons.brightness_5),
                          onPressed: remote.turnOn,
                        ),
                        IconButton(
                          icon: Icon(Icons.volume_up),
                          onPressed: remote.volumeUp,
                        ),
                        IconButton(
                          icon: Icon(Icons.volume_down),
                          onPressed: remote.volumeDown,
                        ),
                        IconButton(
                          icon: Icon(Icons.play_arrow),
                          onPressed: remote.play,
                        ),
                        IconButton(
                          icon: Icon(Icons.pause),
                          onPressed: remote.pause,
                        )
                      ],
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: DeviceList(status["devices"], remote),
                  )
                ],
              ),
            );
          }),
    );
  }
}


class DeviceList extends StatelessWidget{
  List<dynamic> deviceList;
  Remote remote;//todo this should use inheretedWidget instead


  DeviceList(this.deviceList, this.remote);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: deviceList.map((device)=>DeviceWidget(device, remote)).toList(),
    );
  }
}

class DeviceWidget extends StatelessWidget{
  dynamic device;
  Remote remote;

  DeviceWidget(this.device, this.remote);

  @override
  Widget build(BuildContext context) {
    String osd_string = device["osd_string"];
    bool isActive = device["active"];
    String physicalAddress = device["physical_address"];
    return GestureDetector(
      onTap: () => remote.switchToDevice(physicalAddress),
      child: Container(
        decoration: BoxDecoration(color: Colors.white, boxShadow: [BoxShadow(blurRadius: 8)]),
        child: Column(
          children: <Widget>[
            Text(osd_string),
            Text(isActive? "Active": "Not Active")
          ],
        ),
      ),
    );
  }



}