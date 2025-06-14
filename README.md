# Escuta Cidadã – Backend

Este repositório contém a parte de backend da aplicação **Escuta Cidadã** e a estrutura do banco de dados.

## Tecnologias Utilizadas

- **Django** -
- **Python** -
- **Render** - 
- **PostgreSQL** -  
  
 ## 🚀 O projeto já está hospedado e funcionando online

O back-end da aplicação está hospedado no Render e já pode ser acessado via API pelo front-end publicado.

---

## 💻 Como Rodar o Projeto Localmente

Para rodar o back-end do *Escuta Cidadã* localmente, siga os passos abaixo.

### 1. Clonar o Repositório

Clone o repositório usando o Git:
```
git clone https://github.com/GuilhermeAzevedo01/Escuta-Cidada-Back.git
```
## 2. Navegar até o Diretório do Projeto
```
cd Escuta-Cidada-Back
```
## 3. Criar Ambiente Virtual
```
feedback/scripts/activate 
```
## 4. Instalar as Dependências
```
pip install -r requirements.txt
```
## 5. Configurar o Banco de Dados
Por padrão, o projeto utiliza PostgreSQL. Para testes locais, você pode configurar o banco no settings.py

## 6. Rodar as Migrações
```
python manage.py makemigrations
```
```
python manage.py migrate
```
## 7. Iniciar o Servidor
```
python manage.py runserver
```

## Funcionalidades do BackEnd

- **API para recebimento de feedbacks** -
- **Armazenamento de dados no PostgreSQL** -
- **Estrutura modular com Django Apps** -
- **Validação dos dados enviados** -
- **Painel de administração com Django Admin** -
- **Deploy via Render** -


