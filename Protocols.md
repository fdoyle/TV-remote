This document describes communication protocol between the client and server

connect on port: 8765

ssdp name "urn:Lacronicus:remote"

## Server Accepts:

```javascript
{
    'command':String
    'target':String?
    'new_name':String?
}
```

command can be any of

```
play
pause
status
power_on
power_off
rename
switch
```

target is TV by default, or uses `address` defined below


## Server Emits (on all HDMI-CEC updates and status update requests)

```javascript
{
    'name':String,
    'devices':[
        {
            'name':String?,
            'powered':Boolean,
            'active':Boolean, 
            'address':String,
            'physical_address':String,
            'osd_string':String,
        }
    ]
}
```