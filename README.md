# Key Value Store using gRPC and Python

**PUC Minas - Laboratório de Desenvolvimento de Aplicações Móveis e Distribuídas**

**Student:** Guilherme Diniz  
**Student ID:** 637423  
**Teacher:** Hugo de Paula  

## Requirements
  - Python3
  - Protocoll Buffer Compiler (if you with to recompile the .proto file to another language)

## Instructions
  1- Install the Python packages:
  
  ```sh
  pip install -r requirements.txt
  ```

  2- Run the server:
  
  ```sh
    cd src/keyValueStore
    python KeyValueServer.py
  ```
  
  3- Run the client:
  
  ```sh
  cd src/keyValueStore
  python keyValueClient.py commands # See avaiable commands below
  ```

## Available client commands:
  - put *key* *value*
  - get *key*
  - getAllKeys
