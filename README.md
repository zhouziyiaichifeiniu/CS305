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

### 2.3 因特网中的电子邮件

用户代理user agent 邮件服务器mail server 简单邮件传输协议simple mail transfer protocol

#### 2.3.1 SMTP

smtp握手的阶段，SMTP客户指示发送方的邮件地址和接收方的邮件地址。之后，客户发送报文（TCP）

SMTP使用的是持久连接

#### 2.3.2 与HTTP的对比

1.

HTTP：拉协议扑pull protorol 用户使用http从服务器拉取这些信息

smtp：推协议push protocol 发送邮件服务器把文件推向接收邮件服务器

2.

smtp要求每个报文采用7比特ascii码

3.   如何处理一个既包含文本又包含图形的文档？ http把每个对象封装到她自己的http响应报文，smtp把所有报文对象放在一个报文之中

#### 2.3.3 邮件报文格式

#### 2.3.4 邮件访问协议mail access protocol

取报文是一个拉操作，需要post office protocol-version3 pop3 或者internet mail access protocol imap或者http

1.POP3

建立tcp连接 -> 特许authorization -> 事务处理 -> 更新

特许：用户发送用户名和口令

事务处理：用户代理取回报文，同时用户代理可以对报文进行删除等操作

更新：客户发出quit命令，服务器删除被标记为删除的报文

2.IMAP

在服务器创建文件夹

3.基于web的电子邮件

用户代理=普通浏览器		用户和远程邮箱之间的通信基于http

### 2.4 DNS:因特网的目录服务

主机名hostname www.facebook.com  ip地址127.0.0.1

#### 2.4.1 DNS提供的服务

域名系统domain name system ： 主机名到ip地址转换的目录服务

dns：一个由分层的dns服务器实现的分布式数据库；一个使得主机能够查询分布式数据库的应用层协议

主机别名host aliasing、规范主机名canonical hostname、邮件服务器别名mail server aliasing、负载分配load distribution

#### 2.4.2 DNS工作机理概述

集中式设计的问题：单点故障a single point of failure、通信容量traffic volume、远距离的集中式数据库distant centralized database、维护maintenance



1.分布式、层次数据库

根dns服务器、顶级域（top-level domain） dns服务器、权威dns服务器、本地dns服务器

递归查询、迭代查询

2.dns缓存

#### 2.4.3 DNS记录和报文

所有dns服务器都存储了资源记录resource record（rr）

rr提供了主机名到ip地址的映射。

rr：（Name，Value，Type，TTL）

type = A： name是主机名，value是对应的ip地址

type = NS： name是个域（foo.com），value是获得该域中主机ip地址的权威nds服务器的主机名

type = CNAME： name是主机名 value是其规范主机名

type = MX： name是邮件服务器的别名 value是其规范主机名

1. DNS报文

![img](http://c.biancheng.net/uploads/allimg/191111/6-1911111G20QV.gif)

2.在DNS数据库中插入记录

### 2.5 P2P文件分发

1.p2p体系结构的扩展性

分发时间distribution time

p2p的时间有一个upper bound，c-s的时间线性增长

2.BitTorrent

洪流torrent 文件块chunk 追踪器tracker 最稀缺优先rarest first 疏通unchoked

接收：针对自己没有的块，在邻居中决定最稀缺的块（数量最少）

响应： 对换算法。根据当前能够以最高速率向他提供数据的邻居，给出优先权。

### 2.6 视频流和内容分发网

#### 2.6.1 因特网视频

#### 2.6.2 HTTP流和DASH

动态适应性流。对于不同的质量水平，客户动态的请求不同版本的视频段数据块。

每个视频版本存储在HTTP服务器中，每个版本都有一个不同的URL。 告示文件manifest file

#### 2.6.3 内容分发网

CDN管理分布在多个地理位置上的服务器，在他的服务器中存储视频的副本，并且所有试图将每个用户请求定向到一个将提供最好的用户体验的CDN位置。

服务器安置原则：

* 深入：通过在遍及全球的接入ISP中部署服务器集群来深入到ISP的接入网中。目的是靠近端用户，减少端用户和CDN集群之间链路和路由器的数量
* 邀请做客：通过少量关键位置建造大集群来邀请到ISP做客。

集群选择策略cluster selection strategy

地理上最为邻近的集群geographically closest

cdn能够对其集群和用户之间的时延和丢包性能执行周期性的实时测量real-time measurement

## 第三章 运输层

### 3.1 概述和运输层服务

逻辑通信logic communication

#### 3.1.1 运输层和网络层的关系

运输层为运行在不同主机上的进程之间提供了逻辑通信

运输层协议将来自应用进程的报文移动到网络层

#### 3.1.2 因特网运输层概述

udp 用户数据报协议 tcp传输控制协议

责任：将两个端系统间IP的交付服务扩展为运行在端系统上的两个进程之间的交付服务

将主机间交付扩展到进程间交付被成为运输层的多路复用transport-layer multiplexing 与多路分解demultiplexing

### 3.2 多路复用与多路分解

多路分解：将运输层报文段中的数据交付到正确的套接字的工作

多路复用：在源主机从不同套接字收集数据块，并为每个数据块封装上首部信息从而生成报文段，然后将报文段传递到网络层

运输层多路复用要求：

1. 套接字有唯一标识符
2. 每个报文段有特殊字段来指示改报文段所要交付到的套接字

源端口号字段source port number field 目的端口号字段destination port number field

1. 无连接的多路复用与多路分解
2. 面向连接的多路复用与多路分解

tcp套接字是一个四元组（源ip地址，源端口号，目的ip地址，目的端口号）

3. web服务器与tcp

### 3.3 无连接运输： UDP

#### 3.3.1 UDP报文段结构

![img](https://img-blog.csdnimg.cn/20210629221936791.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2d0ajA2MTc=,size_16,color_FFFFFF,t_70)

UDP首部有四个字段，每个字段由两个字节组成

#### 3.3.2 UDP检验和

检验和用于确定当UDP报文段从源到达目的地移动时，其中的比特是否发生了改变

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

### 2.3 因特网中的电子邮件

用户代理user agent 邮件服务器mail server 简单邮件传输协议simple mail transfer protocol

#### 2.3.1 SMTP

smtp握手的阶段，SMTP客户指示发送方的邮件地址和接收方的邮件地址。之后，客户发送报文（TCP）

SMTP使用的是持久连接

#### 2.3.2 与HTTP的对比

1.

HTTP：拉协议扑pull protorol 用户使用http从服务器拉取这些信息

smtp：推协议push protocol 发送邮件服务器把文件推向接收邮件服务器

2.

smtp要求每个报文采用7比特ascii码

3.   如何处理一个既包含文本又包含图形的文档？ http把每个对象封装到她自己的http响应报文，smtp把所有报文对象放在一个报文之中

#### 2.3.3 邮件报文格式

#### 2.3.4 邮件访问协议mail access protocol

取报文是一个拉操作，需要post office protocol-version3 pop3 或者internet mail access protocol imap或者http

1.POP3

建立tcp连接 -> 特许authorization -> 事务处理 -> 更新

特许：用户发送用户名和口令

事务处理：用户代理取回报文，同时用户代理可以对报文进行删除等操作

更新：客户发出quit命令，服务器删除被标记为删除的报文

2.IMAP

在服务器创建文件夹

3.基于web的电子邮件

用户代理=普通浏览器		用户和远程邮箱之间的通信基于http

### 2.4 DNS:因特网的目录服务

主机名hostname www.facebook.com  ip地址127.0.0.1

#### 2.4.1 DNS提供的服务

域名系统domain name system ： 主机名到ip地址转换的目录服务

dns：一个由分层的dns服务器实现的分布式数据库；一个使得主机能够查询分布式数据库的应用层协议

主机别名host aliasing、规范主机名canonical hostname、邮件服务器别名mail server aliasing、负载分配load distribution

#### 2.4.2 DNS工作机理概述

集中式设计的问题：单点故障a single point of failure、通信容量traffic volume、远距离的集中式数据库distant centralized database、维护maintenance



1.分布式、层次数据库

根dns服务器、顶级域（top-level domain） dns服务器、权威dns服务器、本地dns服务器

递归查询、迭代查询

2.dns缓存

#### 2.4.3 DNS记录和报文

所有dns服务器都存储了资源记录resource record（rr）

rr提供了主机名到ip地址的映射。

rr：（Name，Value，Type，TTL）

type = A： name是主机名，value是对应的ip地址

type = NS： name是个域（foo.com），value是获得该域中主机ip地址的权威nds服务器的主机名

type = CNAME： name是主机名 value是其规范主机名

type = MX： name是邮件服务器的别名 value是其规范主机名

1. DNS报文

![img](http://c.biancheng.net/uploads/allimg/191111/6-1911111G20QV.gif)

2.在DNS数据库中插入记录

### 2.5 P2P文件分发

1.p2p体系结构的扩展性

分发时间distribution time

p2p的时间有一个upper bound，c-s的时间线性增长

2.BitTorrent

洪流torrent 文件块chunk 追踪器tracker 最稀缺优先rarest first 疏通unchoked

接收：针对自己没有的块，在邻居中决定最稀缺的块（数量最少）

响应： 对换算法。根据当前能够以最高速率向他提供数据的邻居，给出优先权。

### 2.6 视频流和内容分发网

#### 2.6.1 因特网视频

#### 2.6.2 HTTP流和DASH

动态适应性流。对于不同的质量水平，客户动态的请求不同版本的视频段数据块。

每个视频版本存储在HTTP服务器中，每个版本都有一个不同的URL。 告示文件manifest file

#### 2.6.3 内容分发网

CDN管理分布在多个地理位置上的服务器，在他的服务器中存储视频的副本，并且所有试图将每个用户请求定向到一个将提供最好的用户体验的CDN位置。

服务器安置原则：

* 深入：通过在遍及全球的接入ISP中部署服务器集群来深入到ISP的接入网中。目的是靠近端用户，减少端用户和CDN集群之间链路和路由器的数量
* 邀请做客：通过少量关键位置建造大集群来邀请到ISP做客。

集群选择策略cluster selection strategy

地理上最为邻近的集群geographically closest

cdn能够对其集群和用户之间的时延和丢包性能执行周期性的实时测量real-time measurement

## 第三章 运输层

### 3.1 概述和运输层服务

逻辑通信logic communication

#### 3.1.1 运输层和网络层的关系

运输层为运行在不同主机上的进程之间提供了逻辑通信

运输层协议将来自应用进程的报文移动到网络层

#### 3.1.2 因特网运输层概述

udp 用户数据报协议 tcp传输控制协议

责任：将两个端系统间IP的交付服务扩展为运行在端系统上的两个进程之间的交付服务

将主机间交付扩展到进程间交付被成为运输层的多路复用transport-layer multiplexing 与多路分解demultiplexing

### 3.2 多路复用与多路分解

多路分解：将运输层报文段中的数据交付到正确的套接字的工作

多路复用：在源主机从不同套接字收集数据块，并为每个数据块封装上首部信息从而生成报文段，然后将报文段传递到网络层

运输层多路复用要求：

1. 套接字有唯一标识符
2. 每个报文段有特殊字段来指示改报文段所要交付到的套接字

源端口号字段source port number field 目的端口号字段destination port number field

1. 无连接的多路复用与多路分解
2. 面向连接的多路复用与多路分解

tcp套接字是一个四元组（源ip地址，源端口号，目的ip地址，目的端口号）

3. web服务器与tcp

### 3.3 无连接运输： UDP

#### 3.3.1 UDP报文段结构

![img](https://img-blog.csdnimg.cn/20210629221936791.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2d0ajA2MTc=,size_16,color_FFFFFF,t_70)

UDP首部有四个字段，每个字段由两个字节组成

#### 3.3.2 UDP检验和

checksum的计算：所有比特相加，溢出位与最低比特位相加，再取反获得checksum

检验和用于确定当UDP报文段从源到达目的地移动时，其中的比特是否发生了改变

### 3.4 可靠数据传输原理

可靠数据传输协议reliable data transfer protocol

单向数据传输unidirectional data transfer

#### 3.4.1 构造可靠数据传输协议

1. 经完全可靠信道的可靠数据传输：rdt1.0

rdt的发送端接收高层数据，产生分组，并将分组发送到信道中

rdt的接收端从底层接收分组，从分组中取出数据，将数据上传给较高层

2. 经具有比特差错bit errors信道的可靠数据传输：rdt2.0

自动重传请求automatic repeat request

差错检测checksum：使接收方检测到何时出现了比特差错

接收方反馈：ACK和NAK

重传：接收方收到差错分组时返回NAK，发送方将重传该分组文

rdt2.1、rdt2.2

为了解决ack和nak受损到问题，在数据分组中添加新字段，让发送方对其数据分组编号。

rdt2.2实现了无nak的可靠数据传输协议

3. 经具有比特差错的丢包信道的可靠数据传输：rdt3.0

两个问题：怎样检测丢包？丢包后该做什么？

冗余数据分组duplicate data transfer  倒计时计数器countdown timer 比特交替协议alternating-bit protocol

#### 3.4.2 流水线可靠数据传输协议

利用率utilization 流水线pipelining

流水线的要求：

* 必须增加序号范围。
* 协议的发送方和接收方两端需要缓存多个分组
* 所需序号范围和对缓冲的要求取决于数据传输协议如何处理丢失、损坏及延时过大的分组

#### 3.4.3 回退N步 Go-Back-N

基序号base 下一个序号nextseqnum 窗口长度window size 滑动窗口协议sliding-window protocol 基于事件的编程event-based programming

GBN发送方必须响应三种类型的事件：

* 上层的调用：检测窗口是否已满
* 收到一个ack：对序号为n对分组的确认采取累计确认cumulative acknowledgement。表明接收方已正确接收序号为n及以前的所有分组。
* 超时事件：定时器将用于恢复数据或确认分组的丢失。只使用一个定时器，一旦超时，将发送所有已发送但还未确认多分组。



GBN接收方：

如果一个序号为n的分组被正确接收到，并且按序，接收方分组发送一个序号为n的ACK。在其他情况下，接收方丢弃分组。

#### 3.4.4 选择重传

gbn的问题：单个比特的差错就能够引起重传大量分组，许多分组根本没有必要重传

selective repeat：发送方仅重传哪些在接收方出错的分组

发送方：

* 从上层收到数据：根据窗口大小决定要不要发送数据
* 超时：每个分组都有一个定时器
* 收到ack：如果ack的分组在窗口内，标记为ack，如果为base，则窗口移动到第一个没有ack标记的分组



接收方：

* 序号在[base,base+n-1]的分组被接受并返回ack。如果不为base，则缓存，如果为base，将所有连续的缓存向上交付分组
* 序号在[base-n,base-1]范围内，产生一个ack
* 其他情况则忽略





1. 检验和：用于检测在一个传输分组中的比特错误
2. 定时器： 用于超时/重传一个分组。接收方可能会收到一个分组的多个冗余副本
3. 序号： 对发送方的数据分组按顺序编号。可用于检测冗余分组
4. 确认：接收方回复分组被正确的接受到了
5. 否定确认：接收方告诉发送方分组未被正确接收
6. 窗口、流水线： 发送方被限制只发送那些序号落在指定范围内的分组。

### 3.5 面向连接的运输：TCP

#### 3.5.1 TCP连接

面向连接的connection-oriented 点到点point-to-point 三次握手three-way handshake 最大报文段长度maximum segment size

#### 3.5.2 TCP报文段结构

![在这里插入图片描述](https://img-blog.csdnimg.cn/bdad0ba97b114354bcc553832011f43c.png)

序号字段sequence number field、确认号字段acknowledgement number field

接收窗口字段receive window field：用于流量控制

标志字段：ack、syn、fin：连接建立和拆除  

1. 序号和确认号

序号是报文段首字节在字节流中的编号

主机a填充进报文段的确认号是主机a期望从主机b收到的下一子节的序号

2. 序号和确认号的案例

c -> s : seq = 42 ack = 79 data = 'c'

s -> c : seq = 79 ack = 43 data = 'c'

c -> s : seq = 43 ack = 80

#### 3.5.3 往返事件的估计与超时

1. 估计往返时间

t = 0.125* 过去计算的时间 + 0.875 * 刚刚计算的时间

rtt的偏差：devrtt 是预测值和过去值的差值

2. 设置和管理重传超时间隔

Timeout = estimatertt + 4 * devrtt

#### 3.5.4 可靠数据传输

tcp每次重传都会将下一次的超时间隔设为先前值的两倍：这种修改提供了一个形式受限的拥塞控制

发送方如果收到三个冗余ack，就执行快速重传fast retransmit

#### 3.5.5 流量控制

tcp通过让发送方维护一个成为接受窗口receive window的变量来提供流量控制

RcvBuffer >= LastByteRcvd - LastByteRead

rwnd = RcvBuffer - [LastByteRcvd - LastByteRead]

tcp规范中要求：当主机B的接收窗口为0时，主机A继续发送只有一个字节数据的报文段。

#### 3.5.6 TCP连接管理

连接：

1. 报文段首部的SYN被置为1，同时会随机选择一个初始序号**client_isn**并放置到序号字段
2. 服务器提取syn报文段，向用户发送允许连接的报文段。 syn被置为1，确认号字段被置为 **client_isn + 1 **。最后，选择自己的初始序号**server_isn**，放置到序号字段
3. 客户端将确认字段置为**server_isn+1** ，syn被置为0

关闭：

1. 客户端在其报文段的FIN置为1，服务器接收到该报文后，会发送一个确认报文段
2. 服务器在其报文段的FIN置为1，客户也会发送一个确认报文段



tcp state



### 3.6 拥塞控制原理

#### 3.6.1 拥塞原因与代价

每连接的吞吐量per-connection throughput 供给负荷offered load

当分组的到达速率接近链路容量时，分组经历巨大的排队时延

发送方必须执行重传以补偿因为缓存溢出而丢弃的分组

发送方在遇到大时延所进行的不必要重传会引起路由器利用其链路带宽来转发不必要的分组副本

一个分组沿一条路径被丢弃时，每个上游路由器用于转发该分组到丢弃该分组使用的传输容量最终被浪费掉了

#### 3.6.2 拥塞控制方法

* 端到端拥塞控制

tcp采用端到端的控制

tcp报文段的丢失被认为是网络拥塞的一个迹象，tcp会相应的减小其窗口长度

* 网络辅助的拥塞控制：路由器向发送方提供关于网络中拥塞状态的显式反馈信息

在available bite rate中，路由器通知发送方他能在输出链路上支持的最大主机发送速率



### 3.7 TCP拥塞控制

tcp使用端到端的拥塞控制，因为ip曾不向端系统提供显式的网络拥塞反馈

运行在发送方的tcp拥塞控制机制跟踪一个额外的变量：拥塞窗口congestion window

发送方的发送速率是 cwnd/RTT 字节/秒

“丢包事件”：出现超时或收到接收方的三个冗余ack

#### 指导性原则

* 一个丢失的报文段意味着阻塞，因此当丢失报文段是应当降低TCP发送方的速率
* 一个确认报文段指示该网络正在向接收方交付发送方的报文段，此时能够增加发送方的速率
* 带宽探测



TCP拥塞控制算法 TCP congestion control algorithm

1. 慢启动SS 2. 拥塞避免 3. 快速恢复

**慢启动**： cwnd的值以一个MSS开始，每个传输的报文段首次被确认就增加1。 如果存在一个超时丢包，发送方将cwnd设置为1并重新开始SS，同时将ssthresh（慢启动阈值）设为cwnd / 2。当cwnd = ssthresh时，结束慢启动进入拥塞避免。当检测到三个冗余ack，结束慢启动，进入快速恢复状态

**拥塞避免**：每个RTT只将cwnd的值增加一个MSS。三个冗余ack出现时，cwnd减半，+3，进入快速恢复阶段

**快速恢复**

加性增、乘性减additive-increase multiplicative-decrease AIMD

#### TCP吞吐量的宏观描述

TCP发送数据的速率是拥塞窗口与当前RTT的函数。  窗口长度w字节，往返时间RTT： w/RTT

丢包发生时，W代表w的值，则吞吐量在W/RTT和W/2*RTT变化

平均吞吐量：3W/4*RTT

#### 经高带宽路径的TCP

1. 公平性
2. 明确拥塞通告explicit congestion notification

