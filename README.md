# Portal de Apresentações - ADHONEP Capítulo 230

Portal oficial em HTML puro para o **Capítulo 230 da ADHONEP**, contendo o catálogo dinâmico de apresentações em slides interativos (Reveal.js) organizados em **ordem cronológica**, com busca instantânea, filtros por categoria e destaque do próximo encontro.

---

## 🌐 Link Público Ativo

👉 **[https://willianspedroso.github.io/adhonep230/](https://willianspedroso.github.io/adhonep230/)**

---

## 📁 Estrutura do Projeto

```text
adhonep230/
│
├── index.html                           <- Portal principal (Linha do Tempo + Destaque Josué)
├── apresentacoes.js                     <- Banco de dados do acervo (datas, títulos, tags)
├── generate_presentations.py            <- Script automático de conversão PPTX -> Reveal.js
│
├── APRESENTACAO_PRINCIPIO_CORAGEM.HTML  <- Próximo Encontro (Josué 1:9)
├── APRESENTACAO_SWOT_CRISTA.HTML        <- Análise SWOT Cristã & Empreendedora (12/08/2026)
├── APRESENTACAO_EGO_TRANSFORMADO.HTML   <- Ego Transformado - Timothy Keller (29/06/2026)
├── APRESENTACAO_COM_DEUS_E_POSSIVEL.HTML<- Com Deus, é Possível (18/05/2026)
├── APRESENTACAO_O_PODER_QUE_VOCE_POSSUI.HTML <- O Poder que Você Possui (23/03/2026)
├── APRESENTACAO_LIVRE_SE_DOS_RESSENTIMENTOS.HTML <- Livre-se dos Ressentimentos (23/02/2026)
├── APRESENTACAO_LIDERAR_E_SERVIR.HTML   <- Liderar é Servir (13/10/2025)
├── APRESENTACAO_VENDAS_HABILIDADE_CHAVE.HTML <- Vendas Habilidade-Chave (01/09/2025)
├── APRESENTACAO_VOCE_GOVERNA_A_SI_MESMO.HTML <- Você Governa a Si Mesmo? (26/08/2025)
│
└── README.md                            <- Documentação do sistema
```

---

## 🔄 Como o Sistema Funciona (Escalabilidade Fluida)

Como a quantidade de palestras e encontros tende a crescer de forma exponencial, o portal foi desacoplado do código visual:

1. **`apresentacoes.js`**: Centraliza todas as informações das apresentações (título, subtítulo, data real, tags, ícone e link).
2. **`index.html`**: Lê o arquivo `apresentacoes.js` dinamicamente:
   - Ordena os encontros automaticamente por data (mais recentes primeiro).
   - Permite que qualquer pessoa busque por palavras-chave (ex: "Josué", "Vendas", "Liderança").
   - Filtra por categorias (*Liderança*, *Negócios & Gestão*, *Inteligência Emocional*, *Vida & Fé*).
3. **`generate_presentations.py`**: Converte os arquivos `.pptx` diretamente para o padrão Reveal.js com design idêntico ao de Josué.

---

## 🚀 Como Adicionar uma Nova Apresentação no Futuro

### Método 1 (Automático com PPTX)
1. Coloque o novo arquivo `.pptx` na pasta `FEITA`.
2. Adicione os dados do encontro na lista `METADATA` do arquivo `generate_presentations.py`.
3. Execute no terminal:
   ```bash
   python generate_presentations.py
   ```
4. Faça o commit e push para o GitHub:
   ```bash
   git add .
   git commit -m "Nova apresentação adicionada"
   git push
   ```

### Método 2 (Direto no HTML)
1. Crie seu arquivo `APRESENTACAO_NOVA.HTML` na pasta.
2. Abra `apresentacoes.js` e adicione uma nova entrada no array:
   ```javascript
   {
       "id": "nova-palestra",
       "title": "Título da Palestra",
       "subtitle": "Subtítulo do tema",
       "date": "2026-11-15",
       "formattedDate": "15 de Novembro de 2026",
       "badge": "Encontro ADHONEP",
       "status": "proximo", // ou "realizado"
       "category": "Liderança",
       "tags": ["Liderança", "Decisão"],
       "icon": "🤝",
       "filename": "APRESENTACAO_NOVA.HTML",
       "desc": "Breve resumo da mensagem compartilhada.",
       "slidesCount": 12
   }
   ```
3. O `index.html` atualizará a ordem cronológica, busca e filtros automaticamente!
