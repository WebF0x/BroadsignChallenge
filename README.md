# BroadsignChallenge

Here's my submission for the Broadsign's programming challenge

## Output of the program

```
Question 1
Creating a domain with id=123, name="Broadsign", mac_addresses=[]
Actual content: id=123, name="Broadsign", mac_addresses=[]
Question 2
	Assumption: A domain ID is always between 0x0000 and 0xFFFF to fit in the 2 first bytes
	Assumption: We want to prevent adding an invalid address or an address to the wrong domain
Creating the 3 domains
Filling domains with 10 MAC addresses each
Domain: "domain 1"
	Adress #0: AA:AA:00:00:00:00
	Adress #1: AA:AA:00:00:00:01
	Adress #2: AA:AA:00:00:00:02
	Adress #3: AA:AA:00:00:00:03
	Adress #4: AA:AA:00:00:00:04
	Adress #5: AA:AA:00:00:00:05
	Adress #6: AA:AA:00:00:00:06
	Adress #7: AA:AA:00:00:00:07
	Adress #8: AA:AA:00:00:00:08
	Adress #9: AA:AA:00:00:00:09
Domain: "domain 2"
	Adress #0: BB:BB:00:00:00:00
	Adress #1: BB:BB:00:00:00:01
	Adress #2: BB:BB:00:00:00:02
	Adress #3: BB:BB:00:00:00:03
	Adress #4: BB:BB:00:00:00:04
	Adress #5: BB:BB:00:00:00:05
	Adress #6: BB:BB:00:00:00:06
	Adress #7: BB:BB:00:00:00:07
	Adress #8: BB:BB:00:00:00:08
	Adress #9: BB:BB:00:00:00:09
Domain: "domain 3"
	Adress #0: CC:CC:00:00:00:00
	Adress #1: CC:CC:00:00:00:01
	Adress #2: CC:CC:00:00:00:02
	Adress #3: CC:CC:00:00:00:03
	Adress #4: CC:CC:00:00:00:04
	Adress #5: CC:CC:00:00:00:05
	Adress #6: CC:CC:00:00:00:06
	Adress #7: CC:CC:00:00:00:07
	Adress #8: CC:CC:00:00:00:08
	Adress #9: CC:CC:00:00:00:09
From a MAC address we can obtain its domain ID
For example, here is the domain ID of the MAC address "BB:BB:42:42:42:42"
ID: 48059
```

## Run it yourself

```
git clone https://github.com/WebF0x/BroadsignChallenge.git
cd Broadsign/
python main.py
```
