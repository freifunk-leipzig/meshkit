from meshkit import *


if not config == None:
    db.define_table('imageconf',
        Field('target',
            label=T('Target'),
            comment=T('For which hardware platform you want to build an image. If you are unsure which is the right one for your device visit the openwrt wiki and search for your device there.'),
            requires=IS_IN_SET(
                targets,
                error_message=T('%(name)s is invalid') % dict(name=T('Target')),
                zero=None
            ),
        ),
        Field('status',
            requires=IS_EMPTY_OR(
                IS_IN_SET([ '0', '1', '2', '3' ], error_message=T('%(name)s is invalid') % dict(name=T('Status')))
            )
        ),
        Field('noconf', 'boolean', label=T("No configuration"),
            comment=T('If you check this option meshkit will only build your images, but not configure your system. Also it is still possible to select packages and upload your own files.')
        ),
        Field('expert', 'boolean', label=T('Expert mode'),
            comment=T('Enable this to show much more options for customizing your firmware.')),
        Field('mail', label=T('Email'),
            comment=T('Enter your email address here. After the images have been built you will receive an email with download links for the firmware.'),
            requires=IS_EMPTY_OR(IS_EMAIL(error_message=T('%(name)s is invalid') % dict(name=T('Email')))),
        ),
        Field('community',
            label=T('Community'),
            comment=T('Please select your wireless community here. This will select reasonable defaults for step 2 of the image configuration.'),
            requires=IS_IN_SET(communities,
                zero=None,
                error_message=T('%(name)s is invalid') % dict(name=T('Community'))
            )
        ),
        Field('nodenumber', 
            label=T('Nodenumber'),
            comment=T('Please enter the Node Number for your weimarnetz node.'),
            requires=IS_EMPTY_OR(IS_DECIMAL_IN_RANGE(1, 1000, error_message=T('%(name)s is invalid') % dict(name=T('Node Number'))))
        ),
        Field('password_hash', type='string', default=None,
              requires=IS_EMPTY_OR(
                IS_MD5CRYPT()
              ),
              label=T('Password Hash'), widget=password_md5crypt
        ),
        Field('pubkeys',type='text', label=T('Public Keys'),
            comment=T('Add ssh public keys, one per line.'),
            requires=IS_EMPTY_OR([
                    IS_LENGTH(32768,0, error_message=T('%(name)s can only be up to %(len)s characters long') % dict(name=T('Pubkeys'), len='32768')),
                    IS_MATCH('[a-zA-Z0-9\/\+,-@\.\=]+', error_message=T('%(name)s contains invalid characters') % dict(name=T('Pubkeys')) )
                ])
        ),
        Field('profile',
            label=T('Profile'),
            comment=T('This sets a profile for your router model. If your device is not listed try something generic (default) if available.'),
            requires=IS_EMPTY_OR(IS_MATCH('[a-zA-Z0-9\-]+', error_message=T('%(name)s is invalid') % dict(name=T('Profile'))))
        ),
        Field('webif',
            label=T('Web Interface'),
            comment=T('Webinterface that is installed. This may remove or add packages depending on your selection.'),
            requires=IS_EMPTY_OR(IS_IN_SET(config.webifs, error_message=T('%(name)s is invalid') % dict(name=T('Webinterface')))),
        ),
        Field('theme',
            label = T('Theme'),
            comment = T('Chooses the theme for the web interface. Freifunk-generic is the only one that is customised for communities, so you should probably use this theme.'),
            requires=IS_EMPTY_OR(IS_IN_SET(themes, error_message=T('%(name)s is invalid') % dict(name=T('Theme'))))
        ),
        Field('ipv6', 'boolean', label=T('IPv6'),
            comment=T('Enable/Disable IPv6 globally.')
        ),
        Field('ipv6_config',
            requires=IS_EMPTY_OR(IS_IN_SET(['static', 'auto-ipv6-random', 'auto-ipv6-fromv4'], error_message=T('%(name)s is invalid') % dict(name=T('Webinterface'))))
        ),
        Field('packages', type='text', label=T('Packages'),
            requires=IS_EMPTY_OR(
                IS_MATCH(
                    '[a-zA-Z0-9\-\_\n]+',
                    error_message=T('%(name)s is invalid') % dict(name=T('Packages'))
                )
            )
        ),
        Field('rand',
            requires=IS_EMPTY_OR([
                IS_ALPHANUMERIC(),
                IS_LENGTH(32)])
        ),
        Field('hostname',
            requires=IS_EMPTY_OR(IS_MATCH('[a-zA-Z0-9][a-zA-Z0-9\.\-]+[a-zA-Z0-9]', error_message=T('%(name)s is invalid') % dict(name=T('Hostname')))),
            comment=T('Hostname. If left empty it will be autogenerated from the IPv4 address')
        ),
        Field('latitude',
            label=("Latitude"),
            comment=T('Latitude') + " " + T('in decimal notation.'),
            requires=IS_EMPTY_OR(
                IS_DECIMAL_IN_RANGE(
                    -180, 180,
                    error_message=T('%(name)s must be a decimal value between -180 and 180, e.g. 12.34567.') % dict(name=T('Latitude'))
                )
            )
        ),
        Field('longitude',
            label = T('Longitude'),
            comment=T('Longitude') + " " + T('in decimal notation.'),
            requires=IS_EMPTY_OR(
                IS_DECIMAL_IN_RANGE(
                    -180, 180,
                    error_message=T('%(name)s must be a decimal value between -180 and 180, e.g. 12.34567.') % dict(name=T('Longitude'))
                )
            )
        ),
        Field('upload', 'upload',
            requires=IS_EMPTY_OR(IS_UPLOAD_FILENAME(extension='gz', error_message=T('%(name)s is invalid') % dict(name=T('Upload'))))
        ),
        Field('wifiifsnr', 'integer'),
        Field('wifi0ipv4addr',
            requires=IS_EMPTY_OR(IS_IPV4(error_message=T('%(name)s is invalid') % dict(name='WIFI0 ' + T('IP address'))))
        ),
        Field('wifi0ipv6addr',
            requires=IS_EMPTY_OR(IS_IPV6CIDR(error_message=T('%(name)s is invalid') % dict(name='WIFI0 ' + T('IPv6 address'))))
        ),
        Field('wifi0ipv6ra', 'boolean'),
        Field('wifi0chan',
            requires=IS_EMPTY_OR(IS_INT_IN_RANGE(1, 170, error_message=T('%(name)s is invalid') % dict(name='WIFI0 ' + T('Channel'))))
        ),
        Field('wifi0dhcp','boolean'),
        Field('wifi0vap','boolean'),
        Field('wifi0dhcprange',
            requires=IS_EMPTY_OR(IS_IPV4CIDR(error_message=T('%(name)s is invalid') % dict(name='WIFI0 ' + T('DHCP Range'))))
        ),
        Field('wifi1ipv4addr',
            requires=IS_EMPTY_OR(IS_IPV4(error_message=T('%(name)s is invalid') % dict(name='WIFI1 ' + T('IP address'))))
        ),
        Field('wifi1ipv6addr',
            requires=IS_EMPTY_OR(IS_IPV6CIDR(error_message=T('%(name)s is invalid') % dict(name='WIFI1 ' + T('IPv6 address'))))
        ),
        Field('wifi1ipv6ra', 'boolean'),
        Field('wifi1chan',
            requires=IS_EMPTY_OR(IS_INT_IN_RANGE(1, 170, error_message=T('%(name)s is invalid') % dict(name='WIFI1 ' + T('Channel'))))
        ),
        Field('wifi1dhcp','boolean'),
        Field('wifi1vap','boolean'),
        Field('wifi1dhcprange',
            requires=IS_EMPTY_OR(IS_IPV4CIDR(error_message=T('%(name)s is invalid') % dict(name='WIFI1 ' + T('DHCP Range'))))
        ),
        Field('wifi2ipv4addr',
            requires=IS_EMPTY_OR(IS_IPV4(error_message=T('%(name)s is invalid') % dict(name='WIFI2 ' + T('IP address'))))
        ),
        Field('wifi2ipv6addr',
            requires=IS_EMPTY_OR(IS_IPV6CIDR(error_message=T('%(name)s is invalid') % dict(name='WIFI2 ' + T('IPv6 address'))))
        ),
        Field('wifi2ipv6ra', 'boolean'),
        Field('wifi2chan',
            requires=IS_EMPTY_OR(IS_INT_IN_RANGE(1, 170, error_message=T('%(name)s is invalid') % dict(name='WIFI2 ' + T('Channel'))))
        ),
        Field('wifi2dhcp','boolean'),
        Field('wifi2vap','boolean'),
        Field('wifi2dhcprange',
            requires=IS_EMPTY_OR(IS_IPV4CIDR(error_message=T('%(name)s is invalid') % dict(name='WIFI2 ' + T('DHCP Range'))))
        ),
        Field('nickname',
            label = T('Nickname'),
            comment = T('Enter your nickname here.'),
            requires=IS_EMPTY_OR(
                IS_LENGTH(32,0, error_message=T('%(name)s can only be up to %(len)s characters long') % dict(name=T('Nickname'), len='32'))
            )
        ),
        Field('name',
            label = T('Name'),
            comment = T('Enter your name here.'),
            requires=IS_EMPTY_OR(
                IS_LENGTH(32,0, error_message=T('%(name)s can only be up to %(len)s characters long') % dict(name=T('Name'), len='32'))
            )
        ),
        Field('email',
            label = T('Mail'),
            comment = T('Enter your email address here.'),
            requires=IS_EMPTY_OR(IS_EMAIL(error_message=T('Not a valid email address!')))
        ),
        Field('phone', label=T('Phone'),
            comment = T('Enter your phone number here.'),
            requires=IS_EMPTY_OR(
            IS_LENGTH(32,0, error_message=T('%(name)s can only be up to %(len)s characters long') % dict(name=T('Phone'), len='32'))
            )
        ),
        Field('location', label=T('Location'),
            comment=T('Location of your node.'),
            requires=IS_EMPTY_OR(
                IS_LENGTH(64,0, error_message=T('%(name)s can only be up to %(len)s characters long') % dict(name=T('Location'), len='64'))
            )
        ),
        Field('homepage',
            label = T('Homepage'),
            comment = T('If you have a homepage, then you can add it here.'),
            requires=IS_EMPTY_OR(
                IS_URL(error_message=T("%(name)s isn't a valid URL") % dict(name=T('Homepage'), len='255'))
            )
        ),
        Field('note', length=1024, type='text', label = T("Note"),
            comment = T('You may enter a custom comment here.'),
            requires=IS_EMPTY_OR(
                    IS_LENGTH(1024,0, error_message=T('%(name)s can only be up to %(len)s characters long') % dict(name=T('Note'), len='1024'))
                )
        ),
        Field('wanproto', label=T('WAN Protocol'),
            comment=T('Protocol to use for the WAN interface.'),
            requires=IS_EMPTY_OR(
                IS_IN_SET(
                    config.wanprotos,
                    error_message=T('%(name)s is invalid') % dict(name=T('Wan Protocol'))
                )
            )
        ),
        Field('wanipv4addr',label=T('IPv4 Address'), length=15,
            comment=T('IPv4 address for the wan interface'),
            requires=IS_EMPTY_OR(
                IS_IPV4(
                    error_message=T('%(name)s is invalid') % dict(name='WAN ' + T('IP address')))
                )
        ),
        Field('wannetmask', label=T('Netmask'), length=15,
            comment=T('IPv4 netmask for the wan interface'),
            requires=IS_EMPTY_OR(
                IS_IPV4(
                    error_message=T('%(name)s is invalid') % dict(name='WAN ' + T('Netmask'))
                )
            )
        ),
        Field('wangateway', label=T('Gateway'), length=15,
            comment=T('Internet gateway'),
            requires=IS_EMPTY_OR(
                IS_IPV4(
                    error_message=T('%(name)s is invalid') % dict(name='WAN ' + T('Gateway'))
                )
            )
        ),
        Field('wandns', label=T('DNS'), length=255,
            comment=T('DNS server(s). Seperate by space if you want to use multiple DNS servers.'),
            requires=IS_EMPTY_OR(
                IS_MATCH(
                    '[0-9\. ]+',
                    error_message=T('%(name)s is invalid') % dict(name=T('Profile'))
                )
            )
        ),
        Field('wan_allow_ssh', 'boolean', label=T('Allow ssh'),
            comment=T('Add firewall rule to allow ssh access from the wan interface.')
        ),
        Field('wan_allow_web', 'boolean', label=T('Allow web'),
            comment= T('Add firewall rule to allow web access from the wan interface.')
        ),
        Field('sharenet','boolean', label=T('Share internet'),
            comment=T('Allow others in the mesh to use your internet connection. This makes use of the olsrd dyngw_plain plugin, which checks for available internet connectivity and starts to announce it as hna as soon as it is detected.')
        ),
        Field('localrestrict','boolean', label=T('Protect local network'),
            default=True,
            comment=T('Protect the network behind wan from being accessed from the mesh.'),
        ),
        Field('wan_qos', 'boolean', label=T('QOS'),
            comment=T('Adds traffic shaping with a fixed down- and upload limit to the WAN-Interface.')
        ),
        Field('wan_qos_down', 'integer', label=T('Download speed'), default='1024',
            comment=T('Download speed in kbit/s. Set it about 10% lower than your actual internet download speed.')
        ),
        Field('wan_qos_up', 'integer', label=T('Upload speed'), default='128',
            comment=T('Upload speed in kbit/s. Set it about 10% lower than your actual internet upload speed.')
        ),
        Field('lanproto', label=T('LAN Protocol'),
            comment = T('Protocol to use for the LAN interface.'),
            requires=IS_EMPTY_OR(
                IS_IN_SET(
                    config.lanprotos, error_message=T('%(name)s is invalid') % dict(name='LAN ' +T('Protocol')),
                )
            )
        ),
        Field('lanipv4addr', label=T('IPv4 Address'), length=15, default="192.168.1.1",
            comment = T('IPv4 address for the LAN interface'),
            requires=IS_EMPTY_OR(IS_IPV4(error_message=T('%(name)s is invalid') % dict(name='LAN ' + T('IP address'))))
        ),
        Field('lannetmask', label=T('Netmask'), length=15, default="255.255.255.0",
            comment=T('IPv4 netmask for the LAN interface'),
            requires=IS_EMPTY_OR(IS_IPV4(error_message=T('%(name)s is invalid') % dict(name='LAN ' + T('Netmask'))))
        ),
        Field('lanipv6addr', length=255,
            label = T('IPv6 Address'),
            comment = T('IPv6 address for the LAN interface'),
            requires=IS_EMPTY_OR(IS_IPV6CIDR(error_message=T('%(name)s is invalid') % dict(name='LAN ' + T('IPv6 address'))))
        ),
        Field('lanipv6ra', 'boolean'),
        Field('landhcp','boolean', label=T('Enable DHCP'),
            comment=T('Enable DHCP-Server for the LAN interface.')
        ),
        Field('landhcprange',
            requires=IS_EMPTY_OR(IS_IPV4CIDR(error_message=T('%(name)s is invalid') % dict(name='LAN ' + T('DHCP Range'))))
        ),
        Field('url',
            requires=IS_EMPTY_OR(IS_URL(error_message=T('%(name)s is invalid') % dict(name=T('URL'))))
        ),
    )
