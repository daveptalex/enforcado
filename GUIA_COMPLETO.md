# Guia Completo: Enforcado 3D -> Google Play Store

## PARTE 1: Configurar Git e GitHub

### 1.1 Configurar o teu utilizador Git (se ainda não tiveres)
```bash
git config --global user.name "daveptalex"
git config --global user.email "O_TEU_EMAIL@gmail.com"
```

### 1.2 Fazer login no GitHub via terminal
```bash
gh auth login
```
- Selecionar: **GitHub.com**
- Selecionar: **HTTPS**
- Selecionar: **Login with a web browser**
- Copiar o código que aparecer e abri-lo no browser
- Autorizar o GitHub CLI

---

## PARTE 2: Criar Repositório e Fazer Push

### 2.1 Criar o repositório no GitHub
```bash
cd ~/IA/enforcado
gh repo create enforcado --public --source=. --push
```
Isto cria o repositório E faz push de todos os ficheiros automaticamente.

Se der erro porque o repositório já existe, faz manualmente:
```bash
cd ~/IA/enforcado
git init
git add .
git commit -m "Enforcado 3D - Jogo do Enforcado com gráficos 3D"
git remote add origin https://github.com/daveptalex/enforcado.git
git branch -M main
git push -u origin main
```

### 2.2 Verificar que o repositório foi criado
Abre no browser:
```
https://github.com/daveptalex/enforcado
```

---

## PARTE 3: Ativar GitHub Pages

### 3.1 Ativar via terminal (com gh)
```bash
gh api repos/daveptalex/enforcado/pages -X PUT -f build_type=legacy -f source='{"branch":"main","path":"/"}'
```

### 3.2 OU ativar manualmente no browser
1. Ir a `https://github.com/daveptalex/enforcado`
2. Clicar em **Settings** (tab)
3. No menu lateral, clicar em **Pages**
4. Em **Source**, selecionar **Deploy from a branch**
5. Em **Branch**, selecionar **main** e pasta **/ (root)**
6. Clicar em **Save**

### 3.3 Testar o site
Esperar ~1-2 minutos e depois abrir:
```
https://daveptalex.github.io/enforcado/
```
O jogo deve carregar normalmente.

---

## PARTE 4: Gerar a App Android (TWA)

### 4.1 Instalar Bubblewrap (gerador de TWA)
```bash
npm install -g @nicepkg/bubblewrap
```

### 4.2 Criar o projeto Android
```bash
cd ~/IA/enforcado
bubblewrap init --manifest=https://daveptalex.github.io/enforcado/manifest.json
```

Durante o `init`, responde às perguntas:
- **Package ID**: `com.enforcado3d.game`
- **App name**: `Enforcado 3D`
- **Theme color**: `#0a0612`
- **Background color**: `#0a0612`
- **Use a different signing key?**: Yes (para teres controlo da chave)
- **Key password**: Define uma password segura
- **Key alias**: `enforcado3d`
- **Validity (years)**: 25

### 4.3 Gerar o APK/AAB
```bash
bubblewrap build
```

Isto vai gerar:
- `app-release-signed.apk` - para instalar diretamente
- `app-release-bundle.aab` - para submeter à Play Store

---

## PARTE 5: Publicar na Google Play Store

### 5.1 Criar conta de desenvolvedor
1. Ir a `https://play.google.com/console`
2. Fazer login com a tua conta Google
3. Pagar a taxa de registo: **$25** (pagamento único)
4. Preencher os dados da conta de programador

### 5.2 Criar a aplicação
1. No Play Console, clicar em **Criar aplicação**
2. **Nome**: `Enforcado 3D`
3. **Idioma padrão**: Português
4. **Gratuito ou pago**: Gratuito
5. Clicar em **Criar**

### 5.3 Preencher a ficha da aplicação
Na secção **Produção**:

**Configurações básicas:**
- Título: `Enforcado 3D`
- Descrição curta: `Jogo do Enforcado com gráficos 3D interativos`
- Descrição completa: `Enforcado 3D é um jogo clássico do enforcado completamente renovado com gráficos 3D interativos em Three.js. Adivinha a palavra antes de seres enforcado! Funciona offline e é totalmente gratuito.`

**Ícone da aplicação:**
- Usar o ficheiro `icons/icon-512x512.png`

**Capturas de ecrã:**
- Tirar capturas do jogo a funcionar no telemóvel
- Mínimo: 2 capturas
- Formato: JPG ou PNG, 16:9 ou 9:16

**Classificação por conteúdo:**
- Classificar o jogo (provavelmente "Todos")

### 5.4 Submeter o .aab
1. Na secção **Produção**, clicar em **Criar nova versão**
2. Em **App bundles**, clicar em **Enviar**
3. Selecionar o ficheiro `app-release-bundle.aab`
4. Preencher a **nota de versão**: `Versão inicial - Jogo do Enforcado 3D`
5. Clicar em **Revisar**

### 5.5 Submeter para revisão
1. Verificar que tudo está correto
2. Clicar em **Enviar para revisão**
3. A Google demora normalmente **1-3 dias** para aprovar

---

## Resumo dos Comandos (Copy-Paste)

```bash
# 1. Configurar git
git config --global user.name "daveptalex"
git config --global user.email "email@gmail.com"

# 2. Login no GitHub
gh auth login

# 3. Criar repositório e fazer push
cd ~/IA/enforcado
gh repo create enforcado --public --source=. --push

# 4. Ativar GitHub Pages
gh api repos/daveptalex/enforcado/pages -X PUT -f build_type=legacy -f source='{"branch":"main","path":"/"}'

# 5. Instalar Bubblewrap
npm install -g @nicepkg/bubblewrap

# 6. Criar projeto Android
bubblewrap init --manifest=https://daveptalex.github.io/enforcado/manifest.json

# 7. Gerar APK/AAB
bubblewrap build
```

---

## URLs Importantes

- **Repositório**: `https://github.com/daveptalex/enforcado`
- **GitHub Pages**: `https://daveptalex.github.io/enforcado/`
- **Manifest PWA**: `https://daveptalex.github.io/enforcado/manifest.json`
- **Play Console**: `https://play.google.com/console`
- **PWABuilder** (alternativa): `https://www.pwabuilder.com/`
