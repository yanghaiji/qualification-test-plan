# Qualification-Test-Plan

> Qualification-Test-Plan 是自我学习自动化测试过程中的实战总结，这里简称 qtp
> 大家可以根据自的需要进行增删，也欢迎大家共同维护
> 
> **有任何问问题大家可以添加微信 📧: 372787553**

## qtp 目录简介

```python

├───common  # 公共模块
├───config  # 常用的系统配置
├───data  # 用于存储数据驱动是的数据
├───logs  # 日志记录
├───page  # selenium 封装
├───page_element  # 页面元素数据配置
├───page_object  # 需要测试的测试类封装
├───report  # 生成的报告路径
├───script  # 其他常用脚本
├───testcase  # 测试的case
│   ├───interface  # 接口相关
│   ├───webui  # web自动化相关
├───utils  # 常用工具类
├───requirements.txt  # 项目相关依赖
├───pytest.ini  # pytest 只配置
├───main.py  # 测试类
├───run.py  # 启动类

```

> 本项目采用POM 设计模式，即Page Object Model
> 

## 项目依赖安装

### 虚拟环境初始化

- 进入项目
> cd  project directory

- 创建虚拟环境
> python -m venv venv
>
- 激活虚拟环境 
    - Windows:
    >.\venv\Scripts\activate.bat
    - Unix 或 MacOs 上：
    > source venv/bin/activate

  
### 安装项目依赖 在txt文件内

> pip install -r requirements.txt
> 
> 确保您的电脑已经安装了 selenium 的 webdriver

### 启动项目

> 安装完成后， 原则 rur.py进行项目启动，启动后则会在本地 report/html/ 内成绩测试报告