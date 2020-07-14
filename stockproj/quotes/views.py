from django.shortcuts import render

def home(request):
    import requests
    import json 

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker "/quote?token=pk_2d493df3ace74135846b58fb4fc7eeb9")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api' : api})

        else:
            
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."})

 

def about(request):
    return render(request, 'about.html', {})

#pk_2d493df3ace74135846b58fb4fc7eeb9