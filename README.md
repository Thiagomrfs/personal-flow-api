# README

Este é um guia para executar o projeto PersonalFlow, uma API desenvolvida em Django. Ele fornecerá as instruções necessárias para configurar um ambiente virtual opcional e iniciar o projeto.

## Configuração do Ambiente

A criação de um ambiente virtual é uma prática recomendada para isolar as dependências do projeto e garantir a consistência do ambiente de desenvolvimento.

### Instalação do Virtualenv (opcional)

Se você ainda não tem o `virtualenv` instalado, você pode instalá-lo usando o `pip`, que é o gerenciador de pacotes padrão do Python:

```bash
pip install virtualenv
```

### Criação do Ambiente Virtual (opcional)

Dentro do diretório raiz do projeto, você pode criar um ambiente virtual executando o seguinte comando:

#### Windows

```bash
virtualenv nome_do_ambiente
```

#### Unix/Linux

```bash
python3 -m venv nome_do_ambiente
```

Isso criará um novo diretório chamado `nome_do_ambiente` no qual todas as dependências serão instaladas.

### Ativação do Ambiente Virtual (opcional)

Para ativar o ambiente virtual, você pode executar o seguinte comando:

#### Windows

```bash
.\nome_do_ambiente\Scripts\activate
```

#### Unix/Linux

```bash
source nome_do_ambiente/bin/activate
```

### Instalação das Dependências

Uma vez que o ambiente virtual está ativado (ou se você optou por não criar um ambiente virtual), você pode instalar todas as dependências do projeto usando o `pip`. Certifique-se de estar no diretório raiz do projeto e execute o seguinte comando:

```bash
pip install -r requirements.txt
```

Isso instalará todas as dependências listadas no arquivo `requirements.txt`.

## Executando o Projeto

Após configurar o ambiente e instalar as dependências, você está pronto para executar o projeto PersonalFlow.

Certifique-se de estar no diretório raiz do projeto e execute o seguinte comando:

```bash
python manage.py runserver
```

Isso iniciará o servidor de desenvolvimento do Django, e a API PersonalFlow estará disponível em [http://localhost:8000/](http://localhost:8000/).

## Conclusão

Este arquivo README forneceu instruções básicas para configurar e executar o projeto PersonalFlow, uma API desenvolvida em Django. Sinta-se à vontade para personalizar este arquivo e adicionar mais informações relevantes ao seu projeto.