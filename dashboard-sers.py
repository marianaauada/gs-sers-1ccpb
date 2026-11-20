# Neighborhood Action Dashboard - SERS (Global Solution 2026.2)
# Iluminação da praça: comparação entre Atual, A, B e C

import streamlit as st
import pandas as pd
 
st.title("Dashboard de Iluminação da Praça")
st.write("Helaine G. Mota (RM 576838) e Mariana B. Auada (RM 575333)")
 
# Premissas
tarifa = st.number_input("Tarifa (R$/kWh)", value=0.70) 
fator_emissao = 0.0385   
pontos = 15
horas = 12
 
#  Consumo atual (E = P x t / 1000) 
potencia_vsap = 168  # 150 W da lâmpada + 18 W do reator
consumo_hoje = 9 * potencia_vsap * horas / 1000 * 30   
consumo_ref = pontos * potencia_vsap * horas / 1000 * 30  
 
# Consumo com led (100% por 4h e 30% por 8h) 
wh_led_por_ponto = 4 * 50 + 8 * 15         
consumo_led = pontos * wh_led_por_ponto / 1000 * 30      
 
# Indicadores
economia_kwh = consumo_ref - consumo_led
economia_pct = economia_kwh / consumo_ref * 100
economia_reais = economia_kwh * tarifa
emissao_ref = consumo_ref * 12 * fator_emissao            
emissao_led = consumo_led * 12 * fator_emissao
emissao_evitada = emissao_ref - emissao_led
 
# Apresentação tela
st.header("Indicadores da Alternativa A (LED)")
col1, col2, col3 = st.columns(3)
col1.metric("Consumo (kWh/mês)", round(consumo_led, 1))
col2.metric("Economia de energia", str(round(economia_pct, 1)) + "%")
col3.metric("Redução de custo (R$/mês)", round(economia_reais, 2))
 
st.header("Comparação de consumo (kWh/mês)")
dados = pd.DataFrame(
    {"kWh/mês": [consumo_hoje, consumo_ref, consumo_led]},
    index=["Hoje (9 acesas)", "Referência (15 acesas)", "Alternativa A"],
)
st.bar_chart(dados)
 
st.header("Comparação financeira (10 anos)")
# Total = investimento + 10 x (energia + manutenção) + bateria
total_atual = 900 + 10 * (consumo_ref * 12 * tarifa + 1500)
total_a = 15000 + 10 * (consumo_led * 12 * tarifa + 300)
total_b = 63150 + 10 * 750 + 30000
total_c = 23250 + 10 * 500
 
tabela = pd.DataFrame({
    "Alternativa": ["Atual", "A", "B", "C"],
    "Custo total em 10 anos (R$)": [total_atual, total_a, total_b, total_c],
})
st.table(tabela)
st.caption("B e C: energia da rede = R$ 0 (cenário ideal, projeção).")
 
st.header("Emissões de CO₂")
st.write("Emissões da referência:", round(emissao_ref, 1), "kg CO₂/ano")
st.write("Emissões evitadas pela Alternativa A:", round(emissao_evitada, 1), "kg CO₂/ano")
st.write("Em B e C, as emissões evitadas podem chegar a", round(emissao_ref, 1),
         "kg CO₂/ano (projeção).")
 
st.header("Energia renovável (Alternativa C)")
geracao_mes = 1.65 * 1314 / 12   # 1,65 kWp x 1.314 kWh/kWp/ano
renovavel = min(100, geracao_mes / consumo_led * 100)
st.write("Geração solar:", round(geracao_mes, 1), "kWh/mês")
st.write("Participação de energia renovável:", round(renovavel), "% (limitado a 100%)")
 
st.header("Monitoramento dos pontos de luz")
funcionando = st.slider("Pontos funcionando", 0, 15, 9)
disponibilidade = funcionando / 15 * 100
st.write("Disponibilidade da iluminação:", round(disponibilidade), "%")
if funcionando < 15:
    st.error("ALERTA: " + str(15 - funcionando) + " ponto(s) de luz com falha!")
else:
    st.success("Todos os pontos estão funcionando.")
 
