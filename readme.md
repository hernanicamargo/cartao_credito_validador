# Projeto: Validador de Cartão de Crédito

## Descrição
Este projeto é um validador de cartões de crédito. Ele foi desenvolvido utilizando Python com o framework Flask e tem como propósito verificar a validade de números de cartões de crédito utilizando o algoritmo de Luhn.

## Como executar o projeto

1. **Pré-requisitos**:
    - Certifique-se de ter o Python 3.x instalado em sua máquina.

2. **Instalação**:
    - Clone o repositório para sua máquina local:
      ```bash
      git clone [URL do repositório]
      ```
    - Navegue até o diretório do projeto:
      ```bash
      cd cartao_credito_validador
      ```
    - Crie e ative um ambiente virtual:
      ```bash
      python -m venv venv
      source venv/bin/activate # No Windows: venv\Scripts\activate
      ```
    - Instale as dependências necessárias:
      ```bash
      pip install -r requirements.txt
      ```

3. **Execução**:
    - Para iniciar o servidor Flask, execute o seguinte comando:
      ```bash
      flask run
      ```
    - Acesse o projeto em `http://localhost:5000`.

4. **Testes** (opcional):
    - Para rodar os testes, utilize o comando:
      ```bash
      pytest
      ```

## Observações
- Certifique-se de configurar corretamente as variáveis de ambiente, se necessário.
- Caso encontre problemas, verifique se todas as dependências estão instaladas corretamente.

