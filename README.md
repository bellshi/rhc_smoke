rhc_smoke
=========
a framework for rhc_smoke test

### Introduction

rhc smoke case link : https://tcms.engineering.redhat.com/plan/4962/test-plan-for-openshift-2-0#testcases

add new case : wirte new case in rhc_smoke/case folder.

### Setup

Please prepare two accounts, one is updated to silver plan.

Then set env(dev|int|stg) and accounts in rhc_smoke/config/express.conf. 

### How to Start

git clone this repo

cd rhc_smoke

./init.sh

### Result

detail log is in rhc_smoke/log

fail result is in rhc_smoke/result

Enjoy it !

If you have problems, please feel free to contact with cshi@redhat.com
