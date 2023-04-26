import json
import tempfile
import requests
from typing import List

from mitreattack.stix20 import MitreAttackData


class Mitre:
    def __init__(self) -> None:
        self.tmp_file = tempfile.NamedTemporaryFile(mode='w+', prefix='enterprise-attack', suffix='.json')
        self.raw_data_path = self.tmp_file.name
        self.enterprise_endpoint = 'https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json'

        local_db = self.__generate_local_enterprise_database()

        if local_db:
            self.mitre_attack_data = MitreAttackData(stix_filepath=self.raw_data_path)
            self.tmp_file.close()
        else:
            self.tmp_file.close()
            raise Exception("Local Mitre database not found.")

    def __generate_local_enterprise_database(self) -> bool:
        try:
            enterprise_data = requests.get(self.enterprise_endpoint).json()
            json.dump(enterprise_data, self.tmp_file,  ensure_ascii=False, indent=4)
            self.tmp_file.flush()
            print(f'The local database was successfuly generated.')
            return True

        except Exception as error:
            print(f'Error on generate_local_enterprise_database(). {error}')
            return False

    def get_all_tactics(self) -> List[dict]:
        tactics = self.mitre_attack_data.get_tactics(
            remove_revoked_deprecated=True)
        data = [json.loads(i.serialize()) for i in tactics]
        return data

    def get_techniques_by_tactic(self, tactic_shortname: str, domain='enterprise-attack') -> List[dict]:
        """
        Retrieve techniques by tactic.

        Parameters:
            tactic_shortname (str) - the x_mitre_shortname of the tactic (e.g. 'defense-evasion')
            domain (str) - domain of the tactic (must be 'enterprise-attack', 'mobile-attac', or 'ics-attack')
            remove_revoked_deprecated (bool, optional) - remove revoked or deprecated objects from the query, by default False
        """
        techniques = self.mitre_attack_data.get_techniques_by_tactic(
            tactic_shortname=tactic_shortname,
            domain=domain,
            remove_revoked_deprecated=True
        )
        data = [json.loads(i.serialize()) for i in techniques]
        return data
