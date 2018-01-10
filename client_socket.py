#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('nkr-vm-machine.snt.billing.ru', 9191))
sock.send(b'hello, world!')

data = sock.recv(1024)
sock.close()

print(data)