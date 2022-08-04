import json,requests 
base_url="https://api.openweathermap.org/data/2.5/weather"
appid=("3a8be193e8bfd32e378c1fe5e0bede9f")



def main():


	message=input("Do you want to search by city or zipcode?")
	message=message.lower()


	if message==("city"):
		city=input("Input city name here: ")
		test_value=city.isalpha()
		while test_value!=True:# https://datascienceparichay.com/article/python-check-if-string-contains-only-letters/
			city=input("Please enter a vaild response: ")
			test_value=city.isalpha()

		url_true=(f"{base_url}?q={city}&units=imperial&APPID={appid}")

	elif message==("zipcode"):
		zipcode=input("Enter zipcode here: ")
		test_value2=zipcode.isalpha()

		while test_value2!=False:
			zipcode=input("Please enter a vaild response: ")
			test_value2=zipcode.isalpha()

		url_true=(f"{base_url}?q={zipcode}&units=imperial&APPID={appid}")

	else:
		exit()

	print(url_true)
	print()
	response=requests.get(url_true)

	unformatted_data=response.json() 

	temp=unformatted_data["main"]["temp"]
	temp=float(temp)
	print(f"message{temp}")

	def temp_conversion():
		global temperature
		temperature=(temp-32)*0.5556
		temperature=round(temperature,2)

	question=input(f"Do you want to see what {temp} would be in celsius? Enter Yes or No: ")
	question=question.title()

	if question==("Yes"):
		temp_conversion()
		print(temperature," C")#I don't know how to get the degree sign so I hope this is close enough

	temp_max=unformatted_data["main"]["temp_max"]
	temp_max=float(temp_max)
	print(f"message{temp_max}")

	def max_temp_conversion():
		global variable_name
		variable_name=(temp_max-32)*0.5556
		variable_name=round(variable_name,2)

	question_2=input(f"Do you want to see what {temp_max} would be in celsius? Enter Yes or No: ")
	question_2=question_2.title()

	if question_2==("Yes"):
		max_temp_conversion()
		print(variable_name," C")


while True:
	main()
	if input("Repeat the program?(Y/N): ").strip().upper() != ("Y"):
	  break
