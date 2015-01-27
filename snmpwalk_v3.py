from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
    cmdgen.UsmUserData('usr-sha-aes128', 'authkey1', 'privkey1',
                       authProtocol=cmdgen.usmHMACSHAAuthProtocol,
                       privProtocol=cmdgen.usmAesCfb128Protocol),
    #cmdgen.UdpTransportTarget(('demo.snmplabs.com', 161)),
    cmdgen.UdpTransportTarget(('127.0.0.1', 161)),
    cmdgen.MibVariable('IF-MIB', '').loadMibs(),
    lexicographicMode=True, maxRows=100,
    ignoreNonIncreasingOid=True
)

if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
            )
        )
    else:
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))