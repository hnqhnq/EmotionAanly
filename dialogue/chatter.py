# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 11:00
# @File    : chatter.py
# @Author  : hnq

from chatterbot import ChatBot
chatbot=ChatBot("Ron Obvious")

from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("今天星期几")
print(response)
