import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# OpenELM's model isn't working
MODEL_ID = "meta-llama/Llama-3.2-1B"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, trust_remote_code=True)

class Player:
    def __init__(self, name, model, tokenizer):
        self.name = name
        self.model = model
        self.tokenizer = tokenizer

    def _generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt", padding=True)
        outputs = self.model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            num_return_sequences=1,
            pad_token_id=self.tokenizer.eos_token_id
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def generate_message(self, history):
        prompt = f"""You are {self.name}. 
            The following is a conversation with another player to decide on an activity ('F' or 'S').
            You want to maximize your points.
            - If you both choose 'F', you get 8 points and the other gets 5. 
            - If you both choose 'S', you get 5 points and the other gets 8. 
            - If you disagree, you both get 0.
            Conversation history:
            {history}
            What is your next message?
            {self.name}:"""
        message = self._generate_response(prompt)
        return message

    def choose_activity(self, history):
        prompt = f"""You are {self.name}. 
            Based on the following conversation, you must choose either 'F' or 'S'.
            Conversation history:
            {history}
            Give your final choice; return only either 'F' or 'S':"""
        response = self._generate_response(prompt)
        return response

def play_round(player_a, player_b, rounds=2):
    history = []
    for i in range(rounds):
        print(f"--- Round {i+1} ---")
        # Player A's turn
        msg_a = player_a.generate_message("\n".join(history))
        history.append(f"{player_a.name}: {msg_a}")
        print(f"{player_a.name}: {msg_a}")

        # Player B's turn
        msg_b = player_b.generate_message("\n".join(history))
        history.append(f"{player_b.name}: {msg_b}")
        print(f"{player_b.name}: {msg_b}")

    conversation = "\n".join(history)
    choice_a = player_a.choose_activity(conversation)
    choice_b = player_b.choose_activity(conversation)
    
    return choice_a, choice_b

if __name__ == "__main__":
    player_A = Player("Player A", model, tokenizer)
    player_B = Player("Player B", model, tokenizer)

    choice_a, choice_b = play_round(player_A, player_B)
    print(f"Final Choices: {player_A.name}-- {choice_a}, {player_B.name}-- {choice_b}")
