#!/bin/sh

docker build -t frr-image:prd -f Dockerfile .
if [ `echo $?` == 0 ]; then
	docker rm -f frr
	docker run -dt --restart=always -p 8008:8008 --name frr frr-image:prd
fi