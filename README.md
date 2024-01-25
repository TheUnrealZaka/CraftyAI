# CraftyAI, un agente inteligente para Minecraft 
Presentamos a CraftyAI, un agente inteligente en Minecraft impulsado por LLM (Large Language Models) que explora continuamente el mundo, adquiere diversas habilidades y realiza nuevos descubrimientos sin intervención humana. En este repositorio, proporcionamos el código de CraftyAI.

# Instalación
CraftyAI requiere [Python](https://www.python.org/downloads/release/python-3109/) ≥ 3.9 y [Node.js](https://nodejs.org/en) ≥ 16.13.0. Necesitas seguir las siguientes instrucciones para instalar CraftyAI.

```sh
git clone https://github.com/TheUnrealZaka/CraftyAI
cd CraftyAI
pip install -e .
```

Además de las dependencias de Python, necesitas instalar los siguientes paquetes de Node.js:

```sh
cd craftyai/env/mineflayer
npm install -g npx
npm install
cd mineflayer-collectblock
npm install
npx tsc
cd ..
npm install
```

También necesitas instalar los siguientes paquetes de las APIs de GPT4Free:

```sh
cd api
pip install -e .
```

## Instalación de la instancia de Minecraft

CraftyAI depende del juego Minecraft. Es necesario instalar el juego [Minecraft](https://www.minecraft.net/) y configurar una instancia de Minecraft.

### Instalación de mods
En este tutorial, instalaremos el lanzador Fabric y 5 mods. Recuerda usar la versión correcta de Fabric que coincida con la versión de tu juego (1.19) de todos los mods. 
1. Puedes descargar el último instalador de Fabric desde [aquí](https://fabricmc.net/use/installer/). Para usuarios de Windows, sólo tienes que descargar el archivo `.exe`. Para usuarios de Linux o Mac, descarga el archivo jar y ejecuta `java -jar fabric-installer-0.11.2.jar` para instalar. Selecciona que la versión del juego sea `1.19` y la del cargador `0.14.18`. Detectará automáticamente la ubicación de instalación de tu juego Minecraft.
2. Después de instalar Fabric, tendrás una carpeta `%appdata%/.minecraft/mods`(en Windows). Necesitas poner todos los mods en esta carpeta. También tendrás una carpeta `%appdata%/.minecraft/versions/fabric-loader-0.14.18-1.19`. Esta es la versión con la que ejecutarás el juego. 
3. En ese repositorio, te dejamos los mods necesarios en la carpeta mods aunque también tienes la opción de descargar directamente en la carpeta `%appdata%/.minecraft/mods`: 
   * [Fabric API](https://modrinth.com/mod/fabric-api/version/0.58.0+1.19): APIs básicas de Fabric.
   * [Mod Menu](https://cdn.modrinth.com/data/mOgUt4GM/versions/4.0.4/modmenu-4.0.4.jar): Sirve para gestionar todos los mods que te descargues.
   * [Complete Config](https://www.curseforge.com/minecraft/mc-mods/completeconfig/download/3821056): Dependencia de la pausa del servidor.
   * [Multi Server Pause](https://www.curseforge.com/minecraft/mc-mods/multiplayer-server-pause-fabric/download/3822586): Utilizado para pausar el servidor cuando se espera la respuesta de GPT-4.
4. Para el último mod [Better Respawn](https://github.com/xieleo5/better-respawn/tree/1.19), necesitas clonar y compilar manualmente. Por eso, se recomienda usar la que tenemos compilada.

### Instalación de la instancia
Después de instalar Minecraft oficial, usted debe tener un lanzador oficial de Minecraft, abrirlo, y siga las instrucciones aquí:
1. Selecciona la versión a la que quieres jugar e inicia el juego.
2. Selecciona `Singleplayer` y crea un nuevo mundo.
3. Configura el modo de juego en `Creativo` y la dificultad en `Pacifico`.
4. Una vez creado el mundo, pulsa `Esc` y selecciona `Open to LAN`.
5. Selecciona `Allow cheats: ON` y pulsa `Start LAN World`.
6. Verás un número de puerto en el chat del juego, ese es tu `mc-port`, usa este número para ponerlo en el fichero `main.py` en el apartado `mc_port=xxxxx,`

# Primeros pasos

CraftyAI utiliza GPT4Free, que se encuentra en la carpeta `api/`. También puedes usar GPT-4 de OpenAI como modelo de lenguaje aunque necesitas tener una clave API de OpenAI para usar CraftyAI, que es de pago. Puedes obtenerla [aquí](https://platform.openai.com/account/api-keys).

En nuestro caso, se necesita la API de HuggingFace para poder usar GPT4Free. Puedes obtenerla [aquí](https://huggingface.co/settings/tokens)

Una vez que tienes el token, puedes ponerlo en el fichero `main.py` en el apartado `openai_api_key = ""`.

Después del proceso de instalación, puedes abrir 2 terminales y poner 2 comandos para cada terminal para ejecutar CraftyAI:

```sh
g4f api
```
```sh
python3 main.py
```

# Reanudar desde un punto de control durante el aprendizaje

Si detienes el proceso de aprendizaje y quieres reanudarlo desde un punto de control más tarde, puedes iniciar CraftyAI modificando `main.py` con lo siguiente:
```python
from craftyAI import CraftyAI

craftyai = CraftyAI(
    openai_api_key=openai_api_key,
    ckpt_dir="ckpt/",
    resume=True,
)
```

# FAQ
Si tiene alguna duda, consulte primero [FAQ](FAQ.md) antes de abrir una incidencia.