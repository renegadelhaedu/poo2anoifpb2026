from fpdf import FPDF

nome = input('Qual o seu nome? ')
paixao = input('Qual o sua paixao? ')


# 1. Inicializar o documento (P = Retrato, mm = milímetros, A4 = tamanho do papel)
pdf = FPDF(orientation='P', unit='mm', format='A4')

# 2. Adicionar a primeira página
pdf.add_page()

# 3. Configurar a fonte (Família, Estilo, Tamanho em pontos)
pdf.set_font("Arial", style='B', size=16)

# 4. Criar uma célula de texto (Largura, Altura, Texto, Borda, Quebra de linha, Alinhamento)
# ln=1 significa que o próximo elemento vai para a linha de baixo
pdf.cell(w=190, h=10, txt="Minha primeira e única paixão", border=0, ln=1, align='C')

# Espaçamento manual de 10mm
pdf.ln(10)

# Mudar a fonte para o corpo do texto
pdf.set_font("Arial", size=12)

# Adicionar parágrafos simples
pdf.cell(w=0, h=8, txt='Meu nome é ' + nome, ln=1)
pdf.cell(w=0, h=8, txt='Essa é minha paixão' + paixao, ln=2)

# 5. Salvar o arquivo no computador
pdf.output(nome+ ".pdf")
