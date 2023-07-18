import requests

def main():
    headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "currency-converter-by-api-ninjas.p.rapidapi.com"
    }

    current_currency = input("Please enter which currency you are converting from: ");
    amount = input("Please enter the amount: ")
    converted_currency = input("Please enter the currency to convert to: ")

    url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

    querystring = {"have": current_currency ,"want": converted_currency,"amount": amount}

    


    response = requests.get(url, headers=headers, params= querystring)
    response_list = response.json()

    errors = response_list.get('error')
    new_value = response_list.get('new_amount')

    if errors == None:
        print("Your new converted value is", new_value, converted_currency)
    else:
        print("Your error was: ", errors, ". Please try again.")
        


if __name__ == "__main__":
    main()
