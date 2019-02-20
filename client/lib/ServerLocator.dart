import 'package:TV/ssdp/upnp.dart';

class ServerLocator {
  Future<List<String>> get() async {
    var disc = new DeviceDiscoverer();
//    var devices = await disc.discoverDevices(type: "urn:Lacronicus:remote");
    var devices = await disc.discoverDevices(type: "upnp:lacronicus", timeout: Duration(milliseconds: 500));
    return devices.map((device) => device.location)
        .map((location)=>
          Uri.parse(location).host
    ).toList();
  }
}
