import csv,pandas as pd

def getHeader(fileName):
    file = open(fileName)
    csvreader = csv.reader(file)
    header = next(csvreader)
    return header

def getAttributesCSV(file):
    header = []
    header = getHeader(file)
    df = pd.read_csv(file,usecols=header)
    deleteValuesNulls(df["Edad"],df)
    #print(df["Edad"])

def deleteValuesNulls(attribute,df):
    cont = 0
    for value in attribute:
        cont += 1
        if value <= 0:
            df.drop(cont,axis=0,inplace=True)





if __name__ == '__main__':
    fileName = 'datos.csv'
    getAttributesCSV(fileName)


