from fhir import FHIRHandle, testfhir
import matplotlib.pyplot as plt
import numpy as np


fhir = None
allPatients = None
patientCount = None


plt.rcdefaults()


def initialise():
    global fhir, allPatients, patientCount
    fhir = FHIRHandle()
    allPatients = fhir.getAllPatients()
    patientCount = len(allPatients)


def genderdata():
    data = {'male': 0, 'female': 0}
    for patient in allPatients:
        if patient.gender == 'female':
            data['female'] = data['female'] + 1
        else:
            data['male'] = data['male'] + 1
    return data


def gendergraph():
    data = genderdata()
    plt.clf()
    plt.bar(list(data.keys()), list(data.values()))
    return plt


def agedata():
    ages = np.empty(patientCount)
    count = 0
    for patient in allPatients:
        ages[count] = patient.age()
        count += 1

    bins = np.arange(0,101,10)
    categories = np.digitize(ages,bins)

    ageBinned = np.empty(11)

    for x in range(0, 11):
        get = np.where(categories == (x + 1))
        ageBinned[x] = len(get[0])

    binLabels = ['<10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100', '100+']
    data = {}
    for x in range(0, len(binLabels)):
        label = binLabels[x]
        ageNum = ageBinned[x]

        data[label] = ageNum

    return data


def agegraph():
    data = agedata()
    plt.clf()
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()), rotation='45')
    return plt



def maritaldata():
    statuses = {}
    for patient in allPatients:
        if str(patient.marital_status) in statuses:
            statuses[str(patient.marital_status)] += 1
        else:
            statuses[str(patient.marital_status)] = 1

    return statuses



def maritalgraph():
    marital = maritaldata()
    plt.clf()
    plt.bar(list(marital.keys()), list(marital.values()), align="center")
    return plt


def languagedata():
    lang = {}
    for patient in allPatients:
        for language in patient.communications.languages:
            lang.update(({language: lang.get(language, 0) + 1}))

    return lang


def languagegraph():
    lang = languagedata()
    plt.clf()
    plt.bar(range(len(lang)), list(lang.values()), align='center')
    plt.xticks(range(len(lang)), list(lang.keys()), rotation='vertical')
    return plt

def statedata():
    states = {}
    for patient in allPatients:
        for address in patient.addresses:
            if str(address.state) in states:
                states[str(address.state)] += 1
            else:
                states[str(address.state)] = 1
    return states

def stategraph():
    states = statedata()
    plt.clf()
    plt.bar(range(len(states)), list(states.values()), align='center')
    plt.xticks(range(len(states)), list(states.keys()))
    return plt

def countrydata():
    countries = {}
    for patient in allPatients:
        for address in patient.addresses:
            if str(address.country) in countries:
                countries[str(address.country)] += 1
            else:
                countries[str(address.country)] = 1

    return countries


def countrygraph():
    countries = countrydata()
    plt.clf()
    plt.bar(range(len(countries)), list(countries.values()), align='center')
    plt.xticks(range(len(countries)), list(countries.keys()), rotation='vertical')

    return plt
