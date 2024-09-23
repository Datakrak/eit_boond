from boondmanager import get_boond_csv

def main_index():
    url = "https://ui.boondmanager.com/api/payments.csv?perimeterAgencies=2"
    df = get_boond_csv(url)
    print(df)
    return "Hellow World"

if(__name__) == "__main__":
    main_index()