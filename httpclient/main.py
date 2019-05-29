#!/usr/bin/python

import urllib
import urllib.request
import http.client
import socks

socks5_ip = "192.168.12.26"
socks5_port = 1081

# https://www.cnblogs.com/heshangaichirou/p/10620374.html
# https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse
# 设置代理
def configSocks5Proxy(conn, dst_ip, dst_port):
    # 设置 连接 dst_ip"192.168.8.230", dst_port8888 时走代理
    conn.set_tunnel(dst_ip, )
    # 获取socket
    conn.sock = socks.socksocket()
    # 设置代理信息
    conn.sock.set_proxy(socks.PROXY_TYPE_SOCKS5, socks5_ip, socks5_port)
    # 让代理socks,去连接目标
    conn.sock.connect((dst_ip, dst_port))

# 建立http 连接， 并获取 cookies
def httpget(dst_ip, dst_port, path):
    # http 与 https 不同
    #conn = http.client.HTTPSConnection(url)
    conn = http.client.HTTPConnection(dst_ip, dst_port)

    configSocks5Proxy(conn, dst_ip, dst_port)

    conn.request("GET", path)
    r1 = conn.getresponse()
    cookie = r1.getheader("Set-Cookie")
    print("get cookie: " + cookie)

    print(r1.read())

if __name__ == "__main__":
    #urlget(url)
    httpget("192.168.8.230", 8888, "/")
    print("ok")