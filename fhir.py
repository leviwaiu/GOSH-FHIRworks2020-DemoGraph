from fhir_parser import FHIR


def testfhir():
    # fhir = FHIR()
    fhir = FHIR(endpoint="https://fhir.compositegrid.com:5001/api/")
    patients = fhir.get_patient('8f789d0b-3145-4cf2-8504-13159edaa747')
    print(patients)


class FHIRHandle:
    fhir = None

    def __init__(self, endpoint="https://fhir.compositegrid.com:5001/api/"):
        self.fhir = FHIR(endpoint=endpoint)

    def getPatient(self, patientId):
        return self.fhir.get_patient(patientId)

    def getAllPatients(self):
        return self.fhir.get_all_patients()

