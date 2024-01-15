from craftyai import CraftyAI

openai_api_key = ""

craftyai = CraftyAI(
    openai_api_key=openai_api_key,
    mc_port=xxxxx,
    resume=False,
)

craftyai.learn()