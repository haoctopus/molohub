## **【简介】**

![img](README/xmolo-zx.png)

这是一个将本地的HA控制网页反向代理到公网, 这样公网就可以轻松访问到HA控制台页面, 并控制家里已经连上HA的硬件. 基于安全方面的考虑, 该组件需要经过Google, GitHub或微信小程序的授权才能正常使用.

由于Home Assistant运行于局域网下, 想要通过外网远程访问HA, 首先HA部署环境所在网络下的路由器支持端口映射(port mapping), 映射后在公网通过ip:port直接访问，同时为了方便访问还需要一个ddns服务来把wan ip和动态域名绑定。但是由于网络供应商的网络环境复杂性, 以及用户自身内网环境复杂性, 很难系统性地总结一套通用有效的方法来实现. 上述技术实施起来比较繁琐, 对普通用户来说门槛较高, 本组件旨在简化用户进行远程访问本地HA控制网络.

**【安装软件】**

- [molohub组件](https://github.com/haoctopus/molohub)
  下载molohub文件夹，保存在`HomeAssistant配置目录/custom_components/`目录中。

**【HA中配置实例】**

```yaml
molohub:
```

**【相关链接】**
平台入口网站：<http://www.molo.cn>
molohub组件：<https://github.com/haoctopus/molohub>

**【效果展现】**
![img](README/molo_info.png)
****
![img](README/molo_login.png)
****
![img](README/molo_info2.png)
****
![img](README/molo_wechat_suc.png)