try:
  import json,requests
except Exception as e:
  print(e)
  print('(in a scotish accent)'"I'm giving her all she's got Captain!")
else:
  print("Though I walk through the valley of the shadow of programming, I shall fear no error.")
base_url="https://api.openweathermap.org/data/2.5/weather"
appid=("3a8be193e8bfd32e378c1fe5e0bede9f")



def main():
  message=input("Do you want to search by city or zipcode?")
  message=message.lower()
  if message==("city"):
    city=input("Input city name here: ")
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

  try:
    response=requests.get(url_true)
    unformatted_data=response.json() 
  except Exception as e:
    print(e)
    print("Fear me!")
  else:
    print("connection_established")
  temp=unformatted_data["main"]["temp"]
  temp=float(temp)
  print(f"current temperature is:{temp}\u00B0F")
  
  def temp_conversion():
    global temperature
    temperature=(temp-32)*0.5556
    temperature=round(temperature,2)

  if input(f"Do you want to see what {temp} would be in celsius? Enter Yes or No: ").strip().upper()==("YES"):
    temp_conversion()
    print(f"{temperature}\u00B0C")#I don't know how to get the degree sign so I hope this is close enough
  
  temp_max=unformatted_data["main"]["temp_max"]
  temp_max=float(temp_max)
  print(f"This is your high for today:{temp_max}\u00B0F")

  def max_temp_conversion():
	  global variable_name
	  variable_name=(temp_max-32)*0.5556
	  variable_name=round(variable_name,2)

  if input(f"Do you want to see what {temp_max} would be in celsius? Enter Yes or No: ").strip().upper()==("YES"):
	  max_temp_conversion()
	  print(f"{variable_name}\u00B0C")


while True:
	main()
	if input("Repeat the program?(Y/N): ").strip().upper() != ("Y"):
	  break
#This last while loop with the if statement and the idea to put everything into a main() function came from https://stackoverflow.com/questions/41365922/how-do-i-repeat-the-program-in-python
