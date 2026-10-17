import zipfile
import xml.etree.ElementTree as ET
import os
import re
import json

FEITA_DIR = r"E:\willians\adhonep\FEITA"
TARGET_DIR = r"E:\willians\adhonep\adhonep230"

# Imagens de fundo de altíssima qualidade (Unsplash) por temática
BACKGROUNDS = [
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1920&q=85",
    "https://images.unsplash.com/photo-1518495973542-4542c06a5843?auto=format&fit=crop&w=1920&q=85"
]

METADATA = [
    {
        'file': 'VOCE GOVERNA A SI MESMO.pptx',
        'id': 'voce-governa-a-si-mesmo',
        'filename': 'APRESENTACAO_VOCE_GOVERNA_A_SI_MESMO.HTML',
        'title': 'Você Governa a Si Mesmo?',
        'subtitle': 'Autogoverno, Inteligência Emocional e Maturidade nos Negócios',
        'date': '2025-08-26',
        'formattedDate': '26 de Agosto de 2025',
        'badge': 'Revista Meetings 14 • Lição 4',
        'category': 'Inteligência Emocional',
        'tags': ['Autogoverno', 'Inteligência Emocional', 'Maturidade', 'Liderança', 'Provérbios 16:32'],
        'icon': '🛡️',
        'desc': 'A força interior que conquista cidades. Como dominar as próprias emoções na pressão corporativa, superar rejeições e liderar a si mesmo com equilíbrio e sabedoria.'
    },
    {
        'file': 'VENDAS-HABILIDADE-CHAVE.pptx',
        'id': 'vendas-habilidade-chave',
        'filename': 'APRESENTACAO_VENDAS_HABILIDADE_CHAVE.HTML',
        'title': 'Vendas: A Habilidade-Chave por Trás de Toda Riqueza',
        'subtitle': 'A Ciência de Gerar Valor, Renda e Prosperidade',
        'date': '2025-09-01',
        'formattedDate': '01 de Setembro de 2025',
        'badge': 'Revista Meetings 14 • Lição 5',
        'category': 'Negócios & Gestão',
        'tags': ['Vendas', 'Geração de Receita', 'Negociação', 'Prosperidade', 'Mentalidade'],
        'icon': '📈',
        'desc': 'Por que saber vender é a habilidade mais importante do empresário e profissional. Técnicas e princípios práticos para destravar faturamento e criar negócios sustentáveis.'
    },
    {
        'file': 'LIDERAR_SERVIR.pptx',
        'id': 'liderar-e-servir',
        'filename': 'APRESENTACAO_LIDERAR_E_SERVIR.HTML',
        'title': 'Liderar é Servir: Treinar com Amor, Não com Rejeição',
        'subtitle': 'A Liderança que Forma Gigantes e Inspira Pessoas',
        'date': '2025-10-13',
        'formattedDate': '13 de Outubro de 2025',
        'badge': 'Revista Meetings 14 • Lição 10',
        'category': 'Liderança',
        'tags': ['Liderança Servidora', 'Gestão de Pessoas', 'Mentoria', 'Amor e Firmeza'],
        'icon': '👑',
        'desc': 'Liderar não é mandar nem controlar; é servir com visão. Como enxergar o potencial escondido em cada colaborador e liderar à luz do exemplo de Jesus.'
    },
    {
        'file': 'LIVRE-SE_DOS_RESSENTIMENTOS.pptx',
        'id': 'livre-se-dos-ressentimentos',
        'filename': 'APRESENTACAO_LIVRE_SE_DOS_RESSENTIMENTOS.HTML',
        'title': 'Livre-se dos Ressentimentos',
        'subtitle': 'O Poder Libertador do Perdão para Viver o Extraordinário',
        'date': '2026-02-23',
        'formattedDate': '23 de Fevereiro de 2026',
        'badge': 'Revista Meetings 10 • Lição 5',
        'category': 'Inteligência Emocional',
        'tags': ['Perdão', 'Cura Interior', 'Paz nos Negócios', 'Maturidade'],
        'icon': '🕊️',
        'desc': 'Um coração cheio de mágoas torna a caminhada pesada. Princípios práticos para soltar as amarras do passado, curar relacionamentos e prosperar com leveza.'
    },
    {
        'file': 'O_PODER_QUE_VOCE_POSSUI.pptx',
        'id': 'o-poder-que-voce-possui',
        'filename': 'APRESENTACAO_O_PODER_QUE_VOCE_POSSUI.HTML',
        'title': 'O Poder que Você Possui',
        'subtitle': 'Ação Direcionada, Mudança de Crenças e a Oração de Jabez',
        'date': '2026-03-23',
        'formattedDate': '23 de Março de 2026',
        'badge': 'Revista Meetings 9 • Lição 12',
        'category': 'Vida & Fé',
        'tags': ['Poder da Ação', 'Jabez', 'Crenças Fortalecedoras', 'Visão'],
        'icon': '⚡',
        'desc': 'Tem poder quem age na direção certa. Como alinhar o que você aceita como verdade em sua mente com o plano soberano de Deus para alargar suas fronteiras.'
    },
    {
        'file': 'COM_DEUS_E_POSSIVEL.pptx',
        'id': 'com-deus-e-possivel',
        'filename': 'APRESENTACAO_COM_DEUS_E_POSSIVEL.HTML',
        'title': 'Com Deus, é Possível',
        'subtitle': 'Planejamento Humano versus Direção e Soberania Divina',
        'date': '2026-05-18',
        'formattedDate': '18 de Maio de 2026',
        'badge': 'Café com Deus Pai',
        'category': 'Vida & Fé',
        'tags': ['Planejamento', 'Direção Divina', 'Isaías 43', 'Confiança'],
        'icon': '🌅',
        'desc': 'No mundo corporativo aprendemos a mitigar riscos e projetar cenários, mas é a fé que sustenta o passo. Quando a jornada não fizer sentido, confie no Criador.'
    },
    {
        'file': os.path.join('EGO_TRANSFORNADO', 'EGO_TRANSFORMADO.pptx'),
        'id': 'ego-transformado',
        'filename': 'APRESENTACAO_EGO_TRANSFORMADO.HTML',
        'title': 'Ego Transformado',
        'subtitle': 'A Verdadeira Humildade e a Liberdade Cristã (Timothy Keller)',
        'date': '2026-06-29',
        'formattedDate': '29 de Junho de 2026',
        'badge': 'Resumo Livro • Timothy Keller',
        'category': 'Inteligência Emocional',
        'tags': ['Timothy Keller', 'Humildade', 'Identidade', '1 Coríntios 4', 'Paz Interior'],
        'icon': '📖',
        'desc': 'O dilema da autoestima e a incessante busca por validação. Como a resposta de Paulo em 1 Coríntios 3-4 nos liberta do ego insaciável para uma paz inabalável.'
    },
    {
        'file': 'ANALISE_SWOT_EMPREENDEDORISCO.pptx',
        'id': 'swot-crista-empreendedora',
        'filename': 'APRESENTACAO_SWOT_CRISTA.HTML',
        'title': 'Análise SWOT Cristã & Empreendedora',
        'subtitle': 'Diagnóstico Estratégico e Mordomia Bíblica (Business as Mission)',
        'date': '2026-08-12',
        'formattedDate': '12 de Agosto de 2026',
        'badge': 'Business as Mission (BAM)',
        'category': 'Negócios & Gestão',
        'tags': ['SWOT', 'Estratégia', 'BAM', 'Mordomia', 'Governança'],
        'icon': '📊',
        'desc': 'Integrando forças, fraquezas, oportunidades e ameaças ao propósito de Reino. Os negócios como vocação sagrada e ferramenta de transformação social e espiritual.'
    }
]

def extract_pptx_slides(pptx_path):
    with zipfile.ZipFile(pptx_path, 'r') as z:
        slides = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
        def slide_num(s):
            m = re.search(r'slide(\d+)\.xml', s)
            return int(m.group(1)) if m else 999
        slides = sorted(slides, key=slide_num)
        
        parsed_slides = []
        for s in slides:
            tree = ET.fromstring(z.read(s))
            paras = []
            for p in tree.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}p'):
                # Pegar texto do parágrafo
                t_parts = [t.text for t in p.iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t') if t.text]
                full_text = ''.join(t_parts).strip()
                if full_text and not full_text.startswith('style.') and not full_text in ['ppt_w', 'ppt_h']:
                    paras.append(full_text)
            if paras:
                parsed_slides.append(paras)
        return parsed_slides

def generate_reveal_html(meta, slides_data):
    title = meta['title']
    subtitle = meta['subtitle']
    badge = meta['badge']
    
    sections_html = []
    
    # SLIDE 1: Abertura / Capa
    bg0 = BACKGROUNDS[0]
    sections_html.append(f"""
        <!-- SLIDE 1: CAPA -->
        <section data-background-image="{bg0}">
            <div class="glass-box" style="text-align: center;">
                <span class="badge">ADHONEP • Capítulo 230</span>
                <h1 style="font-size: 2.2em; margin: 16px 0 10px 0;">{title}</h1>
                <p style="font-size: 0.95em; color: var(--gold-light); font-weight: 400; margin-bottom: 20px;">
                    {subtitle}
                </p>
                <div class="speaker-cue">
                    🏛️ <strong>Encontro de Homens de Negócios</strong> • {badge}
                </div>
            </div>
            <aside class="notes">
                Boas-vindas a todos os empresários, executivos e convidados. Apresente o tema com entusiasmo e acolhimento.
            </aside>
        </section>
    """)
    
    # SLIDES DO PPTX
    for idx, slide_paras in enumerate(slides_data, 1):
        bg_img = BACKGROUNDS[idx % len(BACKGROUNDS)]
        
        # Analisar primeiro parágrafo como título se for curto ou título conhecido
        first_line = slide_paras[0] if len(slide_paras) > 0 else ""
        content_lines = slide_paras[1:] if len(slide_paras) > 1 else slide_paras
        
        # Verificar se é a Oração de Convite
        is_prayer = any('ORAÇÃO' in p.upper() or 'ORACAO' in p.upper() or 'LIVRO DA VIDA' in p.upper() for p in slide_paras)
        
        if is_prayer:
            # Layout especial para a Oração de Convite
            prayer_text = "<br>".join([f"<strong>{p}</strong>" if any(k in p.upper() for k in ['PAI', 'PERDÃO', 'SALVADOR', 'AMÉM']) else p for p in slide_paras if not ('ORAÇÃO' in p.upper() or 'ORACAO' in p.upper())])
            if not prayer_text.strip():
                prayer_text = "Pai, peço perdão por meus pecados.<br>Purifica-me com Teu sangue, pois hoje me torno uma nova pessoa.<br>Abro meu coração para que Tua alegria, paz e saúde reinem em minha vida e família.<br>Escreve meu nome no Livro da Vida, pois creio que Jesus é meu único e suficiente Salvador.<br><strong>Amém!</strong>"
            
            sections_html.append(f"""
        <!-- SLIDE: ORAÇÃO DE CONVITE -->
        <section data-background-image="{bg_img}">
            <div class="glass-box" style="text-align: center;">
                <span class="badge" style="background: linear-gradient(135deg, #d4af37, #96741b); color: #090d15;">Momento Especial</span>
                <h2 style="font-size: 2.1em; color: var(--gold-light); margin: 12px 0 16px 0;">Oração de Convite ADHONEP</h2>
                <div class="verse-box" style="font-size: 0.85em; line-height: 1.8; text-align: center; margin: 0 auto; max-width: 900px;">
                    {prayer_text}
                </div>
                <div class="speaker-cue" style="margin-top: 18px;">
                    🙏 Convide a todos a ficarem em pé ou inclinarem a cabeça para este momento solene de oração e decisão.
                </div>
            </div>
            <aside class="notes">
                Momento mais importante do encontro: convite para receber a Jesus e orar juntos a oração de entrega.
            </aside>
        </section>
            """)
            continue
            
        # Slide Normal de Conteúdo
        # Detectar se há versículo bíblico
        has_bible = any(any(book in p for book in ['Provérbios', 'Isaías', 'Coríntios', 'Salmos', 'Josué', 'Mateus', 'João', 'Romanos', 'Ec ']) for p in slide_paras)
        
        slide_title = first_line if len(first_line) < 60 else title
        body_items = [p for p in content_lines if p != slide_title]
        
        body_html = ""
        for p in body_items:
            # Se for citação bíblica
            if any(book in p for book in ['Provérbios', 'Isaías', 'Coríntios', 'Salmos', 'Josué', 'Mateus', 'João', 'Romanos', 'Ec ']):
                body_html += f'<div class="verse-box">{p}</div>\n'
            elif p.startswith('#'):
                # Tag de vídeo ou observação
                body_html += f'<div class="speaker-cue">🎬 <strong>Recurso:</strong> {p.replace("#", "").strip()}</div>\n'
            elif len(p) > 100 or p.endswith('.'):
                body_html += f'<p style="font-size: 0.78em; line-height: 1.6; margin-bottom: 12px; color: #eceff4;">{p}</p>\n'
            else:
                body_html += f'<li style="margin-bottom: 8px;">{p}</li>\n'
                
        if '<li>' in body_html:
            # envolver em ul
            body_html = f'<ul style="font-size: 0.75em; line-height: 1.6; margin: 12px 0 16px 20px;">\n{body_html}\n</ul>'
            
        sections_html.append(f"""
        <!-- SLIDE {idx + 1} -->
        <section data-background-image="{bg_img}">
            <div class="glass-box">
                <span class="badge">{badge}</span>
                <h2 style="font-size: 1.7em; margin-bottom: 16px;">{slide_title}</h2>
                <div class="content-body">
                    {body_html}
                </div>
            </div>
            <aside class="notes">
                Aborde cada ponto conectando com a realidade do empresário e profissional liberal.
            </aside>
        </section>
        """)

    all_sections = "\n".join(sections_html)

    html_template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | ADHONEP Capítulo 230</title>
    
    <!-- Reveal.js CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/theme/night.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {{
            --gold: #d4af37;
            --gold-light: #f3e5ab;
            --dark-bg: rgba(12, 18, 28, 0.88);
            --card-bg: rgba(255, 255, 255, 0.08);
        }}

        .reveal {{
            font-family: 'Montserrat', sans-serif;
            color: #f4f4f6;
        }}

        .reveal h1, .reveal h2, .reveal h3 {{
            font-family: 'Cormorant Garamond', serif;
            text-transform: none;
            color: var(--gold-light);
            font-weight: 700;
            letter-spacing: 0.5px;
            margin: 0 0 12px 0;
            line-height: 1.15;
            text-shadow: 0 4px 15px rgba(0,0,0,0.7);
        }}

        .glass-box {{
            background: var(--dark-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(212, 175, 55, 0.35);
            border-radius: 16px;
            padding: 26px 36px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.65);
            text-align: left;
            max-width: 1280px;
            margin: 0 auto;
            box-sizing: border-box;
        }}

        .badge {{
            display: inline-block;
            background: var(--gold);
            color: #0c121c;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.48em;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 8px;
        }}

        .verse-box {{
            background: rgba(212, 175, 55, 0.12);
            border-left: 4px solid var(--gold);
            padding: 14px 20px;
            margin: 14px 0;
            border-radius: 0 10px 10px 0;
            font-style: italic;
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.05em;
            color: #fbfbfd;
            line-height: 1.45;
        }}

        .speaker-cue {{
            margin-top: 14px;
            padding-top: 10px;
            border-top: 1px dashed rgba(255,255,255,0.2);
            font-size: 0.55em;
            color: #b8c4d0;
            font-style: italic;
            line-height: 1.35;
        }}

        /* Botão para voltar à página inicial */
        .back-home-button {{
            position: fixed;
            top: 16px;
            left: 16px;
            z-index: 99999;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(12, 18, 28, 0.85);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            color: var(--gold-light);
            border: 1px solid rgba(212, 175, 55, 0.35);
            padding: 8px 16px;
            border-radius: 30px;
            font-family: 'Montserrat', sans-serif;
            font-size: 13px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.25s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        }}

        .back-home-button:hover {{
            background: rgba(212, 175, 55, 0.95);
            color: #0c121c;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
        }}
    </style>
</head>
<body>

<!-- Botão Voltar ao Portal -->
<a href="index.html" class="back-home-button" title="Voltar ao Portal do Capítulo 230">
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg>
    <span>Portal ADHONEP 230</span>
</a>

<div class="reveal">
    <div class="slides">
{all_sections}
    </div>
</div>

<!-- Reveal.js Scripts -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/notes/notes.min.js"></script>

<script>
    Reveal.initialize({{
        width: 1400,
        height: 800,
        margin: 0.04,
        minScale: 0.2,
        maxScale: 2.0,
        hash: true,
        transition: 'fade',
        backgroundTransition: 'fade',
        controls: true,
        progress: true,
        center: true,
        plugins: [ RevealNotes ]
    }});
</script>

</body>
</html>
"""
    return html_template

def main():
    catalog = []
    
    # 1. Adicionar o PRÓXIMO ENCONTRO (Coragem - Josué)
    catalog.append({
        'id': 'principio-coragem-josue',
        'title': 'O Princípio da Coragem nos Negócios',
        'subtitle': 'Governança, Estratégia (SWOT & BSC) e Fé à luz de Josué 1:9',
        'date': '2026-10-25',
        'formattedDate': 'Próximo Encontro • Outubro/2026',
        'badge': 'Próximo Encontro',
        'status': 'proximo',
        'category': 'Liderança',
        'tags': ['Josué', 'Coragem', 'Liderança', 'Decisão', 'SWOT', 'BSC'],
        'icon': '⚔️',
        'filename': 'APRESENTACAO_PRINCIPIO_CORAGEM.HTML',
        'desc': 'Uma jornada prática e espiritual inspirada na liderança de Josué. Como superar a paralisia do medo, tomar decisões firmes e liderar com fé e autoridade no mercado corporativo.',
        'slidesCount': 12
    })
    
    # 2. Processar os PPTX anteriores
    for meta in METADATA:
        pptx_path = os.path.join(FEITA_DIR, meta['file'])
        if not os.path.exists(pptx_path):
            print(f"Arquivo não encontrado: {pptx_path}")
            continue
            
        print(f"Processando {meta['file']}...")
        slides_data = extract_pptx_slides(pptx_path)
        
        # Gerar o arquivo HTML
        html_content = generate_reveal_html(meta, slides_data)
        target_path = os.path.join(TARGET_DIR, meta['filename'])
        
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"  -> Gerado: {meta['filename']} ({len(slides_data) + 1} slides)")
        
        # Adicionar ao catálogo de encontros realizados
        catalog.append({
            'id': meta['id'],
            'title': meta['title'],
            'subtitle': meta['subtitle'],
            'date': meta['date'],
            'formattedDate': meta['formattedDate'],
            'badge': meta['badge'],
            'status': 'realizado',
            'category': meta['category'],
            'tags': meta['tags'],
            'icon': meta['icon'],
            'filename': meta['filename'],
            'desc': meta['desc'],
            'slidesCount': len(slides_data) + 1
        })
        
    # Salvar apresentacoes.js
    js_content = f"// Catálogo oficial de Apresentações - ADHONEP Capítulo 230\n// Este arquivo é lido dinamicamente pelo index.html\n\nconst APRESENTACOES = {json.dumps(catalog, ensure_ascii=False, indent=4)};\n"
    
    js_path = os.path.join(TARGET_DIR, "apresentacoes.js")
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"\nCatálogo salvo com sucesso em: {js_path} ({len(catalog)} apresentações)")

if __name__ == "__main__":
    main()
