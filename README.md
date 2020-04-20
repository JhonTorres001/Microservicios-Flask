## Microservicios Con Flask  [![Build Status](https://travis-ci.org/pantsel/konga.svg?branch=master)](https://travis-ci.org/pantsel/konga)    [![Gitter chat](https://badges.gitter.im/pantsel-konga/Lobby.png)](https://gitter.im/pantsel-konga/Lobby)

Ejercicio de microservicios con flask

Se plantea establecer una arquitectura orientada a microservicios usando el micro-framework flask para ofrecer la implementación de los servicios de:

 - Suma 
 - Resta
 - Multiplicación
 - División.

# Presentado a: 
- Ingeniero Alejandro Daza

# Integrantes:

- Wilson Heli Villamizar Valencia (20201099050) 
- Alejandro Lopez Castañeda       (20201099037)
- Jhon Fredy Torres Ramírez       (20201099048)

## Arquitectura Propuesta

Arquitectura de referencia propuesta de Kong - Kong Inc.

![arq](https://user-images.githubusercontent.com/15526824/79803656-068c2600-8328-11ea-9c14-fba27198ce0a.png)


## Herramientas seleccionadas 

- Python 3.6
- Docker Desktop 19.03.8
- Flask 1.1.2
- Kong 2.0.3 
- Konga 2.0.3
- Insomnia
- Azure
- VSC

## Explicación de despliegue

Kong es una capa de abstracción de microservicios nativa de la nube, rápida, escalable y distribuida (también conocida como API Gateway o API Middleware) . Disponible como proyecto de código abierto en 2015, sus valores principales son alto rendimiento y extensibilidad.

Mantenido activamente, Kong es ampliamente utilizado en la producción en compañías que van desde nuevas empresas hasta Global 5000, así como organizaciones gubernamentales.

### Instalar Kong

docker run -d --name kong-database \
              -p 5432:5432 \
              -e POSTGRES_USER=kong \
              -e POSTGRES_DB=kong \
              postgres:9.4

docker run -d --name kong \
              --link kong-database:kong-database \
              -e KONG_DATABASE=postgres \
              -e KONG_PG_HOST=kong-database \
              -p 8000:8000 \
              -p 8443:8443 \
              -p 8001:8001 \
              -p 7946:7946 \
              -p 7946:7946/udp \
              kong:0.10.1
              
### Configurar Httpie

host=<tu-hostname-externo>
alias http='docker run -it --rm mcampbell/httpie'
http httpbin.org/headers
http $host:8000
 
### Registrar Un API

http POST $host:8001/apis name=demo hosts=$host upstream_url=http://httpbin.org
http $host:8000/headers Host:$host
Activar Plugin Key-Auth
http POST $host:8001/apis/demo/plugins name=key-auth
http $host:8000/headers Host:$host
 
### Crear Usuario Alice

http POST $host:8001/consumers username=alice custom_id=alice@wonderland.com
http POST $host:8001/consumers/alice/key-auth key=1111
http POST $host:8001/consumers/alice/key-auth key=2222
 
### Probar Autenticación

http $host:8000/headers Host:$host apikey:1111
http DELETE $host:8001/consumers/alice/key-auth/1111

### Instalacion Konga
https://github.com/pantsel/konga/blob/master/README.md

![Captura de pantalla 2020-04-20 a la(s) 5 24 45 p  m](https://user-images.githubusercontent.com/15526824/79805528-f9713600-832b-11ea-94b9-76094817c33f.png)

## Pugins:

- Authentication
- Security
- Traffic Control
- Serverless
- Analytics & Monitoring
- Transformations
- Logging

## License
```
The MIT License (MIT)
=====================

Copyright (c) 2015 Panagis Tselentis

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
