from urllib import request

def download_csv(url):
    response = request.urlopen(url)
    csv_str = str(response.read())
    lines = csv_str.split("\\n")
    dest_url = r'file2.csv'
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download_csv("http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip")