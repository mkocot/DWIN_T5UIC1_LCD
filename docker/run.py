#!/usr/bin/env python3
from os import environ as env
import logging
from dwinlcd import DWIN_LCD

# default INFO
logging.basicConfig(level=env.get("LOGLEVEL", "INFO"))
# for dwin DEBUG
logging.getLogger("dwin").setLevel(logging.DEBUG)

serial_dev = env.get("DWIN_SERIAL", "/dev/ttyS0")
encoder_pins = [int(x) for x in env.get("DWIN_ENCODER", "25,24").split(",")]
button_pin = int(env.get("DWIN_BUTTON", "23"))

moonraker_api_key = env.get("MOONRAKER_API_KEY", "")
moonraker_host = env.get("MOONRAKER_HOST", "127.0.0.1")
moonraker_port = env.get("MOONRAKER_PORT", "7125")

print("Starting DWIN_LCD")
print(f"Serial: {serial_dev}")
print(f"Pins: Encoder({encoder_pins}), Button({button_pin})")
print(f"Moonraker: {moonraker_host}:{moonraker_port}, API KEY: xxxxx")

DWINLCD = DWIN_LCD(serial_dev,
        encoder_pins,
        button_pin,
        moonraker_api_key,
        host=moonraker_host,
        port=moonraker_port,
)

