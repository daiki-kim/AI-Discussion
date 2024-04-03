from openai import OpenAI


client = OpenAI()

TALK_CNT = 6


class AI:
    def __init__(self):
        self.model = "gpt-4-0125-preview"

    def say_on(self, theme):
        completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "あなたはユーザーが出したお題についての考えを述べるものです。"},
                {"role": "user", "content": f"「{theme}」というテーマについてあなたのアイデアを200文字以内で答えてください。"}
            ]
        )
        # chatGPTの回答
        return completion.choices[0].message.content

    def say_against(self, opinion):
        completion = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system",
                 "content": "あなたはユーザーのアイデアに対して新たなのブレインストーミングを行います。"},
                {"role": "user",
                 "content": f"{opinion}。以上が私のアイデアです。内容をより発展させて200文字以内で意見を述べてください。"}
            ]
        )
        # chatGPTの回答
        return completion.choices[0].message.content


def discussion(max_cnt, theme):
    ai_speakers = [AI(), AI()]
    cnt = 0
    answer = None

    while cnt < max_cnt:
        if cnt == 0:
            speaker = ai_speakers[0]
            answer = speaker.say_on(theme)
        else:
            speaker = ai_speakers[cnt % 2]
            answer = speaker.say_against(answer)
        print(f"AI{cnt % 2 + 1}:\n{answer}")
        cnt += 1
    print("Finish.")


if __name__ == "__main__":
    input_theme = input("AI同士で話合わせたいテーマを入力してください(例：「AIとプログラミングを使った近未来のビジネス」)：\n")
    discussion(TALK_CNT, input_theme)
