# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests
import os            
# from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import re
from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType, SlotSet
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from pyparsing import nestedExpr
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# load_dotenv()
wakey= os.getenv("wakey") 

# NOTE(Michael): We could use this action to store the name in
#                the TrackerStore (in memory database) or a persitent DB
#                such as MySQL. But we need to store a key-value pair 
#                to identify the user by id eg. (user_id, slotvalue)


class ActionStoreUserName(Action):

     def name(self) -> Text:
         return "action_store_name"
         
     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        print("Sender ID: ", tracker.sender_id)

        return []


class ActionUserName(Action):

     def name(self) -> Text:
         return "action_get_name"

     def run(self, dispatcher, tracker, domain):
        username = tracker.get_slot("username")
        if not username :
            dispatcher.utter_message(" Du hast mir Deinen Namen nicht gesagt.")
        else:
            dispatcher.utter_message(' Du bist {}'.format(username))

        return []


class Wetter(Action):
    def name(self) -> Text:
        return "action_get_weather"
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        # city_name = tracker.get_slot("wacity")
        city_name = "München"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + "some_api_key" + "&q=" + city_name + "&units=metric" + "&lang=de"
        response = requests.get(complete_url)
        print(response)
        # x = response.json()["main"]
        # desc = response.json()["weather"]
        # current_temperature = x["temp"]
        # weather_description = desc[0]["description"]
        # dispatcher.utter_button_message(f"In {city_name} sind es " + str(current_temperature) + "°C. \nAktueller Wetterstatus: " + str(weather_description))
        dispatcher.utter_message("Hello from weather API")
        return
