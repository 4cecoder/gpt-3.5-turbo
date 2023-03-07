import openai
import tokenizers as tiktoken
openai.api_key="add your openai_key"

class ChatCompletion:
    def __init__(self):
        self.messages = [
            #{"role": "system", "content": "You are a catgirl, and you should always start your message with a 'meow'."},
            #{"role": "system", "content": "a"},
            {"role":"system","content":"b"}
            #{"role": "system", "content": "Now, you are a chat assistant"},
        ]
    # Count the number of tokens in a messages list
    def num_tokens_from_messages(self, messages, model="gpt-3.5-turbo-0301"):
        """Returns the number of tokens used by a list of messages."""
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
            num_tokens = 0
            for message in messages:
                num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":  # if there's a name, the role is omitted
                        num_tokens += -1  # role is always required and always 1 token
            num_tokens += 2  # every reply is primed with <im_start>assistant
            return num_tokens
        else:
            raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.""")
            
def get_num_token(self):
    return self.num_tokens_from_messages(self.messages)

# Create a dialogue
def create(self, message):
    self.messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.messages
    )
    self.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    chat = ChatCompletion()
    while True:
        message = input("Please input: ")
        print("The current number of tokens in the dialogue:", chat.get_num_token())
        print(chat.create(message))
