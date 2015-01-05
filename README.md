rhc_smoke
=========

a framework for rhc_smoke test

rhc_smoke/
│
├── bin
│   ├── account.py         ------ 测试账户工具（清理app）
│   ├── analysis.py        ------ 测试结果分析工具
│   └── rhc_smoke.py       ------ 主程序
├── case
│   └── example.py         ------ 测试用例
├── config 
│   ├── express.conf       ------ 测试配置文件（账户，环境）
│   ├── log.conf           ------ 日志配置文件
│   └── rhc_smoke.list     ------ 测试用例列表
├── init.sh                ------ 初始化脚本
├── lib
│   ├── check.py           ------ 正则表达式检查
│   ├── check.pyc               
│   ├── option.py          ------ 加载测试配置文件
│   ├── option.pyc         
│   ├── setup.py           ------ 初始化测试
│   └── setup.pyc
├── log
│   └── example.log        ------ 测试日志
├── README.md
└── result
    └── example.result     ------ 根据测试日志使用测试结果分析工具得到的可读性测试报告
