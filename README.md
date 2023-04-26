# Mitre ATT&CK Data
API para visualização das diretriz para classificar e descrever ataques cibernéticos e intrusões. [MitreATT&CK](https://attack.mitre.org/).

-----
## Requisitos

- Python >= 3.6
- virtualenv
- uvicorn

## Complemento 
 - [Flutter APP](https://github.com/mitre-attack-data/app) • Run in Android and Chrome

## Executando Localmente

#### Venv
Crie um ambiente virtual e o ative.
```sh
python3 -m venv venv
source venv/bin/activate
```

Instale os pacotes e rode a aplicação.

```sh
make install
make run-dev
```

#### Docker
```sh
make build-run
```

#### Deploy on Heroku
É preciso ter o CLI do Heroku, estar logado e ter um app criado para fazer o deploy.
```sh
make deploy
```
