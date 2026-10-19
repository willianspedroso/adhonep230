import os

with open("img1.b64", "r") as f:
    img1_b64 = f.read()

with open("img46.b64", "r") as f:
    img46_b64 = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Análise SWOT Cristã & Empreendedora | ADHONEP Capítulo 230</title>
    
    <!-- Reveal.js CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/theme/night.min.css">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>
        :root {{
            --gold: #d4af37;
            --gold-light: #f3e5ab;
            --dark-bg: rgba(12, 18, 28, 0.90);
            --card-bg: rgba(255, 255, 255, 0.07);
            --green-border: rgba(46, 204, 113, 0.4);
            --red-border: rgba(231, 76, 60, 0.4);
            --blue-border: rgba(52, 152, 219, 0.4);
            --orange-border: rgba(230, 126, 34, 0.4);
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
            padding: 24px 34px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
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

        .badge-green {{
            background: #27ae60;
            color: #ffffff;
        }}

        .badge-red {{
            background: #c0392b;
            color: #ffffff;
        }}

        .badge-blue {{
            background: #2980b9;
            color: #ffffff;
        }}

        .badge-orange {{
            background: #d35400;
            color: #ffffff;
        }}

        /* Versículos */
        .verse-box {{
            border-left: 4px solid var(--gold);
            padding-left: 18px;
            margin: 12px 0;
            font-family: 'Cormorant Garamond', serif;
            font-style: italic;
            font-size: 1.08em;
            color: #ffffff;
            line-height: 1.4;
            background: rgba(212, 175, 55, 0.08);
            border-radius: 0 8px 8px 0;
            padding: 10px 18px;
        }}

        /* Dicas do Orador */
        .speaker-cue {{
            margin-top: 14px;
            padding-top: 10px;
            border-top: 1px dashed rgba(255,255,255,0.2);
            font-size: 0.52em;
            color: #b8c4d0;
            font-style: italic;
            line-height: 1.35;
        }}

        /* Grids SWOT */
        .grid-2x2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
            margin-top: 12px;
        }}

        .grid-3col {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 14px;
            margin-top: 12px;
        }}

        .grid-4col {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-top: 12px;
        }}

        .card-item {{
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 14px 16px;
            font-size: 0.62em;
            line-height: 1.45;
        }}

        .card-item h4 {{
            font-family: 'Montserrat', sans-serif;
            font-size: 1.08em;
            color: var(--gold-light);
            margin: 0 0 6px 0;
            font-weight: 600;
        }}

        .card-item.strength {{
            border-top: 3px solid #2ecc71;
        }}
        .card-item.strength h4 {{
            color: #a8f0c6;
        }}

        .card-item.weakness {{
            border-top: 3px solid #e74c3c;
        }}
        .card-item.weakness h4 {{
            color: #fab1a0;
        }}

        .card-item.opportunity {{
            border-top: 3px solid #3498db;
        }}
        .card-item.opportunity h4 {{
            color: #a0d8ef;
        }}

        .card-item.threat {{
            border-top: 3px solid #e67e22;
        }}
        .card-item.threat h4 {{
            color: #fed330;
        }}

        /* Matriz SWOT Consolidada (Slide 9) */
        .matrix-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            font-size: 0.58em;
        }}

        .matrix-header {{
            background: rgba(212, 175, 55, 0.15);
            border: 1px solid rgba(212, 175, 55, 0.4);
            padding: 8px 12px;
            text-align: center;
            font-weight: 700;
            color: var(--gold-light);
        }}

        .matrix-cell {{
            border: 1px solid rgba(255, 255, 255, 0.12);
            padding: 12px 14px;
            vertical-align: top;
            width: 50%;
            background: rgba(255, 255, 255, 0.03);
            line-height: 1.45;
        }}

        .matrix-cell.s {{ border-left: 3px solid #2ecc71; }}
        .matrix-cell.w {{ border-left: 3px solid #e74c3c; }}
        .matrix-cell.o {{ border-left: 3px solid #3498db; }}
        .matrix-cell.t {{ border-left: 3px solid #e67e22; }}

        .matrix-cell strong {{
            display: block;
            margin-bottom: 6px;
            font-size: 1.1em;
        }}

        .matrix-cell ul {{
            margin: 0;
            padding-left: 18px;
        }}

        /* Fluxo / Estágios */
        .flow-container {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            margin-top: 16px;
        }}

        .flow-step {{
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.15), rgba(255, 255, 255, 0.04));
            border: 1px solid var(--gold);
            padding: 14px 16px;
            border-radius: 12px;
            font-size: 0.58em;
            line-height: 1.4;
            flex: 1;
            text-align: center;
        }}

        .flow-step strong {{
            display: block;
            color: var(--gold-light);
            font-size: 1.15em;
            margin-bottom: 6px;
        }}

        .flow-arrow {{
            color: var(--gold);
            font-size: 1.2em;
            font-weight: bold;
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

        <!-- SLIDE 1: IMAGEM DE ABERTURA OFICIAL -->
        <section data-background-image="data:image/png;base64,{img1_b64}">
            <div class="glass-box" style="margin-top: 360px; text-align: center;">
                <span class="badge">ADHONEP • Capítulo 230</span>
                <h1 style="font-size: 2.1em; margin: 4px 0;">Negócios como Missão</h1>
                <p style="font-size: 0.78em; color: var(--gold-light); font-weight: 400; margin: 0;">
                    Análise SWOT Cristã & Empreendedora • Visão de Reino e Gestão Estratégica
                </p>
            </div>
            <aside class="notes">
                Slide de abertura oficial do encontro da ADHONEP. Acolha os empresários e participantes com alegria e passe para a introdução.
            </aside>
        </section>

        <!-- SLIDE 2: TÍTULO & PROPÓSITO -->
        <section data-background-image="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box" style="text-align: center;">
                <span class="badge">Diagnóstico Estratégico</span>
                <h2>Análise SWOT Cristã & Empreendedora</h2>
                <p style="font-size: 0.8em; color: #e6e6e6; margin: 12px 0 20px 0; line-height: 1.5;">
                    Integrando Diagnóstico Estratégico de Negócios aos Princípios da Mordomia Bíblica e Visão de Reino (<em>Business as Mission</em>)
                </p>
                <div class="speaker-cue">
                    💬 <strong>Abertura:</strong> "Empreender não é apenas gerar receita; é cumprir um propósito divino. Hoje vamos usar uma das maiores ferramentas de gestão do mundo — a Análise SWOT — alinhada aos princípios inegociáveis da Palavra de Deus."
                </div>
            </div>
            <aside class="notes">
                Introduza a relevância de unir competência técnica de gestão com a ética e os princípios cristãos.
            </aside>
        </section>

        <!-- SLIDE 3: PROPÓSITO & FÉ NO MERCADO -->
        <section data-background-image="https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge">Visão de Reino</span>
                <h2>Propósito & Fé no Mercado</h2>
                <div class="verse-box">
                    “A Análise SWOT no empreendedorismo cristão une a prudência do planejamento empresarial à sabedoria bíblica, capacitando líderes a servirem com integridade, gerarem valor e honrarem a Deus.”
                </div>
                <div class="grid-2x2">
                    <div class="card-item strength">
                        <h4>🏛️ Prudência Estratégica</h4>
                        Mapeamento lúcido e realista da operação, do mercado e das decisões corporativas.
                    </div>
                    <div class="card-item opportunity">
                        <h4>⚖️ Sabedoria Bíblica</h4>
                        Governança baseada na justiça, verdade e no compromisso de ser testemunho vivo nos negócios.
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 Fé sem planejamento gera imprudência; planejamento sem fé gera ansiedade. O equilíbrio é a chave.
                </div>
            </div>
            <aside class="notes">
                Ressalte que o empresário cristão não deve ser ingênuo nos negócios, mas prudente como a serpente e simples como a pomba.
            </aside>
        </section>

        <!-- SLIDE 4: CONCEITOS-CHAVE DO EMPREENDEDOR CRISTÃO -->
        <section data-background-image="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge">Fundamentos</span>
                <h2>Conceitos-Chave do Empreendedor Cristão</h2>
                <div class="grid-3col">
                    <div class="card-item strength">
                        <h4>1. Business as Mission (BAM)</h4>
                        O trabalho e os negócios vistos como vocação sagrada e campo de missão, gerando impacto econômico, social e espiritual na comunidade.
                    </div>
                    <div class="card-item opportunity">
                        <h4>2. Mordomia Fiel</h4>
                        Compreensão de que Deus é o verdadeiro dono dos recursos e do negócio. O empreendedor atua como um gestor prudente, sábio e fiel.
                    </div>
                    <div class="card-item threat">
                        <h4>3. Cultura de Excelência</h4>
                        Trabalhar não apenas para agradar homens, mas com padrão de excelência de Reino (<em>Colossenses 3:23</em>), criando valor real e sustentável.
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 Sua empresa não é um acidente; é a sua plataforma de testemunho diário diante de clientes, fornecedores e equipe.
                </div>
            </div>
            <aside class="notes">
                Explique o conceito de Business as Mission: o empresário é um missionário no mercado de trabalho.
            </aside>
        </section>

        <!-- SLIDE 5: S - FORÇAS (STRENGTHS) -->
        <section data-background-image="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge badge-green">Fator Interno • Positivo</span>
                <h2>S - Forças (Strengths): Fortalezas de Reino</h2>
                <div class="grid-2x2">
                    <div class="card-item strength">
                        <h4>🛡️ Integridade e Ética Inegociáveis</h4>
                        Cumprimento rigoroso de acordos, transparência fiscal, contratual e respeito às leis.
                    </div>
                    <div class="card-item strength">
                        <h4>🤝 Liderança Servidora</h4>
                        Gestão baseada no respeito, valorização sincera da equipe e ambiente de trabalho harmonioso.
                    </div>
                    <div class="card-item strength">
                        <h4>💎 Padrão de Excelência</h4>
                        Entrega de produtos e serviços de altíssima qualidade como forma de honrar a Deus e ao cliente.
                    </div>
                    <div class="card-item strength">
                        <h4>⚓ Resiliência Fundamentada</h4>
                        Perseverança nas crises e tempestades apoiada na oração, na fé inabalável e na paciência.
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 Quais são as fortalezas que diferenciam a sua empresa da concorrência no mercado atual?
                </div>
            </div>
            <aside class="notes">
                Destaque que a reputação de integridade é um ativo intangível de valor incalculável nos dias de hoje.
            </aside>
        </section>

        <!-- SLIDE 6: W - FRAQUEZAS (WEAKNESSES) -->
        <section data-background-image="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge badge-red">Fator Interno • Alerta</span>
                <h2>W - Fraquezas (Weaknesses): Pontos Cegos</h2>
                <div class="grid-2x2">
                    <div class="card-item weakness">
                        <h4>⚠️ Negligência Devocional e Familiar</h4>
                        <em>Workaholismo</em> desmedido, sacrificando o lar, o cônjuge, os filhos e a intimidade com Deus.
                    </div>
                    <div class="card-item weakness">
                        <h4>🔒 Centralização Excessiva</h4>
                        Falta de delegação e ausência de gestão profissional por receio, desconfiança ou perfeccionismo.
                    </div>
                    <div class="card-item weakness">
                        <h4>⚡ Impulsividade e Ansiedade</h4>
                        Decisões precipitadas sem autocontrole; dominar a si mesmo vale mais que conquistar cidades (<em>Pv 16:32</em>).
                    </div>
                    <div class="card-item weakness">
                        <h4>🚫 Incapacidade de Dizer Não</h4>
                        Aceitar contratos desvantajosos, sócios duvidosos ou assumir riscos incompatíveis com o porte da empresa.
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 Reconhecer fraquezas não é sinal de derrota, mas de maturidade para corrigir a rota a tempo.
                </div>
            </div>
            <aside class="notes">
                Toque no equilíbrio familiar: de nada adianta ganhar o mercado inteiro e perder a própria família.
            </aside>
        </section>

        <!-- SLIDE 7: O - OPORTUNIDADES (OPPORTUNITIES) -->
        <section data-background-image="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge badge-blue">Fator Externo • Positivo</span>
                <h2>O - Oportunidades: Terreno de Crescimento</h2>
                <div class="grid-2x2">
                    <div class="card-item opportunity">
                        <h4>💡 Inovação e Impacto Social</h4>
                        Resposta a problemas reais da sociedade com modelos de negócios sustentáveis e soluções éticas.
                    </div>
                    <div class="card-item opportunity">
                        <h4>🌟 Reputação no Mercado</h4>
                        Clientes e parceiros corporativos buscam cada vez mais empresas sérias e confiáveis.
                    </div>
                    <div class="card-item opportunity">
                        <h4>🤝 Redes de Cooperação e Mentoria</h4>
                        Parcerias estratégicas com outros empresários e líderes de valores alinhados (como na ADHONEP).
                    </div>
                    <div class="card-item opportunity">
                        <h4>🌱 Geração de Empregos Dignos</h4>
                        Oportunidade de transformar vidas e famílias inteiras através do trabalho justo e da capacitação.
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 O mercado está sedento de empresas que entregam o que prometem e tratam clientes com verdade.
                </div>
            </div>
            <aside class="notes">
                Incentive o networking de alto nível e as oportunidades que surgem dentro dos capítulos da ADHONEP.
            </aside>
        </section>

        <!-- SLIDE 8: T - AMEAÇAS (THREATS) -->
        <section data-background-image="https://images.unsplash.com/photo-1518495973542-4542c06a5843?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge badge-orange">Fator Externo • Alerta</span>
                <h2>T - Ameaças (Threats): Desafios do Mercado</h2>
                <div class="grid-2x2">
                    <div class="card-item threat">
                        <h4>⚔️ Pressão por Atalhos Éticos</h4>
                        Concorrência desleal, propostas escusas, propinas e tentações de sonegação para sobreviver.
                    </div>
                    <div class="card-item threat">
                        <h4>📉 Instabilidade Econômica</h4>
                        Inflação, oscilações de juros, carga tributária e incertezas do ambiente macroeconômico.
                    </div>
                    <div class="card-item threat">
                        <h4>💰 Cultura do Ganho Fácil</h4>
                        Apelo da sociedade ao materialismo ostensivo, pirâmides e ambição desordenada (<em>1 Tm 6:10</em>).
                    </div>
                    <div class="card-item threat">
                        <h4>📱 Mudanças Tecnológicas Rápidas</h4>
                        Risco de obsolescência caso a empresa não invista em aprendizado contínuo e inovação.
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 As ameaças externas existem para nos manter vigilantes, fundamentados e firmes nos princípios.
                </div>
            </div>
            <aside class="notes">
                Aborde a coragem de não aceitar atalhos desonestos mesmo quando o mercado pressiona.
            </aside>
        </section>

        <!-- SLIDE 9: MATRIZ SWOT CONSOLIDADA (LAYOUT 2x2 FIEL) -->
        <section data-background-image="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge">Diagnóstico Geral Integrado</span>
                <h2>Matriz SWOT do Empreendedor Cristão</h2>
                
                <table class="matrix-table">
                    <tr>
                        <td class="matrix-header" style="color: #a8f0c6;">FAVORÁVEL (Fortalezas / Reino)</td>
                        <td class="matrix-header" style="color: #fab1a0;">DESFAVORÁVEL (Vulnerabilidades / Alertas)</td>
                    </tr>
                    <tr>
                        <td class="matrix-cell s">
                            <strong style="color: #2ecc71;">FORÇAS (Interno)</strong>
                            <ul>
                                <li>Ética e honestidade inegociáveis</li>
                                <li>Liderança servidora e respeitosa</li>
                                <li>Padrão de excelência no serviço</li>
                            </ul>
                        </td>
                        <td class="matrix-cell w">
                            <strong style="color: #e74c3c;">FRAQUEZAS (Interno)</strong>
                            <ul>
                                <li>Dificuldade em delegar funções</li>
                                <li>Desequilíbrio entre trabalho e família</li>
                                <li>Decisões precipitadas por ansiedade</li>
                            </ul>
                        </td>
                    </tr>
                    <tr>
                        <td class="matrix-cell o">
                            <strong style="color: #3498db;">OPORTUNIDADES (Externo)</strong>
                            <ul>
                                <li>Busca por marcas confiáveis e éticas</li>
                                <li>Inovação de impacto social e local</li>
                                <li>Parcerias estratégicas com mesmo propósito</li>
                            </ul>
                        </td>
                        <td class="matrix-cell t">
                            <strong style="color: #e67e22;">AMEAÇAS (Externo)</strong>
                            <ul>
                                <li>Concorrência desleal e atalhos éticos</li>
                                <li>Volatilidade e instabilidade do mercado</li>
                                <li>Cultura do lucro imediato a qualquer custo</li>
                            </ul>
                        </td>
                    </tr>
                </table>

                <div class="speaker-cue">
                    💬 Esta é a visão 360° do seu negócio: enxergar forças para alavancar e fraquezas para proteger.
                </div>
            </div>
            <aside class="notes">
                Momento de síntese: mostre a harmonia visual dos quatro quadrantes operando juntos no diagnóstico.
            </aside>
        </section>

        <!-- SLIDE 10: CRUZAMENTO ESTRATÉGICO -->
        <section data-background-image="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge">Ação Tática</span>
                <h2>Cruzamento Estratégico no Empreendimento</h2>
                <div class="grid-3col">
                    <div class="card-item strength">
                        <h4>1. Forças + Oportunidades</h4>
                        <strong>Alavancagem Máxima:</strong><br>
                        Usar a ética e a excelência comprovadas como cartão de visitas para conquistar clientes exigentes que valorizam transparência e responsabilidade social.
                    </div>
                    <div class="card-item threat">
                        <h4>2. Forças + Ameaças</h4>
                        <strong>Blindagem Estratégica:</strong><br>
                        Manter o compliance e a governança rígidos como muralha contra pressões de atalhos escusos, blindando o patrimônio e o nome da empresa.
                    </div>
                    <div class="card-item opportunity">
                        <h4>3. Fraquezas + Oportunidades</h4>
                        <strong>Desenvolvimento Interno:</strong><br>
                        Profissionalizar a gestão, investir em treinamentos e delegar com eficiência para absorver as novas demandas crescentes do mercado.
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 Estratégia é decidir onde concentrar suas melhores energias para transformar ameaças em aprendizado.
                </div>
            </div>
            <aside class="notes">
                Explique que cruzar quadrantes é o grande diferencial prático da SWOT para sair da teoria para a ação.
            </aside>
        </section>

        <!-- SLIDE 11: SWOT E O CICLO PDCA -->
        <section data-background-image="https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge">Gestão Contínua</span>
                <h2>SWOT e o Ciclo PDCA: Melhoria Contínua</h2>
                <div class="grid-3col">
                    <div class="card-item" style="border-top: 3px solid var(--gold);">
                        <h4>1. PLAN (Planejar)</h4>
                        Usa o diagnóstico SWOT para traçar metas claras, consagrando os planos ao Senhor (<em>Pv 16:3</em>) e definindo indicadores (KPIs) realistas.
                    </div>
                    <div class="card-item" style="border-top: 3px solid #2ecc71;">
                        <h4>2. DO (Executar)</h4>
                        Põe em prática com padrão de excelência, liderança servidora, delegação eficiente, energia e princípios inegociáveis.
                    </div>
                    <div class="card-item" style="border-top: 3px solid #3498db;">
                        <h4>3. CHECK & ACT (Avaliar / Agir)</h4>
                        Avalia os frutos e métricas, corrige pontos fracos e ajusta rotas com sabedoria, responsabilidade e humildade.
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 O sucesso não acontece em um evento único; ele é construído no ciclo diário de planejar, agir e aprimorar.
                </div>
            </div>
            <aside class="notes">
                Relacione o ciclo PDCA com a disciplina bíblica de examinar os próprios caminhos e perseverar.
            </aside>
        </section>

        <!-- SLIDE 12: ESTÁGIOS DE MATURIDADE DO EMPREENDEDOR -->
        <section data-background-image="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge">Evolução de Carreira e Ministério</span>
                <h2>Estágios de Maturidade do Empreendedor</h2>
                
                <div class="flow-container">
                    <div class="flow-step">
                        <strong>1. Diagnóstico</strong>
                        Mapeamento transparente de Forças, Fraquezas e Alinhamento Devocional.
                    </div>
                    <div class="flow-arrow">➔</div>
                    <div class="flow-step">
                        <strong>2. Planejamento</strong>
                        Definição de metas de negócio e indicadores de impacto espiritual e social.
                    </div>
                    <div class="flow-arrow">➔</div>
                    <div class="flow-step">
                        <strong>3. Execução</strong>
                        Operação diária pautada na excelência, ética e valorização de pessoas.
                    </div>
                    <div class="flow-arrow">➔</div>
                    <div class="flow-step" style="border-color: #2ecc71;">
                        <strong style="color: #2ecc71;">4. Frutificação</strong>
                        Multiplicação de recursos, testemunho vivo no mercado e expansão do Reino.
                    </div>
                </div>

                <div class="speaker-cue">
                    💬 Em qual destes quatro estágios a sua empresa e a sua liderança se encontram hoje?
                </div>
            </div>
            <aside class="notes">
                Provoque uma autoavaliação dos líderes: a frutificação só chega para quem não pula etapas.
            </aside>
        </section>

        <!-- SLIDE 13: REFLEXÃO SOBRE PROPÓSITO -->
        <section data-background-image="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box" style="text-align: center;">
                <span class="badge">Propósito Soberano</span>
                <h2>Trabalho como Adoração e Serviço</h2>
                
                <div class="verse-box" style="font-size: 1.2em; max-width: 980px; margin: 20px auto; text-align: center; border-left: none; border-top: 3px solid var(--gold); border-bottom: 3px solid var(--gold); border-radius: 12px; padding: 22px;">
                    “Tudo o que fizerem, façam de todo o coração, como para o Senhor, e não para os homens, sabendo que receberão do Senhor a recompensa da herança. É a Cristo, o Senhor, que vocês estão servindo.”
                    <div style="font-family: 'Montserrat', sans-serif; font-size: 0.85em; color: var(--gold-light); margin-top: 10px; font-weight: 600;">
                        — Colossenses 3:23-24
                    </div>
                </div>

                <div class="speaker-cue">
                    💬 Quando seu cliente entrar na sua loja ou escritório, que ele sinta o padrão de alguém que trabalha para o Rei dos reis.
                </div>
            </div>
            <aside class="notes">
                Deixe o versículo ecoar no ambiente. O trabalho é santo e dignifica o ser humano quando feito para o Senhor.
            </aside>
        </section>

        <!-- SLIDE 14: EMPREENDENDO PARA A GLÓRIA DE DEUS -->
        <section data-background-image="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box">
                <span class="badge">Aplicação & Compartilhamento</span>
                <h2>Empreendendo para a Glória de Deus</h2>
                <p style="font-size: 0.75em; color: var(--gold-light); margin-bottom: 12px;">
                    Gostou do diagnóstico? Vamos aplicar a Análise SWOT e a Gestão Bíblica na prática do seu negócio!
                </p>
                <div class="grid-2x2">
                    <div class="card-item" style="border-left: 4px solid var(--gold);">
                        <h4>📖 Provérbios 16:3</h4>
                        “Consagra ao Senhor tudo o que você faz, e os seus planos serão bem-sucedidos.”
                    </div>
                    <div class="card-item" style="border-left: 4px solid var(--gold);">
                        <h4>📖 Provérbios 16:32</h4>
                        “Melhor é o homem paciente do que o guerreiro, e o que domina o seu espírito do que o que conquista uma cidade.”
                    </div>
                </div>
                <div class="speaker-cue">
                    💬 Abra para perguntas breves, depoimentos ou convide para o momento de reflexão e oração final.
                </div>
            </div>
            <aside class="notes">
                Prepare o coração de todos para a Oração de Convite que acontecerá no próximo slide.
            </aside>
        </section>

        <!-- SLIDE 15: ORAÇÃO DE CONVITE ADHONEP -->
        <section data-background-image="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1920&q=85">
            <div class="glass-box" style="text-align: center;">
                <span class="badge" style="background: linear-gradient(135deg, #d4af37, #96741b); color: #090d15;">Momento Especial</span>
                <h2 style="font-size: 2.2em; color: var(--gold-light); margin: 10px 0 16px 0;">Oração de Convite ADHONEP</h2>
                <div class="verse-box" style="font-size: 0.88em; line-height: 1.8; text-align: center; margin: 0 auto; max-width: 860px; background: rgba(0,0,0,0.5); border: 1px solid rgba(212,175,55,0.4); border-radius: 12px; padding: 20px;">
                    <strong>PAI,</strong><br>
                    PEÇO PERDÃO POR MEUS PECADOS,<br>
                    PURIFICA-ME COM TEU SANGUE,<br>
                    POIS HOJE ESTOU ME TORNANDO UMA NOVA PESSOA.<br>
                    <strong>ABRO MEU CORAÇÃO</strong><br>
                    PARA QUE SUA ALEGRIA, PAZ E SAÚDE REINEM EM MINHA VIDA E EM MINHA FAMÍLIA,<br>
                    NO NOME DE JESUS.<br>
                    ESCREVE MEU NOME NO LIVRO DA VIDA,<br>
                    POIS EU CREIO QUE O SENHOR É MEU ÚNICO E SUFICIENTE SALVADOR.<br>
                    <strong>AMÉM!</strong>
                </div>
                <div class="speaker-cue" style="margin-top: 16px;">
                    🙏 Convide todos a ficarem em pé e orarem juntos em voz alta.
                </div>
            </div>
            <aside class="notes">
                Momento mais nobre e transformador da reunião. Conduza com reverência, amor e convicção.
            </aside>
        </section>

        <!-- SLIDE 16: IMAGEM DE ENCERRAMENTO OFICIAL ADHONEP -->
        <section data-background-image="data:image/png;base64,{img46_b64}">
            <aside class="notes">
                Encerramento oficial. Agradeça a presença de todos e convide para o próximo encontro do Capítulo 230.
            </aside>
        </section>

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

with open("APRESENTACAO_SWOT_CRISTA.HTML", "w", encoding="utf-8") as f:
    f.write(html_content)

print("APRESENTACAO_SWOT_CRISTA.HTML gerado com sucesso!")
