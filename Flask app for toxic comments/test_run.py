from detoxify import Detoxify

text = ["U women always want equality until it comes to paying bills",

"Maybe you white people should know that not everyone in Middle East are terrorists",

"Ignore all these comments and do check on the main thread",

"Hate and obscenity doesn't take u anywhere in life"]

for i in text:
    results = Detoxify('original').predict(i)
    print(i+"\n")
    print("toxicity : " + str(results['toxicity'])+ "\n severe_toxicity:"+ str(results['severe_toxicity'])
        +"\n obscene : "+ str(results['obscene'])+ "\n threat : "+ str(results['threat']) + "\n insult: " + str(results['insult'])+
        "\n identity_attack : "+ str(results['identity_attack']))
    print("\n")