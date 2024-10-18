# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

##############################################################
## TIME REQUEST ##
##############################################################

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime
from typing import Any, Text, Dict, List

class ActionGetTime(Action):
    def name(self):
        return "action_get_time"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        current_time = datetime.now().strftime("%H:%M:%S")
        # Return SlotSet event and message to the user
        return [SlotSet("time", current_time), 
                dispatcher.utter_message(text=f"The current time is {current_time}")]

class ActionGetDate(Action):
    def name(self):
        return "action_get_date"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        current_date = datetime.now().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
        # Return SlotSet event and message to the user
        return [SlotSet("date", current_date), 
                dispatcher.utter_message(text=f"Today's date is {current_date}.")]

class ActionCurrentDateTime(Action):
    def name(self) -> str:
        return "action_current_date_time"

    def run(self, dispatcher, tracker, domain):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dispatcher.utter_message(text=f"The current date and time is {current_time}.")
        return []

class ActionTimeBasedGreeting(Action):

    def name(self) -> str:
        return "action_time_based_greeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:

        # Get the current time
        current_time = datetime.now().hour

        # Define greeting based on time
        if 5 <= current_time < 12:
            greeting = "Good morning! How are you?"
        elif 12 <= current_time < 17:
            greeting = "Good afternoon! How is everything?"
        elif 17 <= current_time < 21:
            greeting = "Good evening! How was your day?"
        else:
            greeting = "Hey! How are you?"

        # Send the greeting to the user
        dispatcher.utter_message(text=greeting)

        return []
    