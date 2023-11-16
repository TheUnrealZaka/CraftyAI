from craftyai import CraftyAI

openai_api_key = ""

craftyai = CraftyAI(
    openai_api_key=openai_api_key,
    mc_port=58607,
    resume=True,
)

craftyai.learn()