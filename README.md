# Global Solution SERS - 1CCPB - 2026.2
### Neighborhood Action Dashboard - Citizen Tech

 - Helaine Gonçalves Mota - RM 576838
 - Mariana Bello Auada - RM 575333

## 1. O problema
- **Espaço escolhido**: praça comunitária em bairro residencial, com playground infantil, área de piquenique, mesas para adultos e espaço pet.
- **Problema energético**: a iluminação é antiga e deficiente, com postes velhos, lâmpadas queimadas e demora de dias para reposição. São 15 pontos de luz com lâmpadas de vapor de sódio de alta pressão (VSAP) de 150 W, e 6 deles (40%) estão queimados, deixando áreas inteiras no escuro. Isso gera dois problemas:
  - Desperdício: as lâmpadas antigas consomem muita energia para a luz que entregam e ficam acesas a noite toda, mesmo sem ninguém na praça.
  - Subutilização: o espaço fica escuro e inseguro à noite, e a comunidade perde o uso da praça depois do trabalho e da escola.
- **Público beneficiado**: crianças (playground), adultos (mesas, caminhadas, piquenique), idosos e tutores de pets.
- **Condições de funcionamento**: uso principalmente noturno, de 18h às 6h (12 h/dia). A solução precisa funcionar de forma autônoma e confiável nesse período.
- **Benefícios esperados**: mais segurança, uso da praça por mais horas, economia de energia e de custos para a prefeitura, redução de emissões e manutenção mais simples, com monitoramento que avisa quando uma lâmpada falha.

A praça do projeto é fictícia. Hoje, com 9 pontos acesos, o consumo é menor que o necessário, mas isso não é economia: é falta de serviço. Por isso a análise compara dois cenários, hoje (9 pontos acesos) e referência (15 pontos acesos).

## 2. Solução

O projeto compara a iluminação atual com três alternativas que atendem à mesma necessidade (15 pontos, 12 h/dia):

- A: troca por LED com sensor de presença e dimerização, ligado à rede.
- B: a alternativa A com painel solar e bateria em cada poste, sem usar a rede (off-grid).
- C: a alternativa A com uma mini usina fotovoltaica conectada à rede, com compensação de créditos.

## 3. Dados utilizados e fontes

| Parâmetro             | Valor             | Justificativa                                                                                                                                                                                                                                                                                                            |
|-----------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pontos de luz         | 15                | Premissa do projeto                                                                                                                                                                                                                                                                                                      |
| Lâmpada atual         | VSAP 150W         | Padrão em iluminação pública antiga                                                                                                                                                                                                                                                                                      |
| Perda do reator       | 18W               | Corresponde ao patamar de eficiência dos reatores de baixa perda para vapor de sódio 150 W homologados no padrão Selo Procel / Inmetro, conforme fichas técnicas de fabricantes como a Demape (modelo externo 150 W com perda de 18 W) e a linha de baixo consumo da Philips citada no Guia Prático Philips Iluminação.  |
| Potência por ponto    | 168W              | 150W + 18W                                                                                                                                                                                                                                                                                                               |
| Funcionamento         | 12h/dia           | 18 às 6h                                                                                                                                                                                                                                                                                                                 |
| Mês/ano de referência | 30 dias/365 dias  | Padrão                                                                                                                                                                                                                                                                                                                   |
| Tarifa                | R$0,70/kWh        | Para clientes residenciais em baixa tensão, a Enel SP teve alta de 9,02% no reajuste de 2026, que entrou em vigor em 4 de julho de 2026. Assim utilizamos R$ 0,70/kWh como premissa do trabalho                                                                                                                          |
| Fator de emissão      | 0,0385 kg CO2/kWh | Média anual do SIN em 2023, MCTI                                                                                                                                                                                                                                                                                         |

## 4. Estimativas de consumo e cálculos

Fórmula usada: E = (P × t) / 1000 (E em kWh, P em W, t em horas).

Por ponto de luz (VSAP): E = (168 W × 12 h) / 1000 = 2,016 kWh/dia.

Cenário atual (9 pontos acesos):

- 2,016 × 9 = 18,144 kWh/dia
- 18,144 × 30 = 544,32 kWh/mês
- 18,144 × 365 = 6.622,6 kWh/ano

Cenário de referência (15 pontos acesos):

- 2,016 × 15 = 30,24 kWh/dia
- 30,24 × 30 = 907,2 kWh/mês
- 907,2 × 365 = 11.037,6 kWh/ano

| Cenário           | Cálculo                | Consumo                                          |
|-------------------|------------------------|--------------------------------------------------|
| Hoje (9 acesas)   | 9 x 168W x 12h / 1000  | 18,1 kWh/dia = 544 kWh/mês                       |
| Referência (15 acesas) | 15 x 168W x 12h / 1000 | 30,2 kWh/dia = 907 kWh/mês e 11.038 kWh/ano |                                                                                       

 **Custo e emissões** (custo = kWh × R$ 0,70; emissões = kWh/ano × 0,0385):

| Cenário                | Custo Mensal | Custo Anual | Emissões (kg CO2/ano)       |
|------------------------|--------------|-------------|-----------------------------|
| Atual (9 acesas)       | R$381,02     | R$4.635,79  | 255,0                       |
| Referência (15 acesas) | R$635,04     | R$7.726,32  | 424,9                       |

 Leitura dos resultados:

- A praça gasta 544 kWh/mês e entrega só 60% da iluminação. O problema é duplo: ineficiência e falta de serviço.
- Todas as alternativas devem iluminar os 15 pontos, para a comparação ser justa. A referência é 907,2 kWh/mês.
- As emissões são baixas (cerca de 425 kg/ano) porque a rede brasileira é majoritariamente renovável. Por isso, o principal benefício da solar aqui é financeiro e de autonomia, não o CO₂ evitado.

## 5. Comparação das alternativas

### 5.1 Base da comparação
- Necessidade energética: iluminar os 15 pontos da praça, 12 h/dia (18h às 6h).
- Período de referência: 1 ano para energia e 10 anos para custo total.
- Premissas de custo: tarifa constante de R$ 0,70/kWh, sem desconto financeiro.

### 5.2 Alternativas
| Opções                    | Descrição                                                                                                    | 
|---------------------------|--------------------------------------------------------------------------------------------------------------|
| Atual                     | Lâmpadas VSAP 150W + reator (168W/ponto), repondo as 6 lâmpadas queimadas                                    |
| Alternativa A             | LED 50W com sensor de presença e dimerização, ligado à rede                                                  |
| Alternativa B (Renovável) | Junção da alternativa A mais um painel e bateria em cada poste, sem a necessidade de rede (Sistema Off-Grid) |
| Alternativa C (Renovável) | Junção da alternativa A mais uma mini usina fotovoltaica conectada à rede, com compensação de créditos       |

Operação do LED (A, B e C): 100% de potência das 18h às 22h (4 h) e 30% das 22h às 6h (8 h), com sensor que eleva a luz quando há pessoas. Por ponto: (4 h × 50 W) + (8 h × 15 W) = 320 Wh/dia = 0,32 kWh/dia.

### 5.3 Consumo e Economia

Alternativa A: 15 pontos × 0,32 = 4,8 kWh/dia; 4,8 × 30 = 144 kWh/mês. Economia: (907,2 − 144) / 907,2 = 84,1%.

| Alternativa     | kWh/dia    | kWh/mês | kWh/ano  | Atual vs Economia |
|-----------------|------------|---------|----------|-------------------|
| Atual (15 VSAP) | 30,24      | 907,2   | 11.037,6 | -                 |
| Alternativa A   | 4,80       | 144,0   | 1.752    | 84,1%             |
| Alternativa B   | 0 da rede  | 0       | 0        | Até 100%          |
| Alternativa C   | ~0 líquido | ~0      | ~0       | Até 100%          |

### 5.4 Dimensionamento Solar
Adotou-se 4,5 kWh/m²/dia (média anual) para o sistema conectado e 4,0 para o autônomo, dimensionado para o pior mês (inverno).

Alternativa B (por poste, autônomo):

- Energia necessária no painel: 320 Wh ÷ 0,70 (perdas de controlador, bateria e cabos) = 457 Wh/dia.
- Painel: 457 ÷ 4,0 = 114 Wp, adotando 130 Wp.
- Bateria (2 dias de autonomia, descarga de 80%, lítio LiFePO₄): 320 × 2 ÷ 0,8 = 800 Wh, adotando cerca de 1 kWh.

Alternativa C (usina única):

- Rendimento: 4,5 × 0,80 (taxa de desempenho) × 365 = cerca de 1.314 kWh/kWp/ano.
- Potência necessária: 1.752 ÷ 1.314 = 1,33 kWp, adotando 3 módulos de 550 Wp = 1,65 kWp.
- Geração: 1,65 × 1.314 = cerca de 2.168 kWh/ano (folga de cerca de 24% sobre o consumo).

### 5.5 Custos estimados

| Item                                             | Valor                             |
|--------------------------------------------------|-----------------------------------|
| Luminária LED 50W                                | R$400                             |
| Controlador/Sensor/Dimerização por ponto         | R$250                             |
| Instalação por ponto(A)/(B)                      | R$250/R$400                       |
| Gateway de monitoramento (comum)                 | R$1.500                           |
| Painel 130 Wp + controlador MPPT + estrutura (B) | R$460 + 300 + 300                 |
| Bateria LiFePo₄ 1 kWh (B)                        | R$2.000                           |
| FV conectada                                     | R$5,00/Wp                         |
| Manutenção/ano por ponto                         | Atual R$100; LED R$20; Solar R$50 |
| Troca de bateria (B)                             | 1 x em 10 anos, 15 x R$2.000      |

*Obs: Estimativa de valores baseada em pesquisa de preços em lojas online, nov/2026

Investimento inicial:

- A: 15 × (400 + 250 + 250) + 1.500 = R$ 15.000
- B: 15 × (400 + 250 + 400 + 1.060 + 2.000) + 1.500 = R$ 63.150
- C: R$ 15.000 + 1.650 Wp × R$ 5,00 = R$ 23.250

### 5.6 Comparação financeira (10 anos)

Payback = investimento extra sobre a atual ÷ economia anual.

- A: R$ 14.100 ÷ R$ 7.700 = 1,8 ano.
- C: R$ 22.350 ÷ R$ 8.726 = 2,6 anos.
- B: a economia anual (cerca de R$ 8.476) pagaria o investimento extra em cerca de 7,3 anos, mas a troca das baterias no ano 10 (R$ 30.000) faz o custo total em 10 anos ficar acima do atual. Por isso, B não se paga no período.

|                              | Atual    | Alternativa A | Alternativa B                                                    | Alternativa C                                              |
|------------------------------|----------|---------------|------------------------------------------------------------------|------------------------------------------------------------|
| Investimento Inicial         | R$900    | R$15.000      | R$63.150                                                         | R$23.250                                                   |
| Energia da rede/ano          | R$7.726  | R$1.226       | R$0 (Cenário ideal, sem taxa de disponibilidade)                 | R$0 (Cenário ideal, sem taxa de disponibilidade)           |
| Manutenção/ano               | R$1.500  | R$300         | R$750                                                            | R$500                                                      |
| Custo anual da operação      | R$9.226  | R$1.526       | R$750                                                            | R$500                                                      |
| Reposição da bateria         | -        | -             | R$30.000                                                         | -                                                          |
| Custo total em 10 anos       | R$93.163 | R$30.264      | R$100.650                                                        | R$28.250                                                   |
| Economia em 10 anos vs Atual | -        | R$62.899      | -R$7.487                                                         | R$64.913                                                   |
| Payback vs Atual             | -        | 1,8 ano       | Não paga em 10 anos                                              | 2,6 anos                                                   |

### 5.7 Impactos ambientais

As emissões foram calculadas com o fator médio do SIN em 2023 (0,0385 kg CO₂/kWh), aplicado ao consumo anual de cada alternativa. A referência é o cenário com os 15 pontos acesos (11.037,6 kWh/ano), que emite 11.037,6 × 0,0385 = 424,9 kg CO₂/ano.

Na Alternativa A, o consumo de 1.752 kWh/ano gera 1.752 × 0,0385 = 67,5 kg CO₂/ano, o que evita 424,9 − 67,5 = 357,4 kg/ano (84,1% da referência). Nas Alternativas B e C, a geração solar tende a eliminar os 67,5 kg restantes, chegando a até 424,9 kg/ano evitados, como projeção condicionada às premissas adotadas.

A eficiência da Alternativa A responde por 84,1% da redução, e a geração solar pelo restante. Como a matriz elétrica brasileira já é majoritariamente renovável, o ganho da solar está mais na economia, na autonomia e na resiliência do que no CO₂ evitado.

A conta considera só as emissões da operação, sem a fabricação de painéis, baterias e luminárias. As baterias de LiFePO₄ (B) exigem logística reversa. Já a troca das lâmpadas de vapor de sódio por LED reduz o descarte de lâmpadas com pequena quantidade de mercúrio. Em C, pode haver consumo residual da rede (taxa de disponibilidade e regras da Lei 14.300).

### 5.8 Viabilidade, benefícios e limitações

Alternativa A: a viabilidade técnica é simples, pois consiste na troca das luminárias nos postes existentes. Os principais benefícios são o baixo custo, a manutenção mínima e a possibilidade de monitoramento remoto. Continua dependendo da rede elétrica convencional e não usa fonte renovável.

Alternativa B: exige painéis solares em cada poste, sem sombreamento de árvores ou outros obstáculos, além de espaço para painéis e baterias. Oferece iluminação sem conexão à rede e maior independência energética, mas tem custo muito elevado, principalmente por causa das baterias, e exige mais manutenção.

Alternativa C: necessita de uma área para instalar três painéis solares (por exemplo na área coberta/telhado do parquinho) e da conexão com a rede da concessionária. Seu principal benefício é o melhor custo-benefício, com energia renovável e possibilidade de reaproveitar a energia pela rede. Depende das regras de compensação de energia (Lei 14.300 e parcela do Fio B) e da aprovação da Enel.

## 6. Diagrama conceitual

![Diagrama conceitual da solução](diagrama.pdf)

**Fluxo de dados do diagrama**

A energia vem dos painéis fotovoltaicos (1,65 kWp), passa pelo inversor e pelo medidor bidirecional, que troca créditos de kWh com a rede da Enel, e alimenta as 15 luminárias LED de 50 W. Os sensores de presença e de luz enviam sinais ao controlador, que faz a dimerização das luminárias. O gateway IoT coleta os dados das luminárias e os envia ao processamento, que calcula kWh, R$ e CO₂. O dashboard apresenta os indicadores e dispara alertas quando um ponto de luz falha.

## 7. Indicadores energéticos e ambientais

|             Indicador             |                Fórmula               |   Unidade  |
|:---------------------------------:|:------------------------------------:|:----------:|
| Consumo de energia                | E = (P × t) / 1000                   | kWh/mês    |
| Redução de custo de energia       | kWh economizados × R$ 0,70           | R$/mês     |
| Participação de energia renovável | mín(100, geração FV / consumo × 100) | %          |
| Emissões evitadas                 | kWh/ano evitados × 0,0385            | kg CO₂/ano |
| Disponibilidade da iluminação     | pontos funcionando / 15 × 100        | %          |

Valores por alternativa:

|               Indicador              | Hoje (9 acesas) | Referência (15 acesas) |              A             |              B             |               C              |
|:------------------------------------:|:---------------:|:----------------------:|:--------------------------:|:--------------------------:|:----------------------------:|
| Consumo da instalação (kWh/mês)      | 544,3           | 907,2                  | 144,0                      | 144,0                      | 144,0 (Antes da compensação) |
| Redução de custo de energia (R$/mês) | –               | –                      | 534,24                     | Até 635,04 (Projeção)      | Até 635,04 (Projeção)        |
| Energia renovável (%)                | 0               | 0                      | 0                          | 100 (Projeção)             | 100 (Projeção)               |
| Emissões evitadas (kg CO₂/ano)       | –               | –                      | 357,4                      | até 424,9 (Projeção)       | até 424,9 (Projeção)         |
| Disponibilidade (%)                  | 60              | 100                    | ~100 (Com alerta de falha) | ~100 (Com alerta de falha) | ~100 (Com alerta de falha)   |

Cálculos:

- Consumo: 15 × 0,32 × 30 = 144,0 kWh/mês. Hoje: 9 × 2,016 × 30 = 544,3 kWh/mês.
- Redução de custo: em A, 763,2 kWh economizados × 0,70 = R$ 534,24. Em B e C, a rede deixa de cobrar os 907,2 kWh: 907,2 × 0,70 = R$ 635,04.
- Energia renovável (C): 2.168 ÷ 12 = 180,7 kWh/mês, que cobre 125% dos 144 kWh. O indicador é limitado a 100%.

## 8. Código do dashboard

O arquivo dashboard_sers.py mostra os indicadores acima, calculados a partir das premissas.

Para rodar:

```
pip install -r requirements.txt
streamlit run dashboard_sers.py
```

## 9. Limitações da proposta
- Tarifa constante e sem desconto financeiro.
- Custos estimados, sem orçamento comercial completo.
- O consumo do LED considera 100% por 4 h e 30% por 8 h, sem contar os momentos em que o sensor eleva a luz acima de 30%.
- B e C são projeções, que dependem de sombreamento, espaço, aprovação da concessionária e regras de compensação (Lei 14.300).
- Em C, pode haver consumo residual da rede (taxa de disponibilidade).
- Emissões da fabricação de painéis, baterias e luminárias não foram contabilizadas.
- O fator de emissão é uma média anual do SIN, não um valor medido para o horário de operação da praça.
- Estimativas de economia, geração renovável e redução de impactos são projeções condicionadas às premissas adotadas, não resultados garantidos.

## 10. Referências 

BRASIL. Lei nº 14.300, de 6 de janeiro de 2022. Institui o marco legal da microgeração e minigeração distribuída, o Sistema de Compensação de Energia Elétrica (SCEE) e o Programa de Energia Renovável Social (PERS); altera as Leis nºs 10.848, de 15 de março de 2004, e 9.427, de 26 de dezembro de 1996; e dá outras providências. Brasília, DF: Presidência da República, 2022. Disponível em: https://www.gov.br/mme/pt-br/acesso-a-informacao/legislacao/leis/lei-n-14-300-2022.pdf/view. Acesso em: 19 nov. 2026.

CENTRO DE REFERÊNCIA PARA ENERGIA SOLAR E EÓLICA SÉRGIO BRITO. Potencial Solar - SunData v 3.0. Rio de Janeiro: CRESESB/CEPEL, 2018. Disponível em: https://cresesb.cepel.br/index.php?section=sundata. Acesso em: 19 nov. 2026.

DEMAPE. Soluções em Iluminação LED & Transformadores. Itatiba, SP: Demape, [2026?]. Disponível em: https://demape.com.br/. Acesso em: 19 nov. 2026.

OMENA, Mateus. Contas de luz: Aneel aprova aumento médio de 10,18% nas tarifas da Enel São Paulo. Exame, 30 jun. 2026. Disponível em: https://exame.com/economia/contas-de-luz-aneel-aprova-aumento-medio-de-1018-nas-tarifas-da-enel-sao-paulo/. Acesso em: 19 nov. 2026.

PHILIPS ILUMINAÇÃO. Guia Prático Philips Iluminação: lâmpadas, reatores, luminárias e LEDs. São Paulo: Philips, 2009. 131 p. Disponível em: https://api.aecweb.com.br/cls/catalogos/supplyeletrica/GuiaBolso_Sistema_09_final_led.pdf. Acesso em: 19 nov. 2026.

RAKHOLIYA, Keyur. Energia Solar em São Paulo: regulamentação, ICMS e distribuidoras. SurgePV, 24 maio 2026. Disponível em: https://www.surgepv.com/pt/solar-compliance/brazil/estado/sao-paulo. Acesso em: 19 nov. 2026.

REIS, Gabriela Bowen Tonelli. Planejamento energético integrado em uma rede de academia de ginástica por meio de cenários energéticos. 2026. 70 f. Monografia (Graduação em Engenharia de Produção) – Escola de Minas, Universidade Federal de Ouro Preto, Ouro Preto, 2026. Disponível em: https://monografias.ufop.br/bitstream/35400000/9679/5/MONOGRAFIA_PlanejamentoEnerg%C3%A9ticoIntegrado.pdf. Acesso em: 19 nov. 2026.

RUDDY, Gabriela. Brasil tem menor taxa de emissão de carbono na geração elétrica em onze anos. Eixos, 16 fev. 2024. Disponível em: https://eixos.com.br/energia-eletrica/brasil-tem-menor-taxa-de-emissao-de-carbono-na-geracao-eletrica-em-onze-anos/. Acesso em: 19 nov. 2026.

SIGNIFY HOLDING. Philips SON-T 150W E E40 1SL. Signify, [2026]. Disponível em: https://www.signify.com/global/prof/conventional-lamps-and-tubes/high-intensity-discharge-lamps/son-high-pressure-sodium/philips-son-t/928487100097_EU/product. Acesso em: 19 nov. 2026.
