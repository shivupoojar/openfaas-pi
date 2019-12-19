import requests
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    # Get the value from the http request body Extract string value, Ex:
    # Pressure= 1010.19090 Split by =, convert it into float
    URL = "https://api.thingspeak.com/update?api_key=LJC420IXZOZ7YNSD&"
    data=req.split('=')
    value=float(data[1])
    # Check for higher or lower than 1010
    if int(value) > 1010
	a= 'Y'
# Insert a data into thingspeak using HTTP GET method
    	params1={'field1':data}
	r=requests.get(URL,params=params1)
    else:
    	a='N'
# return response with Y or N
    return (a)
