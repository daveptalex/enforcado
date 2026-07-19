# Setup TWA - Enforcado 3D (Google Play Store)

## Passo 1: Hospedar no GitHub Pages

1. Criar um repositório no GitHub chamado `enforcado` (ou similar)
2. Fazer push de todos os ficheiros da pasta `enforcado/` para esse repositório
3. Ir a Settings > Pages > Branch: `main` > Save
4. O site estará disponível em: `https://daveptalex.github.io/enforcado/`

## Passo 2: Criar o assetlinks.json (para TWA funcionar)

O `assetlinks.json` deve estar no domínio hosting no caminho:
`https://daveptalex.github.io/.well-known/assetlinks.json`

**ATENÇÃO:** GitHub Pages não suporta `.well-known` diretamente.
Alternativa: usar um subdomínio próprio (ex: `enforcado.seudominio.com`) ou usar Netlify.

Para GitHub Pages, a solução mais fácil é usar **PWABuilder** que gera o APK/TWA automaticamente.

## Passo 3 (MÉTODO RECOMENDADO): Usar PWABuilder

1. Abrir https://www.pwabuilder.com/
2. Inserir o URL: `https://daveptalex.github.io/enforcado/`
3. O PWABuilder vai analisar e verificar os requisitos
4. Clicar em "Package for stores"
5. Selecionar "Google Play Store"
6. Seguir as instruções para gerar o APK/AAB
7. Transferir o ficheiro .aab gerado

## Passo 4: Publicar na Google Play Store

1. Criar conta de desenvolvedor no Google Play Console ($25 taxa única)
2. Criar nova aplicação
3. Fazer upload do .aab gerado pelo PWABuilder
4. Preencher descrição, capturas de ecrã, etc.
5. Submeter para revisão

## Estrutura de Ficheiros

```
enforcado/
├── index.html          # Jogo principal
├── palavras.txt        # Lista de palavras
├── manifest.json       # PWA Manifest
├── sw.js              # Service Worker (offline)
├── icons/             # Ícones para PWA/TWA
│   ├── icon-72x72.png
│   ├── icon-96x96.png
│   ├── icon-128x128.png
│   ├── icon-144x144.png
│   ├── icon-152x152.png
│   ├── icon-192x192.png
│   ├── icon-384x384.png
│   └── icon-512x512.png
├── generate_icons.py   # Script para gerar ícones
├── twa-manifest.json   # Configuração Bubblewrap (opcional)
└── TWA_SETUP.md        # Este ficheiro
```

## Alternativa: Usar Bubblewrap (Terminal)

```bash
# Instalar Node.js e Bubblewrap
npm install -g @nicepkg/bubblewrap

# Criar projeto Android
bubblewrap init --manifest=https://daveptalex.github.io/enforcado/manifest.json

# Gerar APK
bubblewrap build

# O APK estará na pasta ./app-release-signed.apk
```

## Verificar PWA

Depois de hospedar, testar se a PWA funciona:
1. Abrir o URL no Chrome mobile
2. Verificar se aparece "Adicionar ao ecrã principal"
3. Testar funcionalidade offline
