from urllib import request
goog_url="http://samplecsvs.s3.amazonaws.com/SacramentocrimeJanuary2006.csv"


def download(csv_url):
    response = request.urlopen(csv_url)#we had reached that webpage
    csv = response.read()#data is now in csv
    csv_str = str(csv)
    lines=csv_str.split("\\n")#split takes a huge sting and breaks it
    dest_url = r'goog.csv'#its good to use r when working with file
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download(goog_url)