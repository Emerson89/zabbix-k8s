# Zabbix-k8s
Este projeto irá configurar a instalação do zabbix-server em um cluster k8s.

## Dependencias

- kubernetes v1.27.6
- kubectl v.1.23.1

#
## TL;DR
 
 - Usando kustomize

### Apply

```
kubectl apply -k .
```

### Destroy

```
kubectl delete -k .
```
#

## acesso ao front

É criado um ingress *zabbix-ingress* para acesso via browser insira o ip do node:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: zabbix-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: "zabbix.SEU-IP.nip.io"
```

## envs

Password do user zabbix e root do mysql pode ser alterado usando *secrets-server.env* 

MYSQL_ROOT_PASSWORD=password

MYSQL_PASSWORD=zabbix

## alertscripts e externalscripts

Insira os scripts conforme sua necessidade nos diretorios correspondentes e no kustomization.yaml

```yaml
- name: secrets-alertscripts
  files:
  - alertscripts/slack.sh
  - alertscripts/new.sh
- name: secrets-externalscripts
  files:
  - externalscripts/monit.py
  - externalscripts/new.py
```

## backup

Será criado um cronjob que será executado a cada 10 minutos altere conforme sua necessidade

## restore

```
kubectl cp /zabbix.sql monitoring/mysql-podname:/tmp
zcat zabbix.sql.gz | mysql -u USUARIO -p PASSWORD DBNAME

```

# License
GPLv3

