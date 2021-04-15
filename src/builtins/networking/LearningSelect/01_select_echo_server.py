#!/usr/bin/env python
# -*- coding: utf-8 -*-

import select
import socket
import sys
import queue

# 创建 TCP/IP 套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# 绑定套接字到端口
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address),
      file=sys.stderr)
server.bind(server_address)

# 监听即将到来的连接
server.listen(5)

# 我们想读的套接字
inputs = [server]

# 我们想写的套接字
outputs = []

# 消息传出队列 格式：(socket:Queue)
message_queues = {}

while inputs:
    # 等待至少有一个套接字准备好了进行后续处理。
    print('waiting for the next event', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # inputs 处理
    for s in readable:
        if s is server:
            # 可读的套接字需要准备好接收连接。
            connection, client_address = s.accept()
            print('  connection from', client_address, file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # 把我们想发送的数据队列给它。
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # 一个有数据的可读客户端
                print('  received {!r} from {}'.format(
                    data, s.getpeername()), file=sys.stderr,
                )
                message_queues[s].put(data)
                # 添加到输出列表用来做响应
                if s not in outputs:
                    outputs.append(s)
            else:
                # 空结果表明要关闭连接
                print('  closing', client_address,
                      file=sys.stderr)
                # 停止监听该链接的输入
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # 删除这个消息队列
                del message_queues[s]

    # outputs 处理
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # 没有消息在等待，我们要关闭掉。
            print('  ', s.getpeername(), 'queue empty',
                  file=sys.stderr)
            outputs.remove(s)
        else:
            print('  sending {!r} to {}'.format(next_msg,
                                                s.getpeername()),
                  file=sys.stderr)
            s.send(next_msg)

    # 处理 「异常状况」
    for s in exceptional:
        print('exception condition on', s.getpeername(),
              file=sys.stderr)
        # 停止监听此连接的输入。
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # 移除此消息队列。
        del message_queues[s]
