#!/bin/env bash
# TheHive stack install script Shell
# Colors
GREEN="\033[0;32m"
BLUE="\033[0;34m"
RED="\033[0;31m"

# Colors reset
COLOROFF='\033[0m'

# Port SSH
SSH="22/tcp"

# Local Variables
LOGDAY=$(date '+%d-%m-%Y')
LOGTIME=$(date '+%d-%m-%Y %H:%M:%S')
LOGFILE=/var/log/install/install_$LOGDAY.log

# Binary file paths
FAIL2BAN="/etc/init.d/fail2ban"
UFW="/usr/sbin/ufw"

# Checking if root user
function is_root() {
    if [ "$(whoami)" != "root" ]; then
            echo  -e "${RED}Permission not granted, Please run the script with administrator privileges"
            exit 1
    fi
}

# Script exit function if one of the binaries is not installed
function die() {
    echo "$@" >&2 ;
    exit 1
}

function random_string() {
    cat /dev/urandom | tr -dc A-Za-z0-9\^\$\*\@\%\! | head -c 64
}

function random_alpha_num() {
    cat /dev/urandom | tr -dc A-Za-z0-9 | head -c 12
}

function update() {
    echo -e "${BLUE}Update in progress...${COLOROFF}"
    apt-get update
    sleep 0.3
    apt-get -y upgrade
    apt-get -y autoremove
    echo -e "${GREEN}Update completed successfully${COLOROFF}"
}

# Binaries install function
function install_ufw() {
    # Install Firewall
    mkdir /var/log/install
    if [ ! -f ${UFW} ]; then
        echo -e "${BLUE}# ufw Firewall NOT installed, installing...${COLOROFF}"
        echo "$LOGTIME" "ufw Firewall NOT installed, installing..." >> "$LOGFILE"
        apt-get install -y ufw
        ufw default deny incoming
        ufw default allow outgoing
        ufw allow ${SSH}
        ufw allow from 78.199.223.11
        sudo ufw enable
        echo -e "${BLUE}# ufw Firewall installed and enabled${COLOROFF}"
        echo "$LOGTIME" "ufw Firewall installed and enabled" >> "$LOGFILE"
        sleep 0.4
        echo -e "${GREEN}# UFW Firewall ports for SSH and TheHive stack configured${COLOROFF}"
        echo "$LOGTIME" "UFW Firewall ports for SSH and TheHive stack configured" >> "$LOGFILE"
        if [ -f ${UFW} ]; then
            echo -e "${GREEN}# ufw is successfully installed${COLOROFF}"
            echo "$LOGTIME" "ufw is successfully installed" >> "$LOGFILE"
        else
            echo "$LOGTIME" "Problem installing ufw binary" >> "$LOGFILE"
            echo ""
            die "# Failed to install ufw binary.";
        fi
    else
        ufw default deny incoming
        ufw default allow outgoing
        ufw allow ${SSH}
        ufw allow from 78.199.223.11
        sudo ufw enable
        echo -e "${GREEN}# ufw is already installed and configured${COLOROFF}"
        echo "$LOGTIME" "ufw is already installed and configured" >> "$LOGFILE"
    fi
}

function install_fail2ban() {
    # install fail2ban
    if [ ! -f ${FAIL2BAN} ]; then
        echo -e "${BLUE}# fail2ban NOT installed, installing...${COLOROFF}"
        echo "$LOGTIME" "Installation of fail2ban binary in progress..." >> "$LOGFILE"
        apt-get install -y fail2ban
        sleep 1
        # We create a file for the configuration of the jails
        cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
        cd /etc/fail2ban/ || return
        sed -i "s/^dbpurgeage[[:blank:]]*=.*/dbpurgeage = 864000/" /etc/fail2ban/fail2ban.conf
        sed -i '/^\#ignoreip/a ignoreip = 78.199.223.11' /etc/fail2ban/jail.local
        sed -i '92d' /etc/fail2ban/jail.local
        sed -ie '/^\[sshd]/a port = 22' /etc/fail2ban/jail.local
        sed -ie '/^\[sshd]/a enabled = true' /etc/fail2ban/jail.local
        sed -i "s/^bantime[[:blank:]]*= 10m/bantime = 604800/" /etc/fail2ban/jail.local
        sed -ie '/^\[recidive]/a enabled = true' /etc/fail2ban/jail.local
        sed -i '817d' /etc/fail2ban/jail.local
        # We launch fail2ban
        sleep 1
        fail2ban-client -x start

        mkdir scripts

        cd scripts || return
        wget -q --show-progress https://raw.githubusercontent.com/Kr4v3N/Scripts-Bash/master/checklist_ban.sh
        mv checklist_ban.sh checklist_ban
        chmod +x checklist_ban
        cp -- * /usr/local/bin

        if [ -f ${FAIL2BAN} ]; then
            echo -e "${GREEN}# fail2ban is successfully installed${COLOROFF}"
            echo "$LOGTIME" "fail2ban is successfully installed" >> "$LOGFILE"
        else
            echo "$LOGTIME" "Problem installing fail2ban binary" >> "$LOGFILE"
            echo ""
            die "# Failed to install fail2ban binary." ;
        fi
    else
        # We create a file for the configuration of the jails
        cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
        cd /etc/fail2ban/ || return
        sed -i "s/^dbpurgeage[[:blank:]]*=.*/dbpurgeage = 864000/" /etc/fail2ban/fail2ban.conf
        sed -i '/^\#ignoreip/a ignoreip = 78.199.223.11' /etc/fail2ban/jail.local
        sed -i '92d' /etc/fail2ban/jail.local
        sed -ie '/^\[sshd]/a port = 22' /etc/fail2ban/jail.local
        sed -ie '/^\[sshd]/a enabled = true' /etc/fail2ban/jail.local
        sed -i "s/^bantime[[:blank:]]*= 10m/bantime = 604800/" /etc/fail2ban/jail.local
        sed -ie '/^\[recidive]/a enabled = true' /etc/fail2ban/jail.local
        sed -i '817d' /etc/fail2ban/jail.local
        # We launch fail2ban
        sleep 1
        fail2ban-client -x start
        echo -e "${GREEN}# fail2ban is already installed and configured${COLOROFF}"
        echo "$LOGTIME" "fail2ban is already installed and configured">> "$LOGFILE"
    fi
}

function install_docker(){
    # install Docker
    echo "Installing Docker..."
    apt-get remove docker docker-engine docker.io containerd runc
    apt-get update
    apt-get install ca-certificates curl gnupg lsb-release -y
    mkdir -p /etc/apt/keyrings

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    chmod a+r /etc/apt/keyrings/docker.gpg
    apt-get update
    apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
    systemctl enable docker.service
    systemctl enable containerd.service

    echo "Installing Docker Compose..."
    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

    mkdir thehive_project
    cd thehive_project || return
    # TODO: À mettre à jour
    wget -q --show-progress https://gist.githubusercontent.com/Kr4v3N/abc8ce49a7667bd9d56c7f6af25329f0/raw/b4b228c278c69d0d8073be81077f688069795c16/aide_memoire_docker-compose
    wget -q --show-progress https://gist.githubusercontent.com/Kr4v3N/76a8673c9328bce38812e8db3393b52a/raw/c460f27ea8eb4f9622f74e5b0304bd61a1221fce/docker-compose.yaml
    mv aide_memoire_docker-compose cmd_docker.txt

    touch .env
    {
    echo "THEHIVE_VERSION=5.0.18-1"
    echo "THEHIVE_PASS_SECRET=$(random_string)"
    echo ""
    echo "MINIO_ACCESS_KEY=minioadmin"
    echo "MINIO_SECRET_KEY=$(random_string)"
    echo ""
    echo "CORTEX_PORT=9001"
    echo "CORTEX_API_KEY=$(random_string)"
    echo "CORTEX_VERSION=3.1.7-1-withdeps"
    echo ""
    echo "CASSANDRA_CLUSTER_NAME=TheHive"
    echo ""
    echo "ELASTIC_VERSION=7.17.4"
    echo "ELASTIC_XPACK_SECURITY=false"
    echo "ELASTIC_CLUSTER_NAME=hive"
    echo ""
    echo "MINIO_ROOT=minioadmin"
    echo "MINIO_PASSWORD=$(random_string)"
    echo ""
    echo "MISP_VERSION=core-v2.4.164a"
    echo "MISP_MYSQL_HOST=misp_mysql"
    echo "MISP_MYSQL_DATABASE=mispdb"
    echo "MISP_MYSQL_USER=mispuser"
    echo "MISP_MYSQL_PASSWORD=$(random_string)"
    echo "MISP_MISP_ADMIN_EMAIL=mispadmin@lab.local"
    echo "MISP_ADMIN_PASS=$(random_string)"
    echo "BASEURL_MISP=localhost"
    echo "MISP_TIMEZONE=Europe/Paris"
    echo "MISP_INIT=true"
    echo "MISP_CRON_USER_ID=1"
    echo "MISP_REDIS_FQDN=redis"
    echo "MISP_HOSTNAME=https://212.227.30.1"
    echo ""
    echo "MISP_MYSQL_VERSION=5.7"
    echo ""
    echo "REDIS_VERSION=5.0.6"
    echo ""
    echo "MISP_MODULES_VERSION=modules-latest"
    echo "MISP_MODULES_REDIS_BACKEND=redis"
    echo ""
    echo "MARIADB_VERSION=10.7"
    echo ""
    echo "GLPI_VERSION=10.0.2"
    } >> .env

    touch mariadb.env
    {
    echo "MARIADB_ROOT_PASSWORD=$(random_alpha_num)"
    echo "MARIADB_DATABASE=Databse_$(random_alpha_num)"
    echo "MARIADB_USER=glpi_user_$(random_alpha_num)"
    echo "MARIADB_PASSWORD=$(random_string)"
    } >> mariadb.env

    touch mysqldb.env
    {
    echo "MYSQL_DATABASE=mispdb"
    echo "MYSQL_USER=mispuser"
    echo "MYSQL_PASSWORD=$(random_alpha_num)"
    echo "MYSQL_ROOT_PASSWORD=$(random_alpha_num)"
    } >> mysqldb.env

    mkdir -p thehive/conf
    cd thehive/conf || return

    touch application.conf
    {
    echo "## MISP configuration"
    echo "# Enable MISP connector"
    echo "play.modules.enabled += org.thp.thehive.connector.misp.MispModule"
    echo "misp {"
    echo " interval: 1 hour"
    echo " servers: ["
    echo "   { "
    echo "      name = 'MISP_CYROP'"
    echo "      url = 'https://misp'"
    echo "      auth {"
    echo "         type = key "
    echo "         key = '5oiKfNi1b1I4pzjeg7yvgnWDSflaJNWDP2ACwBLl'"
    echo "         }"
    echo "      wsConfig {}"
    echo "      caseTemplate = "MISP-EVENT""
    echo "      tags = ["tag1", "tag2", "tag3"]"
    echo "      includedTheHiveOrganisations = ["Cyrop"]"
    echo "   }"
    echo "  ]"
    echo "}"
    echo ""
    echo ""
    echo "## Cortex configuration"
    echo "# Enable Cortex connector"
    echo "play.modules.enabled += org.thp.thehive.connector.cortex.CortexModule"
    echo "cortex {"
    echo "  servers: ["
    echo "    {"
    echo "      name: "CORTEX_CYROP"      # Cortex name"
    echo "      url: "http://cortex:9001" # URL of Cortex instance"
    echo "      auth {"
    echo "        type: "bearer""
    echo "        key: "3fxFSvDTHl4j6V/r08FZkpGN1fYqdTuL"  # Cortex API key"
    echo "      }"
    echo "      wsConfig {}                  # HTTP client configuration (SSL and proxy)"
    echo "    }"
    echo "  ]"
    echo "}"
    } >> application.conf
}

is_root;
update;
install_ufw;
install_fail2ban;
install_docker;

