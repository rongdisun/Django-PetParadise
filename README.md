---
title: Python Django 宠物乐园
date: 2023-08-23 00:25:21
tags:
---

## 1、简介

本项目是一个简单的宠物乐园项目，包含了宠物管理、领养管理、商品管理和评论管理等功能。

## 2、使用的技术

- python==3.10
- django==4.0
- bootstrap==5
- jquery==3.6

## 3、功能实现

- 用户功能
  - 用户注册
  - 用户登录
  - 用户信息创建与修改
  - 用户密码修改

- 宠物
  - 宠物发布（管理员）
  - 宠物领养（普通用户）
  - 宠物详情（宠物信息、领养宠物）

- 宠物商城
  - 商品列表
  - 商品发布（管理员）
  - 商品收藏
  - 商品购买
  - 商品收藏记录（商品被收藏的人数）
  - 提交订单
  - 我的订单（购买记录）

- 在线社区
  - 发布帖子
  - 跟帖
  - 富文本编辑器

- 权限控制
  - 普通用户的权限可以操作的功能
  - 管理员权限可以操作的功能

## 4、成品页面展示

#### 用户的注册和登录页面

![image-20230823004228146](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823004228146.png)

![image-20230823204851870](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823204851870.png)

#### 用户信息维护与修改

![image-20230823210804747](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823210804747.png)

#### 密码重置

![image-20230823210828525](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823210828525.png)

#### 宠物乐园首页

![image-20230823204952642](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823204952642.png)

#### 宠物详情页

详情页面会显示宠物的详细信息以及领养状态

在这里普通用户可以来申请领养，申请后并不会直接归属到申请者名下，还需要管理员进行审核，用户在管理员审核之前，该用户无法再次申请该宠物，但是不影响其他用户的申请。

同时如果用户没有登陆，直接点击申请领养会让用户进行登录

![image-20230823205100312](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823205100312.png)

#### 宠物领养记录

在这里我们可以查看自己的申请记录，以及一些其他的申请信息以及通过状态。

同时对于管理员通过审核的宠物，领养者可以对领养的宠物添加照片

![image-20230823205611857](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823205611857.png)

![image-20230823205819756](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823205819756.png)

#### 宠物商城

这里会显示宠物的一些商品，可以在宠物详情页查看宠物的详细信息，

可以对商品进行收藏和购买

![image-20230823205930786](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823205930786.png)

![image-20230823210019527](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823210019527.png)

#### 提交订单

在这里，我们可以编辑收货地址，也可以使用默认的地址。可以改变商品的数量。

![image-20230823210207060](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823210207060.png)

#### 在线论坛

在这里可以发布一些信息，不过需要用户进行登录。

在线论坛展示了帖子的观看次数、点赞和点踩，同时用户可以发布帖子

![image-20230823210335985](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823210335985.png)

**用户可以对帖子进行跟帖和评价，同时发帖和跟帖均使用了富文本编辑器**



![image-20230823210605811](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823210605811.png)

#### 管理员界面

##### 整体效果

![image-20230823210953818](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823210953818.png)

##### 添加宠物

![image-20230823210928077](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823210928077.png)

##### 审核用户的宠物申请

![image-20230823211029710](https://raw.githubusercontent.com/rongdisun/learn/main/img/image-20230823211029710.png)

## 4、获取源码

<img src="https://raw.githubusercontent.com/rongdisun/learn/main/img/5f13931de1631b1611043d8211573c7.jpg" alt="5f13931de1631b1611043d8211573c7" style="zoom:25%;" />
