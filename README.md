# Cyclean222Assessment
Instructions:
  Main.py:
    The controller, it randomly sends controls to the broker by bublishing to MQTT broker
    Controls the brightness 0-100
    Controls states 0 off/ 1 on
  CLient.py:
    The light-bulb, subscribes to MQTT broker on 2 topics
    Prints out current states everytime recives a message
    
 Broker for this project is a free broker from EMQX Cloud
