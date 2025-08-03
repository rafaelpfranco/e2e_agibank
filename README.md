# E2E_AgiBank

Este é um projeto de automação de testes End-to-End (E2E) para o blog do AgiBank, utilizando **Playwright** com **Python**.

---

## 📖 Visão Geral do Projeto

Este projeto cobre automação de testes para três módulos principais do blog do AgiBank:

**1. Newsletter**

* Inscrição com e-mail válido
* Validação de campo vazio
* Validação de e-mail inválido

**2. SearchBar**

* Realizar busca com termo inexistente
* Realizar busca com termo existente

**3. Home**

* Abertura de uma postagem

---

## 🛠 Tecnologias Utilizadas

* **Python 3.11+**
* **Playwright**
* **pytest**
* **Faker** 
* **GitHub Actions**

---

## 📂 Estrutura de Pastas

```
├── .github/workflows/ci.yml       # Workflow de CI no Actions
├── config/                        # Configuração central e variáveis de ambiente
├── fixtures/                      # Fixtures de teste
├── pages/                         # Page Objects
├── tests/                         # Specs de teste
├── utils/                         # Utilitários
├── features/                      # Especificação dos cenários de teste
├── conftest.py                    # Fixtures globais
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação
```

---

## 🤝 Como Contribuir

1. Dê um **fork** no repositório;
2. Crie uma **branch** para sua feature (`git checkout -b feat/minha-feature`);
3. Faça as alterações e **commit** (`git commit -m 'Add minha feature'`);
4. **Push** para sua branch no fork;
5. Abra um **pull request** explicando suas mudanças.

---

## 🚀 Pipeline de CI (GitHub Actions)

O workflow `ci.yml` executa sempre que há push ou pull request em `master`, rodando os testes em paralelo nos navegadores **chromium**, **firefox** e **webkit**.

**Como usar localmente**:

```bash
# instalar venv
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.\.venv\\Scripts\\activate # Windows

# instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# rodar todos os testes
pytest -v

# rodar um teste específico
pytest tests/newsletter_test.py::TestNewsletter::test_newsletter_subscription
```

---
