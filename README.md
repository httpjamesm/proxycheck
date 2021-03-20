# proxycheck

This script checks whether your current IP is one of a proxy. This can be useful to check whether your VPN provider is successfully hiding your IP address.

## How It Works

When you use `python proxycheck.py`, it gets your current IP address using wtfismyip.com's JSON REST API and parses the IP address detected. It then passes this to the ProxyNet REST API to check whether your IP address is classified as a proxy or not.

## Requirements

- Python 3 or higher
- The following libraries: requests, tkinter
- An IQ of 5 or higher

## Running

Run proxycheck.py using Python 3.

## Credit

Thanks to database.red for his wonderful ProxyNet API.
