#!/bin/bash

set -e

if [ "$1" = 'init' ]; then
  sh ./root-init.sh
elif [ "$1" = 'connect-cluster' ]; then
  sh ./cluster-connect.sh
fi