#!/bin/bash

set -e

cmd="$*"

if [ "$1" = 'init' ]; then
  sh ./root-init.sh
elif [ "$1" = 'connect-cluster' ]; then
  sh ./cluster-connect.sh
else
  exec "$cmd"
fi