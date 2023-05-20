import openai
import time

openai.api_key = "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"

covered = []

map = {0: 1, 1: 2, 2: 1, 3: 2}

while True:
    try:
        current_str = ""
        for i in range(4):
            if i == 0:
                current_str += "Aha Questions for Luke" + "\n"
                current_str += "="*100 + "\n"
            elif i == 2:
                current_str += "Aha Questions for Russell" + "\n"
                current_str += "=" * 100 + "\n"
            while True:
                ### part 1 ###
                subject = "금융 혹은 주식"
                query = f"{subject} 관련 용어 1개를 설명없이 생성해."

                response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages = [
                        {"role": "user", "content": query}
                    ]
                )

                topic_chatgpt_response = response["choices"][0]["message"]["content"]
                if topic_chatgpt_response not in covered:
                    covered.append(topic_chatgpt_response)
                    break
                else:
                    time.sleep(1)
                    print("generating a new topic")
            ### part 2 ###
            subject = f"금융 분야에서 {topic_chatgpt_response}"

            query = f"{subject}와 관련된 (1) 16글자 이상의 질문 (2) 55글자 이상의 질문의 확장판을 인간이 물어본것처럼 작성해."

            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {"role": "user", "content": query}
                ]
            )
            current_str += "Question " + str(map[i]) + "\n"
            chatgpt_response = response["choices"][0]["message"]["content"]
            current_str += chatgpt_response + "\n"
            time.sleep(5)
    except Exception as e:
        print(e)

    print(current_str)
    print("waiting for a day")
    time.sleep(60*60*24)
