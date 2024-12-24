#!/usr/bin/env python3
# FCC Form499 API Client - Developed by acidvegas in Python (https://git.acid.vegas/fcc-form499-api)

from enum import Enum
import urllib.error
import urllib.parse
import urllib.request

class States(str, Enum):
    '''List of valid states'''

    ALABAMA                  = 'alabama'
    ALASKA                   = 'alaska'
    AMERICAN_SAMOA           = 'american_samoa'
    ARIZONA                  = 'arizona'
    ARKANSAS                 = 'arkansas'
    CALIFORNIA               = 'california'
    COLORADO                 = 'colorado'
    CONNECTICUT              = 'connecticut'
    DELAWARE                 = 'delaware'
    DISTRICT_OF_COLUMBIA     = 'district_of_columbia'
    FLORIDA                  = 'florida'
    GEORGIA                  = 'georgia'
    GUAM                     = 'guam'
    HAWAII                   = 'hawaii'
    IDAHO                    = 'idaho'
    ILLINOIS                 = 'illinois'
    INDIANA                  = 'indiana'
    IOWA                     = 'iowa'
    JOHNSTON_ATOLL           = 'johnston_atoll'
    KANSAS                   = 'kansas'
    KENTUCKY                 = 'kentucky'
    LOUISIANA                = 'louisiana'
    MAINE                    = 'maine'
    MARYLAND                 = 'maryland'
    MASSACHUSETTS            = 'massachusetts'
    MICHIGAN                 = 'michigan'
    MIDWAY_ATOLL             = 'midway_atoll'
    MINNESOTA                = 'minnesota'
    MISSISSIPPI              = 'mississippi'
    MISSOURI                 = 'missouri'
    MONTANA                  = 'montana'
    NEBRASKA                 = 'nebraska'
    NEVADA                   = 'nevada'
    NEW_HAMPSHIRE            = 'new_hampshire'
    NEW_JERSEY               = 'new_jersey'
    NEW_MEXICO               = 'new_mexico'
    NEW_YORK                 = 'new_york'
    NORTH_CAROLINA           = 'north_carolina'
    NORTH_DAKOTA             = 'north_dakota'
    NORTHERN_MARIANA_ISLANDS = 'northern_mariana_islands'
    OHIO                     = 'ohio'
    OKLAHOMA                 = 'oklahoma'
    OREGON                   = 'oregon'
    PENNSYLVANIA             = 'pennsylvania'
    PUERTO_RICO              = 'puerto_rico'
    RHODE_ISLAND             = 'rhode_island'
    SOUTH_CAROLINA           = 'south_carolina'
    SOUTH_DAKOTA             = 'south_dakota'
    TENNESSEE                = 'tennessee'
    TEXAS                    = 'texas'
    UTAH                     = 'utah'
    US_VIRGIN_ISLANDS        = 'us_virgin_islands'
    VERMONT                  = 'vermont'
    VIRGINIA                 = 'virginia'
    WAKE_ISLAND              = 'wake_island'
    WASHINGTON               = 'washington'
    WEST_VIRGINIA            = 'west_virginia'
    WISCONSIN                = 'wisconsin'
    WYOMING                  = 'wyoming'


class CommunicationType(str, Enum):
    '''List of valid communication types'''

    ABS  = 'ABS'  # Audio Bridge Service
    ALLD = 'ALLD' # All Distance
    COAX = 'COAX' # Cable TV provider of local exchange
    VOIP = 'VOIP' # Interconnected VoIP
    CAP  = 'CAP'  # CAP/LEC
    CEL  = 'CEL'  # Cellular/PCS/SMR
    DAT  = 'DAT'  # Wireless Data
    IXC  = 'IXC'  # Interexchange Carrier
    LEC  = 'LEC'  # Incumbent Local Exchange Carrier
    LRES = 'LRES' # Local Reseller
    OSP  = 'OSP'  # Operator Service Provider
    OTHL = 'OTHL' # Other Local
    OTHM = 'OTHM' # Other Mobile
    OTHT = 'OTHT' # Other Toll
    PAG  = 'PAG'  # Paging & Messaging
    PAY  = 'PAY'  # Payphone Service Provider
    PRE  = 'PRE'  # Prepaid Card
    PRIV = 'PRIV' # Private Service Provider
    SAT  = 'SAT'  # Satellite
    SMR  = 'SMR'  # SMR (dispatch)
    TEN  = 'TEN'  # Shared Tenant Service Provider
    TRES = 'TRES' # Toll Reseller


class LogicalOperator(str, Enum):
    '''List of valid logical operators'''

    AND = 'AND'
    OR  = 'OR'


class FCC499Client:
    '''FCC Form 499 API Client'''

    # FCC Form 499 API URL
    BASE_URL = 'http://apps.fcc.gov/cgb/form499/499results.cfm'
    

    def search(self, filer_id=None, legal_name=None, frn=None, states=None, comm_type=None, logical_operator=LogicalOperator.AND):
        '''
        Search the FCC Form 499 Filer Database
        
        :param filer_id: str - The FCC Form 499 Filer ID
        :param legal_name: str - The legal name of the filer
        :param frn: str - The FRN of the filer
        :param states: list[States] - The states to search for
        :param comm_type: CommunicationType - The communication type to search for
        :param logical_operator: LogicalOperator - The logical operator to use
        '''
        
        # Set the default parameters
        params = {'XML': 'TRUE', 'R1': logical_operator.value}
        
        # Add the parameters to the request
        if filer_id:
            params['FilerID'] = filer_id
        if legal_name:
            params['LegalName'] = legal_name
        if frn:
            params['frn'] = frn
        if states:
            params['state'] = ','.join(state.value for state in states)
        if comm_type:
            params['comm_type'] = comm_type.value
            
        # Build the URL
        url = f'{self.BASE_URL}?{urllib.parse.urlencode(params)}'
        
        # Make the request
        try:
            with urllib.request.urlopen(url) as response:
                if response.status != 200:
                    raise ValueError(f'API request failed with status code: {response.status}')
                return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            raise ValueError(f'API request failed with status code: {e.code}')
        except urllib.error.URLError as e:
            raise ValueError(f'API request failed: {str(e)}')


def main():
    client = FCC499Client()
    
    try:
        result = client.search(states=[States.MONTANA], comm_type=CommunicationType.OTHM)
        print(result)        
    except Exception as e:
        print(f'Error: {str(e)}')


if __name__ == '__main__':
    main() 
