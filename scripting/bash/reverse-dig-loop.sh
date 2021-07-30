#!/bin/bash

NET=18.7.22

for n in $(seq 1 254); do
  ADDR=${NET}.${n}
  echo -e "${ADDR}\t$(dig -x ${ADDR} +short)"
done
