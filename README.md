# FCC Form 499 API Client

Python client for interacting with the FCC Form 499 Filer Database API. 

This client provides a simple interface to search the database of telecommunications carriers, interconnected VoIP providers, and other providers of interstate telecommunications.

## Overview
The FCC Form 499 Filer Database is an identification system for all interstate telecommunications carriers, all interconnected VoIP providers, and certain other providers of interstate telecommunications. These providers are required to register with the Commission using the Telecommunications Reporting Worksheet (FCC Form 499-A) and update their registration on a periodic basis.

## Usage
```python
from fcc_form499 import FCC499Client, States, CommunicationType

# Create client instance
client = FCC499Client()

# Search for providers in Montana with communication type "Other Mobile"
result = client.search(
    states=[States.MONTANA],
    comm_type=CommunicationType.OTHM
)

print(result)
```

### Search Parameters
| Parameter        | Description                                           |
|------------------|-------------------------------------------------------|
| filer_id         | FCC Form 499 Filer ID Number                          |
| legal_name       | Legal or Trade Name of Filer                          |
| frn              | Registration Number (CORESID)                         |
| states           | List of states to search *(use States enum)*          |
| comm_type        | Primary Communications Type *(use CommunicationType)* |
| logical_operator | Logical operator for joining states *(AND/OR)*        |

### Communication Types
| Type | Description                         |
|------|-------------------------------------|
| ABS  | Audio Bridge Service                |
| ALLD | All Distance                        |
| COAX | Cable TV provider of local exchange |
| VOIP | Interconnected VoIP                 |
| CAP  | CAP/LEC                             |
| CEL  | Cellular/PCS/SMR                    |
| DAT  | Wireless Data                       |
| IXC  | Interexchange Carrier               |
| LEC  | Incumbent Local Exchange Carrier    |
| LRES | Local Reseller                      |
| OSP  | Operator Service Provider           |
| OTHL | Other Local                         |
| OTHM | Other Mobile                        |
| OTHT | Other Toll                          |
| PAG  | Paging & Messaging                  |
| PAY  | Payphone Service Provider           |
| PRE  | Prepaid Card                        |
| PRIV | Private Service Provider            |
| SAT  | Satellite                           |
| SMR  | SMR (dispatch)                      |
| TEN  | Shared Tenant Service Provider      |
| TRES | Toll Reseller                       |

## Errors
| Error code | Description                                 |
|------------|---------------------------------------------|
| 1          | Invalid state value                         |
| 2          | Could not execute query. Invalid parameters |
| 3          | No results found. Check Query parameters.   |
| 4          | Invalid value for FRN.                      |
| 5          | Invalid value for Filer ID.                 |
| 6          | Invalid value for Communications Type.      |
| 7          | Wrong Request Method. Only GET is allowed.  |

## References
* [FCC Form 499 Filer Database](http://apps.fcc.gov/cgb/form499/499a.cfm)
* [FCC Form 499-A](https://www.fcc.gov/formpage.html)
* [USAC Online Filing](http://forms.universalservice.org)

___

###### Mirrors for this repository: [acid.vegas](https://git.acid.vegas/fcc-form499-api) • [SuperNETs](https://git.supernets.org/acidvegas/fcc-form499-api) • [GitHub](https://github.com/acidvegas/fcc-form499-api) • [GitLab](https://gitlab.com/acidvegas/fcc-form499-api) • [Codeberg](https://codeberg.org/acidvegas/fcc-form499-api)
