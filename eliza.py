

"""A)Name:Sairaj Amberkar

B)The program was completely implemented by contributions exclusively from me without
   referring to any source beyond the ones taught or referred to in class.

C)The program runs without any error and provides the output as required in the assignment.

D)Problem statement: To create Eliza chatbot implementing word spotting and sentence transformation
  using regular expressions.


   1)Word spotting: Crave, Father

   2)Sentence transformation: I need, I would, I want, What related questions

   3)Examples:

        Eliza: Hi there, What's your name?
        User: My name is Ajinkya
        Eliza: Hi Ajinkya, how can I help you today?
        User: I want to become an actor?
        Eliza: Ajinkya, Why do you want to be an actor?
        User: Because I crave fame
        Eliza: Ajinkya, Why don't you tell me more about your cravings?
        User: I need your help with my acting career
        Eliza: Ajinkya, Are you sure you need my help with your acting career?


   4)Program:
     a)A dictionary is created consisting of various replies associated with each keyword and
       eliza will identify keywords using regular expressions and accordingly the part of the program will be executed.

     b)Also, another dictionary is created consisting of translation words.For, eg, Your: my

   5)Algorithm:
     a)First using input function, Eliza requests for the name.
     b)If keywords: Bye, Exit, Quit are not given as the input then the program moves forward.
     c)Now the program searches for phrases/words like I need; I would, I want, crave, father,'?'
     d)Once Eliza receives any of the above-mentioned phrase or words, it will randomly choose the replies from the dictionary for that particular key.

   5)Additional functionality:
       a) Random responses are stored in the dictionary
       b) For any question, sentence not in the dictionary/Gibberish, Eliza has appropriate responses stored and continues the conversation """


# This is a short Eliza program.
# importing regular expression library and random library.

import re
import random

# The 'response' dictionary is used to respond to the user that it has keys associated with a list containing possible replies.
# for example:- If you start your conversation with  "I need," Eliza will respond by taking any random replies from the list and transform that into a question.

response = {'I need': ["why do you need", "Are you sure you need"],
            'I would': ["could you explain why you would", "why would you"],
            'crave': ["Why don't you tell me more about your cravings"],
            'I want': ["What would it mean to you if you got", "Why do you want", "What would you do if you got"],
            'father': ["Tell me more about your father"],
            'what': ["Why do you ask", "How would an answer to that help you", "What do you think"],
            'anyq': ["Why do you ask that", "Please consider whether you can answer your own question.", "Perhaps the answer lies within yourself", "Why don't you tell me"],
            'anyem': ["Please tell me more.", "Can you elaborate on that?", "Very interesting.", "How does that make you feel?"],
            'because': ["Is that the real reason?", "Does that reason apply to anything else"]}

# The 'translate' dictionary is created for translation purpose

translate = {"am": "are",
             "was": "were",
             "I": "you",
             "I would": "you would",
             "I have": "you have",
             "I will": "you will",
             "are": "am",
             "your": "my",
             "yours": "mine",
             "you": "me",
             "me": "you",
             "my": "your"}

# The chat takes string input from the user. The conversation starts with asking your name.
chat = input("Hi there, What's your name? \n")

# spotting the name from the chat.

if not re.findall(r'([Bb]ye)$|([Ee]xit)$|([Qu]it)$', chat):
  name = re.findall(r'\b[A-Z][a-z]+.?$', chat)
  print("Hi {}, how can I help you today?\n".format(
      " ".join(name).replace(".", "")))
else:
  pass


# while exit or bye or quit is not in the input, the code will search for the phrases
# such as, I need or I would, etc. and execute the conditions accordingly.

while not re.findall(r'([Bb]ye)$|([Ee]xit)$|([Qu]it)$', chat):
  chat = input()
  # searches for the pattern "I need" in the input.
  if re.findall(r'I need (.*)', chat):
    for k, ask in response.items():
      if 'I need' not in k:
        continue
      else:
        tran_key = translate.keys()

        ahead = chat.split(r"need", 1)[1]
        newstring = ahead.split()
        for i in range(0, len(newstring)):
          if newstring[i] in tran_key:
            newstring[i] = translate[newstring[i]]
        print("".join(name) + ", " + random.choice(ask) +
              ' {}?'.format(" ".join(newstring)))

  # searches for the pattern "I want" in the input.
  elif re.findall(r'I want (.*)', chat):
    for k, ask in response.items():
      if 'I want' not in k:
        continue
      else:
        tran_key = translate.keys()

        ahead = chat.split(r"want", 1)[1]
        newstring = ahead.split()
        for i in range(0, len(newstring)):
          if newstring[i] in tran_key:
            newstring[i] = translate[newstring[i]]
        print("".join(name) + ", " + random.choice(ask) +
              ' {}?'.format(" ".join(newstring)))

  # searches for the pattern "I would" in the input.
  elif re.findall(r'I would (.*)', chat):
    for k, ask in response.items():
      if 'I would' not in k:
        continue
      else:
        tran_key = translate.keys()

        ahead = chat.split(r"would", 1)[1]
        newstring = ahead.split()
        for i in range(0, len(newstring)):
          if newstring[i] in tran_key:
            newstring[i] = translate[newstring[i]]
        print("".join(name) + ", " + random.choice(ask) +
              ' {}?'.format(" ".join(newstring)))

  elif re.findall(r'(.*)[Be]cause(.*)', chat):
    for k, ask in response.items():
      if 'because' not in k:
        continue
      else:
        print("".join(name) + ", " + random.choice(ask) + '?')

  elif re.findall(r'(.*)[Cr]ave(.*)', chat):  # spot for the word crave
    for k, ask in response.items():
      if 'crave' not in k:
        continue
      else:
        print("".join(name) + ", " + random.choice(ask) + '?')

  elif re.findall(r'(.*)[Fa]ther(.*)', chat):  # spotting for the word father
    for k, ask in response.items():
      if 'father' not in k:
        continue
      else:
        print("".join(name) + ", " + random.choice(ask) + '?')

  elif re.findall(r'(.*)[Wh]ats?', chat):  # spotting for the word whats
    for k, ask in response.items():
      if 'what' not in k:
        continue
      else:
        print("".join(name) + ", " + random.choice(ask) + '?')

  elif re.findall(r'(.*)[Be]cause', chat):
    for k, ask in response.items():
      if 'because' not in k:
        continue
      else:
        print("".join(name) + ", " + random.choice(ask) + '?')

  # any input lines with a question mark will get some response from Eliza.
  elif re.findall(r'(.*)\?', chat):
    for k, ask in response.items():
      if 'anyq' not in k:
        continue
      else:
        print("".join(name) + ", " + random.choice(ask) + '?')

  # if exit or bye or quit is spotted in the input then Eliza will terminate the conversation.
  elif re.findall(r'([Bb]ye)$|([Ee]xit)$|([Qu]it)$', chat):
    break

  # if no input is provided then also Eliza will respond.
  elif re.findall(r'(.*)', chat):
    for k, ask in response.items():
      if 'anyem' not in k:
        continue
      else:
        print("".join(name) + ", " + random.choice(ask))

  else:
    pass
print("bye and keep in touch")
