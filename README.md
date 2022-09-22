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
