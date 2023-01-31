#!/bin/bash

##############################################################
# Displays the RAM consumption of one or more processes
# Example: bash mem_usage.sh apache2 docker
##############################################################

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'

# Colors reset
COLOROFF='\033[0m'

PROCESS="${@}"

if [[ -z ${PROCESS} ]]
then
    echo -e "${RED}Vous devez donner le nom d'un ou plusieurs processus en paramètre.${COLOROFF}"
    echo -e "Par exemple : ${BLUE}bash mem_usage.sh docker-proxy dockerd${COLOROFF}"
else
    for EXPRESSION in $(echo ${PROCESS})
    do
        RAMUSAGE=$(ps -ely | awk -v process=${EXPRESSION} '$13 == process' | awk '{SUM += $8/1024} END {print SUM}'| cut -d "." -f1)
        if [[ -z ${RAMUSAGE} ]]
        then
            echo -e "${RED}Le processus ${EXPRESSION} n'existe pas ou n'est pas activé.${COLOROFF}"
        else
            echo -e "${GREEN}RAM consommée pour ${EXPRESSION} : ${RAMUSAGE} MB${COLOROFF}"
        fi
    done
fi


