#!/usr/bin/env python
# encoding: utf-8

import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True
outgoing = [
    b'It will be repeated.',
    b'This is the message.  ',
]
bytes_sent = 0
bytes_received = 0

# 连接是一个阻塞操作， 因此在返回之后调用 setblocking() 方法
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock.setblocking(False)

# 设置选择器去监听 socket 是否可写的和是否可读
mysel.register(
    sock,
    selectors.EVENT_READ | selectors.EVENT_WRITE,
)

while keep_running:
    print('waiting for I/O')
    for key, mask in mysel.select(timeout=1):
        connection = key.fileobj
        client_address = connection.getpeername()
        print('client({})'.format(client_address))

        if mask & selectors.EVENT_READ:
            print('  ready to read')
            data = connection.recv(1024)
            if data:
                # A readable client socket has data
                print('  received {!r}'.format(data))
                bytes_received += len(data)

            # 当返回结果为空或者收到了我们发送的数据就将连接关闭
            keep_running = not (data or (bytes_received and (bytes_received == bytes_sent)))

        if mask & selectors.EVENT_WRITE:
            print('  ready to write')
            if not outgoing:
                # 我们的消息为空了，这意味着我们再也不必要写数据，
                # 所以将我们的配置更改为从服务器读取
                print('  switching to read-only')
                mysel.modify(sock, selectors.EVENT_READ)
            else:
                # Send the next message.
                next_msg = outgoing.pop()
                print('  sending {!r}'.format(next_msg))
                sock.sendall(next_msg)
                bytes_sent += len(next_msg)

print('shutting down')
mysel.unregister(connection)
connection.close()
mysel.close()
