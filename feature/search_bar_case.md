# Casos de Teste

## ✅ Cenário SR1: Busca com termo existente

**Passos**

1. Acessar a página inicial do blog
2. Inserir um termo existente no campo de busca (ex: `existing_term`)
3. Pressionar Enter ou clicar no botão de busca

**Resultado Encontrado**
Redirecionamento para URL contendo `?s=<termo>`
Heading “Resultados encontrados para:” + termo visível
Lista de posts relacionados exibida

**Resultado Esperado**
URL termina com `?s=<termo>`
`get_search_term()` retorna o termo buscado
`get_article_count()` retorna valor > 0
Todos os cards de notícias estão visíveis

---

## ✅ Cenário SR2: Busca sem resultados

**Passos**

1. Acessar a página inicial do blog
2. Inserir um termo inexistente no campo de busca (ex: `no_results_term`)
3. Pressionar Enter ou clicar no botão de busca

**Resultado Encontrado**
Redirecionamento para URL contendo `?s=<termo>`
Heading “Resultados encontrados para:” + termo visível
Nenhum post relacionado encontrado

**Resultado Esperado**
URL termina com `?s=<termo>`
`get_search_term()` retorna o termo buscado
`get_article_count()` retorna 0
