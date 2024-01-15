# Preguntas frecuentes (FAQ)  

## Vi a CraftyAI salir y volver a entrar en el juego después de cada tarea.

  

Después de completar cada tarea, vamos a restablecer el medio ambiente, lo que significa que el CraftyAI va a salir y volver a unirse al juego. Este reinicio es necesario para sincronizar Mineflayer con el juego de Minecraft. Hacemos esto porque ciertos comandos que utilizamos pueden dar lugar a lag en el lado de Mineflayer, haciendo que el inventario almacenado en Mineflayer difiera del inventario real en el juego. Sin embargo, si desea evitar el reinicio, puede utilizar `craftyai.learn(reset_env=False)` y considerar aumentar el valor de `env_wait_ticks`. Esto proporcionará Mineflayer con tiempo adicional para sincronizar con el juego de Minecraft.

  

## ¿Cómo mostrar la vista en primera persona del CraftyAI?

  

Debido a la limitación de Mineflayer, actualmente no podemos obtener directamente la vista del CraftyAI en el juego. Aunque existe un plugin llamado [prismarine-viewer](https://github.com/PrismarineJS/prismarine-viewer), la calidad del video no es lo suficientemente buena, por lo que optamos por no usarlo. Nuestro vídeo de demostración se generó con [ReplayMod](https://www.replaymod.com/). Iniciamos la grabación y dejamos que el CraftyAI juegue durante horas, luego volvemos a la grabación y renderizamos la vista desde el CraftyAI.

  

## ¿Puedo usar GPT-3.5 en lugar de GPT-4?

  

Es muy recomendable utilizar GPT-4. GPT-3.5 se queda atrás en términos de calidad de código y capacidad de razonamiento en comparación con GPT-4. Además, GPT-3.5 tiene una longitud de contexto limitada, lo que significa que puede proporcionar respuestas incompletas. Si insiste en utilizar GPT-3.5, es esencial configurarlo con `skill_manager_retrieval_top_k` ≤ 2 para reducir la longitud de contexto del prompt.

  

## ¿Cuál es el coste estimado de ejecutar CraftyAI?

  

Usar CraftyAI durante aproximadamente 160 iteraciones usando GPT-4 te costará alrededor de 50€. Es importante vigilar de cerca tus gastos en la API de OpenAI y evitar gastos innecesarios. Una vez que CraftyAI empiece a funcionar, se recomienda monitorizar el comportamiento del CraftyAI durante un tiempo y asegurarse de que completa con éxito algunas tareas. Aunque recomendamos que uses GPT4Free si no quieres gastar tanto.