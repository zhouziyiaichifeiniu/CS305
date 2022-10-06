# CS305

## 第一章

### 1.3 网络核心

#### 1.3.1 分组交换  

packet switch:分组交换机 router: 路由器

store-and-forward transmission：存储整个分组之后才能传输信息

output buffer: 输出缓存  	packet loss丢包 	queuing delay排队时延 	forwarding table转发表

#### 1.3.2 电路交换

circuit switching电路交换 ：预留了通信所需要的资源（缓存，链路传输速率）

frequency-division multiplexing（fdm） 频分复用 

time-division multiplexing（tdm） 时分复用

#### 1.3.3 网络的网络

IXP因特网交换点：同等级ISP互相交换

### 1.4 分组交换网中的时延、丢包和吞吐量

#### 1.4.1 分组交换网中的时延概述

nodal processing delay:节点处理时延  queuing delay：排队时延  transmission delay：传输时延  propagation delay：传播时延

处理时延：决定分组去向 排队时延：分组在链路上等待传输的时间 传输时延：分组长度L / 传输速率R 传播时延：分组在路由器之间链路上的传播时间

#### 1.4.2 排队时延和丢包

traffic intensity流量强度  I = L * a / R  L:分组长度 R: 传输速率 a:分组到达队列的平均速率

* I > 1 : 比特到达队列的速率超过传输速率，队列将趋向无穷大
* I <= 1 : 近似指数增长

丢包loss  存储空间不够，导致路由器丢弃分组

#### 1.4.3 端到端时延

traceroute

#### 1.4.4 计算机网络中的吞吐量

throughput吞吐量   bottleneck link瓶颈链路

### 1.5 协议层次及其服务模型

#### 1.5.1 分层的体系结构

1. 协议分层layer 

协议栈protocol stack

物理层、链路层、网络层、运输层、应用层

报文message  报文段segment  数据报datagram  帧frame  

osi模型

应用层、表示层、会话层、运输层、网络层、数据链路层、物理层

#### 1.5.2 封装

应用层报文段application-layer message -> 运输层报文段transport-layer segment -> 网络层数据报network-layer datagram -> 链路层帧link-layer frame -> 

一个分组具有两种类型的字段：首部字段和有效载荷字段payload field

### 1.6 面对攻击的网络

恶意软件malware  僵尸网络botnet  拒绝服务攻击 denial-of-service

### 1.7 计算机网络和因特网的历史

## 2.应用层

### 2.1 应用层协议原理

#### 2.1.1 网络应用程序体系结构 application architecture

client-server architecture客户-服务器体系结构     固定的ip地址

P2P architecture p2p体系结构        自扩展性self-scalability

### 2.1.2 进程通信

进程process

1. 客户和服务器进程

发起通信的进程被标识为客户，在会话开始时等待联系的进程时服务器



2. 进程与计算机网络之间的接口

socket套接字  ：选择运输层协议，设定几个运输层参数

3. 进程寻址

主机地址、目的主机指定接收进程的标识符

#### 2.1.3 可供应用程序使用的运输服务

可靠数据传输、吞吐量、定时、安全性

1.可靠数据传输reliable data transfer

防止丢包、           loss-tolerant application容忍丢失的应用

2.吞吐量

因特网电话       bandwidth-sensitive application带宽敏感的应用          elastic application弹性应用

3.定时

时延（发送方注入套接字的每个比特到达接收方的套接字的时间限制）

4.安全性

加密

#### 2.1.4 因特网提供的运输服务

1. tcp服务

* 面向连接的服务

先握手、获取tcp连接

* 可靠的数据传输服务

没有丢包

secure sockets layer ssl 安全套接字层

2. udp服务

提供最小服务、无连接

#### 2.1.5 应用层协议 application-layer protocol

交换的报文类型、各种报文类型的语法、字段的语义、确定一个进程合适以及如何发送报文、对报文进行相应的规则

#### 2.1.6 本书涉及的网络应用

web、 文件传输、电子邮件、目录服务、流式视频、p2p

### 2.2 Web 和 HTTP

#### 2.2.1 http概述

http是无状态协议stateless protocol

#### 2.2.2 非持续连接和持续连接

non-persistent connection

所需时间： 2n、n+1

往返时间round-trip-time（rtt）

#### 2.2.3 http报文格式

request line请求行：方法字段、url字段、http版本字段

header line首部行：host、connection、user-agent、



status line状态行：协议版本字段、状态码、状态信息

header line首部行：connection、date、server、……

entity body实体体：包含请求的对象本身

#### 2.2.4 用户与服务器的交互：cookie

..

#### 2.2.5 web缓存

web cache web缓存器   proxy server代理服务器

#### 2.2.6 条件get方法  conditional GET



