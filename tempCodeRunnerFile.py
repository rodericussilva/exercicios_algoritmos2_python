prog_saude = {
    'regiao': ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    'programa': ["Vacinação", "Atendimento Primário", "Saúde da Mulher", "Controle de Epidemias"],
    'beneficiarios': [1200000, 950000, 800000, 1500000, 1300000],
    'investimento': [300, 250, 200, 350, 320]  # Valores em  milhões de reais
}
incremento_pop = {"Norte": 20000,  "Sudeste": 10000, "Sul": 90000 }
for regiao, beneficiario in zip(prog_saude['regiao'], prog_saude['beneficiarios']):
    if regiao == 'Norte':
        atual1 = beneficiario + incremento_pop["Norte"]
        #valor = prog_saude['regiao'].index('Norte')
        prog_saude['beneficiarios'][prog_saude['regiao'].index('Norte')] = atual1
    if regiao == 'Sudeste':
        atual2 = beneficiario + incremento_pop['Sudeste']
        valor2 = prog_saude['regiao'].index('Sudeste')
        prog_saude['beneficiarios'][valor2] = atual2
    if regiao == 'Sul':
        atual3 = beneficiario + incremento_pop['Sul']
        valor3 = prog_saude['regiao'].index('Sul')
        prog_saude['beneficiarios'][valor3] = atual3
print(prog_saude)