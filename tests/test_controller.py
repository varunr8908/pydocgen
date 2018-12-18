import os
import pytest
import base64
from flask import jsonify
from pydocgen import app

@pytest.fixture
def client():
    client = app.test_client()
    yield client

def test_app_running(client):
    rv = client.get('/')
    assert b'App is Up!!' in rv.data

def test_app_docgen(client):
    reqjson = genrequestjson()
    rv = client.post('/docgenerate', json = reqjson)
    json_data = rv.get_json()
    print(json_data)

def genrequestjson():
  root_directory = os.path.dirname(os.path.dirname(__file__))
  with open(os.path.join(root_directory,"./tests/covertemplate_libre.docx"), "rb") as cover_file:
    covertemplate_string = base64.b64encode(cover_file.read())
  with open(os.path.join(root_directory,"./tests/sbctemplate_libre.docx"), "rb") as sbc_file:
    sbctemplate_string = base64.b64encode(sbc_file.read())
  with open(os.path.join(root_directory,"./tests/footertemplate_libre.docx"), "rb") as footer_file:
    footertemplate_string = base64.b64encode(footer_file.read())
       
  reqJson = {
  'DocFormat': 'pdf',
  'CoverTemplate':covertemplate_string.decode('ascii'),
  'GroupName': 'Distant Towers LLC',
  'EffectiveDate': '11/1/2018',
  'DateCreated': '11/1/2018',
  'PreparedBy': 'John Bluth',
  'AgencyName': '',
  'PBEmail': 'john.bluth@nomail.com',
  'QuoteId': '0Q0f4000000RWxkCAG',
  'Zipcode': '33002',
  'RatingRegion': 'Miami-Dade',
  'FooterTemplate': footertemplate_string.decode('ascii'),
  'QuotedPlans': [
    {
      'BusinessPackageId': 'Small Group Achieve MS 100',
      'SBCTemplate': sbctemplate_string.decode('ascii'),
      'MonthlyPremium': '$10499.32',
      'SBC': [
        {
          'Name': 'Coinsurance',
          'INN': '0%',
          'ONN': '25%'
        },
        {
          'Name': 'Out of Pocket Max (Includes Deductible)',
          'INN': '$7,500 individual/$15,600 family. Pediatric Dental is limited to $350 per child, or $700 for 2 or more children.',
          'ONN': '$20,400 individual/$40,800 family. Pediatric Dental is limited to $350 per child, or $700 for 2 or more children.'
        },
        {
          'Name': 'Inpatient Hospital Cost Share',
          'INN': '$750 copay/day for the first 3 days per admission, after deductible',
          'ONN': '50% Coinsurance after deductible'
        },
        {
          'Name': 'Deductible',
          'INN': '$3,500 individual/$7,500 family Doesnt apply to preventive care',
          'ONN': '$7,500 individual/$15,000 family Doesnt apply to preventive care'
        },
        {
          'Name': 'ER Cost Share',
          'INN': '$600 copay/ visit',
          'ONN': 'Same as AvMed Network'
        },
        {
          'Name': 'Urgent Care Cost Share',
          'INN': '$125 copay/ visit at urgent care facilities; $35 copay/ visit at retail clinics',
          'ONN': '50% coinsurance after deductible at urgent care facilities or retail clinics'
        },
        {
          'Name': 'Imaging Tests (CT / PET scans / MRIs) Cost Share',
          'INN': '$350 copay/ visit at independent facilities; $1,000 copay/ visit after deductible at all other facilities',
          'ONN': '50% Coinsurance after deductible'
        },
        {
          'Name': 'PCP Cost Share',
          'INN': 'No charge for first non-preventive visit; $35 copay/ visit thereafter',
          'ONN': '50% Coinsurance after deductible'
        },
        {
          'Name': 'Specialist Cost Share (No Referral Needed)',
          'INN': '$75 copay/ visit',
          'ONN': '50% Coinsurance after deductible'
        },
        {
          'Name': 'Other Deductible',
          'INN': '$65 per child for Pediatric Dental. Doesn’t apply to overall deductible. There are no other specific deductibles.',
          'ONN': 'Not Applicable'
        },
        {
          'Name': 'Outpatient Surgery Cost Share',
          'INN': '$1500 copay/ visit at independent facilities; $1000 copay/ visit after deductible at all other facilities',
          'ONN': '50% Coinsurance after deductible'
        },
        {
          'Name': 'Drug Cost Share',
          'INN': 'Generic - $25 copay (retail)/ $62.50 copay (mail order) Preferred Brand - $55 copay (retail)/ $137.50 copay (mail order) Non-Preferred Brand - $95 copay (retail)/ $237.50 copay (mail order) Specialty - 50% coinsurance after deductible (retail only)',
          'ONN': 'Not Covered'
        }
      ],
      'QuoteCensus': [
        {
          'EmployeeName': 'Mark Levingston',
          'EmployeeNumber': 'A001',
          'BirthDate': '11/9/1986',
          'NumberOfDependents': '2',
          'FamilyRate': '$419.16'
        },
        {
          'EmployeeName': 'Fred Therou',
          'EmployeeNumber': 'A002',
          'BirthDate': '3/4/1989',
          'NumberOfDependents': '1',
          'FamilyRate': '$396.49'
        },
        {
          'EmployeeName': 'Harry Davidson',
          'EmployeeNumber': 'A003',
          'BirthDate': '5/4/1978',
          'NumberOfDependents': '1',
          'FamilyRate': '$452.83'
        },
        {
          'EmployeeName': 'Bruce Campbell',
          'EmployeeNumber': 'A004',
          'BirthDate': '5/4/1983',
          'NumberOfDependents': '0',
          'FamilyRate': '$432.98'
        },
        {
          'EmployeeName': 'David ORourke',
          'EmployeeNumber': 'A005',
          'BirthDate': '7/21/1985',
          'NumberOfDependents': '0',
          'FamilyRate': '$424.48'
        },
        {
          'EmployeeName': 'John Fields',
          'EmployeeNumber': 'A006',
          'BirthDate': '11/9/1989',
          'NumberOfDependents': '3',
          'FamilyRate': '$396.49'
        },
        {
          'EmployeeName': 'Kevin Moore',
          'EmployeeNumber': 'A007',
          'BirthDate': '12/11/1989',
          'NumberOfDependents': '0',
          'FamilyRate': '$385.15'
        },
        {
          'EmployeeName': 'Bryan Friedson',
          'EmployeeNumber': 'A008',
          'BirthDate': '10/15/1985',
          'NumberOfDependents': '0',
          'FamilyRate': '$424.48'
        },
        {
          'EmployeeName': 'David Parker',
          'EmployeeNumber': 'A009',
          'BirthDate': '5/4/1983',
          'NumberOfDependents': '0',
          'FamilyRate': '$432.98'
        },
        {
          'EmployeeName': 'Henry Blake',
          'EmployeeNumber': 'A010',
          'BirthDate': '11/9/1986',
          'NumberOfDependents': '2',
          'FamilyRate': '$419.16'
        },
        {
          'EmployeeName': 'Kevin Wayne',
          'EmployeeNumber': 'A015',
          'BirthDate': '5/23/1990',
          'NumberOfDependents': '0',
          'FamilyRate': '$385.15'
        },
        {
          'EmployeeName': 'Luke Stevenson',
          'EmployeeNumber': 'A016',
          'BirthDate': '6/7/1990',
          'NumberOfDependents': '2',
          'FamilyRate': '$385.15'
        },
        {
          'EmployeeName': 'Jesus Lugo',
          'EmployeeNumber': 'A011',
          'BirthDate': '11/5/1982',
          'NumberOfDependents': '1',
          'FamilyRate': '$435.82'
        },
        {
          'EmployeeName': 'Benjamin Rodstein',
          'EmployeeNumber': 'A012',
          'BirthDate': '11/5/1982',
          'NumberOfDependents': '0',
          'FamilyRate': '$435.82'
        },
        {
          'EmployeeName': 'John Smith',
          'EmployeeNumber': 'A013',
          'BirthDate': '11/11/1986',
          'NumberOfDependents': '0',
          'FamilyRate': '$419.16'
        },
        {
          'EmployeeName': 'Dwayne Jonson',
          'EmployeeNumber': 'A014',
          'BirthDate': '5/4/1978',
          'NumberOfDependents': '0',
          'FamilyRate': '$452.83'
        }
      ]
    }
  ]
    }
  return reqJson

