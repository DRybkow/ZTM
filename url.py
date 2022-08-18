import time, sys, requests

## połączenie internetowe
def urlErr(url):
    # global response 
    try:
        response = requests.get(url,timeout=3)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print ("Http Error.\nUzyskaj połączenie z internetem.")
        time.sleep(3)
        sys.exit()
    except requests.exceptions.ConnectionError:
        print ("Connecting Error.\nUzyskaj połączenie z internetem.")
        time.sleep(3)
        sys.exit()
    except requests.exceptions.Timeout :
        print ("Timeout Error.\nUzyskaj połączenie z internetem.")
        time.sleep(3)
        sys.exit()
    except requests.exceptions.RequestException:
        print ("Something went wrong with your conection.\nUzyskaj połączenie z internetem.")
        time.sleep(3)
        sys.exit()
    return response