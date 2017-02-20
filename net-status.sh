#!/bin/bash

success() {
    echo -e "$(tput setaf 2)$@$(tput sgr0)"
}

warn() {
    echo -e "$(tput setaf 3)$@$(tput sgr0)"
}

error() {
    echo -e "$(tput setaf 1)$@$(tput sgr0)"
    exit 1
}

STATUS=$(ip route show match 0/0)

if [ ! -z "$STATUS" ]; then

    read GATEWAYIP IFACE LOCALIP <<< $(echo $STATUS | awk '{print $3" "$5" "$7}')
    GATEWAYMAC=$(ip neigh | grep "$GATEWAYIP " | awk '{print $5}')

    echo "INTERFACE:   $IFACE"
    echo "GATEWAY IP:  $GATEWAYIP"
    echo "GATEWAY MAC: $GATEWAYMAC"
    echo "LOCAL IP:    $LOCALIP"

    if [ -z $(curl -fsS http://google.com > /dev/null) ]; then
        PUBLICIP=$(dig +short myip.opendns.com @resolver1.opendns.com)

        echo "PUBLIC IP:   $PUBLICIP"

        success "\nOnline"
    else
        echo
        warn "\nLocal Only"
        exit 1
    fi
else
    error "\nInterface Offline"
fi
