# Cyclean222Assessment
Instructions:<br />
&ensp;&ensp;Main.py:<br />
&ensp;&ensp;&ensp;&ensp;The controller, it randomly sends controls to the broker by bublishing to MQTT broker<br />
&ensp;&ensp;&ensp;&ensp;Controls the brightness 0-100<br />
&ensp;&ensp;&ensp;&ensp;Controls states 0 off/ 1 on<br />
&ensp;&ensp;CLient.py:<br />
&ensp;&ensp;&ensp;&ensp;The light-bulb, subscribes to MQTT broker on 2 topics<br />
&ensp;&ensp;&ensp;&ensp;Prints out current states everytime recives a message<br />
    
 Broker for this project is a free broker from EMQX Cloud<br />
