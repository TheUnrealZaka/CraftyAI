# CraftyAI, un agente inteligente para Minecraft 
Presentamos a CraftyAI, un agente inteligente en Minecraft impulsado por LLM (Large Language Models) que explora continuamente el mundo, adquiere diversas habilidades y realiza nuevos descubrimientos sin intervención humana. En este repositorio, proporcionamos el código de CraftyAI.

# 🛠️ Instalación
CraftyAI requiere [Python](https://www.python.org/downloads/release/python-3109/) ≥ 3.9 y [Node.js](https://nodejs.org/en) ≥ 16.13.0. Necesitas seguir las siguientes instrucciones para instalar CraftyAI.

```
git clone https://github.com/TheUnrealZaka/CraftyAI
cd CraftyAI
pip install -e .
```

Además de las dependencias de Python, necesitas instalar los siguientes paquetes de Node.js:

```
cd craftyai/env/mineflayer
npm install -g npx
npm install
cd mineflayer-collectblock
npx tsc
cd ..
npm install
```

También necesitas instalar los siguientes paquetes de las APIs de GPT4Free:

```
cd api
pip install -e .
```

## Instalación de la instancia de Minecraft

CraftyAI depende del juego Minecraft. Es necesario instalar el juego [Minecraft](https://www.minecraft.net/) y configurar una instancia de Minecraft.

