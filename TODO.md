## Adjustments and improvements

### 🔐 Autenticação & Usuários

- [X] Implementar **User model customizado** (UUID, campos essenciais, sem vazamento de PII)
- [ ] Integrar **JWT Authentication** (SimpleJWT)
  - [X] Login (access/refresh)
  - [X] Refresh token
  - [X] Logout (blacklist)
- [ ] Endpoint de **registro de usuário**
- [ ] Endpoint para **perfil do usuário autenticado**
- [ ] (Opcional) Verificação de e-mail

---

### 🏪 Perfis (Customer / Seller)

- [X] Criar modelo **Customer** (OneToOne com User)
- [ ] Criar modelo **Seller**
  - [X] Nome da loja
  - [X] Descrição / links
- [ ] Permissões customizadas (seller-only actions)
- [ ] Endpoints para gerenciamento de perfil

---

### 📦 Produtos

- [ ] Criar modelo **Product**
  - [ ] Nome
  - [ ] Descrição
  - [ ] Preço
  - [ ] Moeda
  - [ ] Estoque
  - [ ] Seller (FK)
- [ ] Upload de imagens (MEDIA)
- [ ] CRUD de produtos (DRF)
- [ ] Permitir criação/edição apenas por sellers
- [ ] Endpoint público de listagem e detalhe

---

### 🛒 Carrinho de Compras

- [ ] Criar modelo **Cart**
- [ ] Criar modelo **CartItem**
- [ ] Endpoints:
  - [ ] Adicionar item
  - [ ] Remover item
  - [ ] Atualizar quantidade
- [ ] Carrinho vinculado ao usuário autenticado
- [ ] Cálculo de subtotal e total

---

### 🧾 Pedidos (Orders)

- [ ] Criar modelo **Order**
- [ ] Criar modelo **OrderItem**
- [ ] Status do pedido (enum)
- [ ] Criar pedido a partir do carrinho
- [ ] Endpoints:
  - [ ] Criar pedido
  - [ ] Listar pedidos do usuário
  - [ ] Detalhar pedido
- [ ] Garantir que usuário só veja seus próprios pedidos

---

### ⭐ Avaliações (Ratings / Reviews)

- [ ] Criar modelo **ProductReview**
- [ ] Uma avaliação por usuário por produto
- [ ] Campos:
  - [ ] Nota (rating)
  - [ ] Comentário
- [ ] Endpoint para criar avaliação
- [ ] Endpoint para listar avaliações do produto
- [ ] Calcular média e total de avaliações no produto

---

### 🔍 Busca e Filtros Avançados

- [ ] Busca por nome e descrição
- [ ] Filtro por faixa de preço
- [ ] Filtro por seller
- [ ] Ordenação por preço
- [ ] Ordenação por rating
- [ ] Paginação nos endpoints de listagem

---

### 🔒 Segurança

- [ ] Configurar CORS corretamente
- [ ] Garantir uso de `USE_TZ = True`
- [ ] Não expor dados sensíveis em serializers
- [ ] Validar uploads (tipo e tamanho de arquivos)
- [ ] Permissões bem definidas por endpoint

---

### 📄 Documentação

- [ ] Integrar Swagger / OpenAPI (drf-spectacular ou drf-yasg)
- [ ] Atualizar README:
  - [ ] Como rodar o projeto
  - [ ] Variáveis de ambiente
  - [ ] Estrutura de pastas
- [ ] Exemplos de requests (curl / Postman)

---

### 🧪 Testes

- [ ] Testes de autenticação
- [ ] Testes de permissões
- [ ] Testes de produtos
- [ ] Testes de pedidos
- [ ] Testes de fluxo completo (integração)
