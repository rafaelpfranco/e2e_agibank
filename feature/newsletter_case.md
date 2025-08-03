# Casos de Teste

## ✅ Cenário NL1: Inscrição com e-mail válido

**Passos**

1. Acessar a página de newsletter
2. Preencher o campo de e-mail com endereço válido (ex: fixture `generate_person_data`)
3. Clicar no botão “Assinar”

**Resultado Encontrado**
Redirecionamento para URL contendo `?subscribe=success#subscribe-blog-blog_subscription-3`
Mensagem de sucesso visível na tela

**Resultado Esperado**
URL termina com `?subscribe=success#subscribe-blog-blog_subscription-3`
Texto da mensagem igual a `NewsletterTexts.SUCCESS_MESSAGE`

---

## ✅ Cenário NL2: Inscrição com e-mail vazio

**Passos**

1. Acessar a página de newsletter
2. Deixar o campo de e-mail em branco ou preencher apenas com espaço
3. Clicar no botão “Assinar”

**Resultado Encontrado**
O input de e-mail fica no estado inválido (`:invalid`)
Bolha nativa exibe mensagem de validação

**Resultado Esperado**
`validationMessage` do input igual a `NewsletterTexts.EMPTY_MESSAGE`

---

## ✅ Cenário NL3: Inscrição com e-mail inválido

**Passos**

1. Acessar a página de newsletter
2. Preencher o campo de e-mail com string sem `@` (ex: `email_invalido`)
3. Clicar no botão “Assinar”

**Resultado Encontrado**
O input de e-mail fica no estado inválido (`:invalid`)
Bolha nativa exibe mensagem de validação truncada

**Resultado Esperado**
`validationMessage` do input igual a `NewsletterTexts.INVALID_EMAIL_MESSAGE`

---
