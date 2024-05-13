#!/bin/bash

battery_percent=$(/usr/sbin/ioreg -c AppleDeviceManagementHIDEventService -r -l | awk '/Magic Mouse/{p=1} /BatteryPercent/ && p{print $3; exit}')

if [ "$battery_percent" -lt 10 ]; then
  osascript -e "display notification \"Mouse battery is ${battery_percent}%\" with title \"Low Battery Alert\" sound name \"Sosumi\"" -e "display dialog \"Mouse battery is ${battery_percent}%\" with title \"Low Battery Alert\" buttons {\"Dismiss\"} with icon stop"
fi
