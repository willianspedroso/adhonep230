# Portal de Apresentações - ADHONEP Capítulo 230

Site em HTML puro com identidade visual da ADHONEP (Capítulo 230), contendo descrição do propósito do capítulo e catálogo/menu com acesso direto a todas as apresentações interativas.

---

## 📁 Estrutura de Arquivos

```text
site_apresentacao/
│
├── index.html                           <- Página inicial (Portal & Menu de Apresentações)
├── APRESENTACAO_PRINCIPIO_CORAGEM.HTML  <- Apresentação em Reveal.js
└── README.md                            <- Guia de uso e publicação gratuita
```

---

## 🚀 Como Testar no Computador

Basta dar dois cliques no arquivo **`index.html`** para abrir em qualquer navegador (Google Chrome, Edge, Safari, Firefox). Não requer instalação de Node.js, banco de dados ou servidor complexo.

---

## ➕ Como Adicionar uma Nova Apresentação

1. Salve seu novo arquivo HTML na mesma pasta (exemplo: `APRESENTACAO_LIDERANCA.HTML`).
2. Abra o arquivo `index.html` em um editor de texto ou código.
3. Localize a área `<div class="presentations-grid">`.
4. Copie o bloco de um dos cards e atualize o título, a descrição e o link no botão:
   ```html
   <a href="APRESENTACAO_LIDERANCA.HTML" class="btn-open" target="_blank">
       <span>Abrir Apresentação</span>
   </a>
   ```

---

## 🌐 Como Publicar de Graça na Internet

### Opção 1: Netlify Drop (A mais rápida - 30 segundos, sem comandos)
1. Acesse: **[app.netlify.com/drop](https://app.netlify.com/drop)**
2. Crie uma conta gratuita (com seu e-mail ou conta do Google).
3. Arraste a pasta inteira `site_apresentacao` para o círculo indicado na página.
4. Pronto! O Netlify vai gerar um link instantâneo com HTTPS (exemplo: `adhonep230.netlify.app`).
5. Nas configurações do Netlify você pode alterar o subdomínio para o nome que quiser de graça (ex: `adhonep-capitulo230.netlify.app`).

### Opção 2: GitHub Pages (Para guardar o histórico no GitHub)
1. Crie uma conta no **[GitHub](https://github.com)** se ainda não tiver.
2. Crie um repositório novo (exemplo: `adhonep230`).
3. Suba os arquivos da pasta para o repositório.
4. No repositório, clique em **Settings** > **Pages** (no menu lateral esquerdo).
5. Em **Branch**, selecione `main` (ou `master`) e a pasta `/ (root)`, depois clique em **Save**.
6. Em cerca de 1 minuto seu site estará online no endereço: `https://seu-usuario.github.io/adhonep230/`.

### Opção 3: Vercel
1. Acesse: **[vercel.com](https://vercel.com)**
2. Conecte com sua conta do GitHub e importe o repositório com 1 clique.
3. O deploy é feito automaticamente.
