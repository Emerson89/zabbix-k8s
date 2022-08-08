# Zabbix-k8s
Este projeto irá configurar a instalação do zabbix-server em um cluster k8s.

## Dependencias

- kubernetes v1.23.1
- kubectl v.1.23.1
- minikube v1.26.0

## Instalação

```
kubectl apply -f namespace.yaml
kubectl apply -f zabbix-front/.
kubectl apply -f zabbix-server/.
kubectl apply -f mysql/.
```
Criando um namespace chamado monitoring

Para ambiente de *teste* execute no minikube para instalação https://k8s-docs.netlify.app/en/docs/tasks/tools/install-minikube/ 
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

```
minikube service zabbix-web -n monitoring --url
```
A saída deve ser o ip ex: http://192.168.49.2:30080

# License
GPLv3
