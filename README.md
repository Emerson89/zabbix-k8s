# Zabbix-k8s
Este projeto irá configurar a instalação do zabbix-server em um cluster k8s.

## Dependencias

- kubernetes v1.23.1
- kubectl v.1.23.1
- minikube v1.26.0


<img src="epYhW2k.png"
     alt="Smiley face"
     width="42" height="42" style="border:5px solid black"
     style="float: left; margin-right: 10px;" />  

## Instalação

```
kubectl apply -f namespace.yaml
kubectl apply -f zabbix-front/.
kubectl apply -f zabbix-server/.
kubectl apply -f mysql/.
```
Criando um namespace chamado monitoring

**CASO FOR USAR O BANCO DE DADOS EM CONTAINER EXISTE O CRONJOB QUE EXECUTA O BACKUP PARA O PV DO CONTAINER**

Para ambiente de **teste** execute no minikube para instalação https://k8s-docs.netlify.app/en/docs/tasks/tools/install-minikube/ 

Aguarde e acompanhe os logs no zabbix-server enquanto o schema do banco é executado
```
** Preparing Zabbix server
** Using MYSQL_USER variable from ENV
** Using MYSQL_PASSWORD variable from ENV
** Using MYSQL_ROOT_PASSWORD variable from ENV
********************
* DB_SERVER_HOST: mysql
* DB_SERVER_PORT: 3306
* DB_SERVER_DBNAME: zabbix
********************
** Creating 'zabbix' user in MySQL database
** Database 'zabbix' already exists. Please be careful with database COLLATE!
** Creating 'zabbix' schema in MySQL
```
Terminado execute o comando

## Acesso ao front

É criado um ingress *zabbix-ingress* para acesso via browser é preciso configurar o arquivo hosts para acesso ao dns interno, para utilizar no minikube habilite usando o comando:
```
minikube addons enable ingress
```
```
NAME             CLASS   HOSTS               ADDRESS        PORTS   AGE
zabbix-ingress   nginx   zabbix.example.io   192.168.49.2   80      2d3h
```
Exemplo de conf /etc/hosts:
```
192.168.49.2 zabbix.example.io
```

## Secrets Zabbix-server

Para integração e monitoramento externo utilize o *zabbix-server-secret.yaml* realize a criptografia dos arquivos 
```
echo 'conteudo a ser criptografado' | base64
```

## Backup

Será criado um cronjob que será executado a cada 10 minutos altere conforme sua necessidade, criando um disco persistente em */mnt/backup* 

## Restore

```
kubectl cp /mnt/backup/zabbix.sql monitoring/mysql-podname:/tmp
zcat zabbix.sql.gz | mysql -u USUARIO -p PASSWORD DBNAME

```

# License
GPLv3
