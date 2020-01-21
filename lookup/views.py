from django.shortcuts import render

def home(request):
    import json
    import requests
    
    if request.method == 'POST':
        zipcode = request.POST['zipcode']
        api_req = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=' + zipcode + '&distance=5&API_KEY=30F386C6-F557-4864-8067-0BC5C4FC7C4F')


        api = json.loads(api_req.content)
        if api == []:
            api = 'error'
        else:
            api = json.loads(api_req.content)

        if api != 'error':

            if api[0]['Category']['Name'] == "Good":        
                desc = "Air quality is considered satisfactory, and air pollution poses little or no risk."
                color = 'good'

            elif api[0]['Category']['Name'] == "Moderate":   
                desc = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                color = 'moderate'

            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                desc = "Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
                color = 'usg'

            elif api[0]['Category']['Name'] == "Unhealthy":
                desc = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                color = 'unhealthy'

            elif api[0]['Category']['Name'] == "Very Unhealthy":       
                desc = "Health alert: everyone may experience more serious health effects."
                color = 'veryunhealthy'

            elif api[0]['Category']['Name'] == "Hazardous":            
                desc = "Health warnings of emergency conditions. The entire population is more likely to be affected."
                color = 'hazardous'

        if api != 'error':
            return render(request, 'home.html', {'api': api, 'desc': desc, 'color': color})
        else:
            return render(request, 'home.html', {'api': api})

    else:
        api_req = requests.get('http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=-6.175110&longitude=106.865036&distance=5&API_KEY=30F386C6-F557-4864-8067-0BC5C4FC7C4F')

        api = json.loads(api_req.content)
        if api == []:
            api = 'error'
        else:
            api = json.loads(api_req.content)

        if api != 'error':
                    
            if api[0]['Category']['Name'] == "Good":        
                desc = "Air quality is considered satisfactory, and air pollution poses little or no risk."
                color = 'good'

            elif api[0]['Category']['Name'] == "Moderate":   
                desc = "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
                color = 'moderate'

            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                desc = "Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
                color = 'usg'

            elif api[0]['Category']['Name'] == "Unhealthy":
                desc = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                color = 'unhealthy'

            elif api[0]['Category']['Name'] == "Very Unhealthy":
                desc = "Health alert: everyone may experience more serious health effects."
                color = 'veryunhealthy'

            elif api[0]['Category']['Name'] == "Hazardous":            
                desc = "Health warnings of emergency conditions. The entire population is more likely to be affected."
                color = 'hazardous'

        if api != 'error':
            return render(request, 'home.html', {'api': api, 'desc': desc, 'color': color})
        else:
            return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
