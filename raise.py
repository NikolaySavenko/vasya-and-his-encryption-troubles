import requests
import time

while True:
	session = requests.Session()
	session.get("https://vasya-and-his-encryption-troubles.vercel.app/")
	print("run!")
	time.sleep(5)
