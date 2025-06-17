# Teste_Software_2025_-lvaro_Peixoto-Charlie_Fonseca-Rafael_Goto-Ryan_Carvalho
Primeira atividade de NPL


# Tutorial de Uso da Aplicação com NLTK

Este é um pequeno guia para uso do código produzido para NPL

---

## Passo 1 - Criar um Ambiente Virtual

Abra o terminal na pasta do projeto e execute os seguintes comandos:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
.venv\Scripts\activate
```

---

## Passo 2 - Criar o arquivo `requirements.txt`

Dentro da pasta do projeto, crie um arquivo chamado:

```
requirements.txt
```

E adicione a seguinte linha dentro dele:

```
nltk
```

---

## Passo 3 - Instalar as dependências

Com o ambiente virtual ativado, instale o **NLTK** usando o comando:

```bash
pip install -r requirements.txt
```

---

## Passo 4 - Exemplo de código em Python

Crie um arquivo chamado, por exemplo, `app.py` e adicione o seguinte código (ou utilize o código do repositorio):

```python
import nltk

# Caso ainda não tenha os recursos necessários do nltk, descomente a linha abaixo para fazer o download
# nltk.download('punkt')

minha_string = "O usuário enfrenta o problema de criar essa lista manualmente."
tokens = nltk.word_tokenize(minha_string)

print(tokens)
```

> **Observação:**  
Se for a primeira vez que você usa o NLTK, será necessário baixar o recurso de tokenização chamado **punkt**.  
Para isso, descomente a linha `nltk.download('punkt')` no código e execute o programa uma vez.

---

## Passo 5 - Rodar o código

No terminal (com o ambiente virtual ainda ativado), execute:

```bash
python app.py
```

---

## Resultado Esperado

Você verá a saída com os tokens da frase, algo como:

```
['O', 'usuário', 'enfrenta', 'o', 'problema', 'de', 'criar', 'essa', 'lista', 'manualmente', '.']
```


