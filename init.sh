#!/bin/sh

# -------- When rhc_smoke run before -------

BASEPATH=$(cd `dirname $0` ; pwd)
echo $BASEPATH
export PYTHONPATH=$PATHONPATH:$BASEPATH

> ~/.openshift/servers.yml
> log/smoke.log

mv -f $HOME/.openshift/express.conf $HOME/.openshift/express.conf.bak
cp config/express.conf $HOME/.openshift/
echo "Copy Config File .... done"


# -------- rhc_smoking -------

echo "Rhc Smoke Test Start ..."
./bin/rhc_smoke.py
echo "Rhc Smoke Test Finish ..."

# -------- When rhc_smoke done --------
echo "-----------------R E S U L T---------------------"
echo -n `date\n` > result/rhc_smoke.result
grep -rn 'fail' log/smoke.log >> result/rhc_smoke.result
cat result/rhc_smoke.result
echo "-----------------Clean Account ------------------"
./bin/account.py
echo "done"
echo "-----------------Delete mid file-----------------"
rm -rf app*
rm -rf sapp
rm -rf testfile
rm -rf ajboss
rm -rf qphp
rm -rf teamapp
echo "done"








