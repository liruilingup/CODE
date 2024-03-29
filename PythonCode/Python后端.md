# range和xrange的区别
range()返回一个递增或递减的数字列表，列表的元素由三个参数决定
xrange则不会直接生成一个list，而是每次调用返回其中的一个值，内存空间使用极少，因而性能非常好
[range和xrange的区别详解](https://www.cnblogs.com/huangbiquan/p/7897145.html)

# Python的is和=的区别
Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。

is和==都是对对象进行比较判断作用的，但对对象比较判断的内容并不相同
== 是比较两个对象的内容是否相等，即两个对象的“值“”是否相等，不管两者在内存中的引用地址是否一样。
is 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同。即is比较两个条件：1.内容相同。2.内存中地址相同

[Python中is和==的区别](https://www.cnblogs.com/wangkun122/p/9082088.html)

# 可迭代对象、迭代器与生成器的区别
（1）迭代器就是用于迭代操作的对象，可以记住遍历位置，迭代器基本方法有iter()和next()；

（2）生成器是一种特殊的迭代器，返回值不通过return而是通过yield;

（3）使用iter内置函数可以获取迭代器的对象。如果对象实现了能返回迭代器的__iter__方法，那么对象就是可迭代的

# Python深拷贝和浅拷贝
也就是地址的复制还是值的复制的区别，深拷贝和浅拷贝就是可变元素的拷贝

深拷贝是将对象本身复制给另一个对象，就是完全跟以前就没有任何关系了，原来的对象怎么改都不会影响当前对象。

浅拷贝是将对象的引用复制给另一个对象，原对象的元素改变的话会改变当前对象，如果当前对象中list元素改变了，也同样会影响原对象。

#  *args 和 **kwargs
如果我们不知道将多少个参数传递给函数，比如当我们想传递一个列表或一个元组值时，就可以使用*args。
当我们不知道将会传入多少关键字参数时，使用**kwargs 会收集关键字参数

# Python 中的 pass 语句
写代码时，有时可能只写了函数声明而没想好函数怎么写，但为了保证语法检查的正确必须输入一些东西。在这种情况下，我们使用 pass 语句。
类似的 break 语句可以跳出循环，continue 语句可以跳到下一轮循环。

# Post和Get请求的区别
* GET和POST是HTTP请求的两种基本方法

GET参数通过URL传递，POST放在Request body中。
GET请求参数会被完整保留在浏览器历史记录里，而POST中的参数不会被保留。
GET请求参数会被完整保留在浏览器历史记录里，而POST中的参数不会被保留。

GET和POST本质上就是TCP链接，并无差别。但是由于HTTP的规定和浏览器/服务器的限制，导致他们在应用过程中体现出一些不同。 

对于GET方式的请求，浏览器会把http header和data一并发送出去，服务器响应200（返回数据）；

而对于POST，浏览器先发送header，服务器响应100 continue，浏览器再发送data，服务器响应200 ok（返回数据）。




# Http协议
超文本传输协议HTTP协议被用于在Web浏览器和网站服务器之间传递信息
# http和https的区别
    1、https协议需要到ca申请证书，一般免费证书较少，因而需要一定费用。

    2、http是超文本传输协议，信息是明文传输，https则是具有安全性的ssl加密传输协议。
    
    3、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。

    4、http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。
　　
[参考链接](https://www.cnblogs.com/wqhwe/p/5407468.html)



# 解决Linux TIME_WAIT过多造成的问题
time_wait的作用：
1）可靠地实现TCP全双工连接的终止
2）允许老的重复分节在网络中消逝



