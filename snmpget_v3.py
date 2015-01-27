from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.UsmUserData('usr-none-none'),
    cmdgen.UdpTransportTarget(('demo.snmplabs.com', 161)),
    #cmdgen.MibVariable('IP-MIB', 'ipAdEntAddr', '127.0.0.1'),
    cmdgen.MibVariable('IP-MIB', 'ipAdEntAddr', '192.168.1.9'),
    lookupNames=True, lookupValues=True
)

# Check for errors and print out results
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex)-1] or '?'
            )
        )
    else:
        for name, val in varBinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))