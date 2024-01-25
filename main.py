from craftyai import CraftyAI

openai_api_key = ""

craftyai = CraftyAI(
    openai_api_key=openai_api_key,
    mc_port=00000,
    resume=False,
)

craftyai.learn(reset_env=False)