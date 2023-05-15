import jinja2

from sap_quiz import SAP_audit


class SAP_report:

    def __init__(self, sap_audit: SAP_audit = None):


        template = """
        
        header:
          author:
            name: {{ author.name }}
            status: {{ author.status }}
         
        body:
          fields:
            {% for field in fields %}
            - name: {{ field.name }}
              value: {{ field.value }}  
            {% endfor %} 
        
        """

        author = {
            'name': 'Roman',
            'status': 'Student'
        }
        fields = [
            {
                'name': 'F1',
                'value': 'FV1',
            },
            {
                'name': 'F2',
                'value': 'FV2',
            },
            {
                'name': 'F3',
                'value': 'FV3',
            },
            {
                'name': 'F4',
                'value': 'FV4',
            },
        ]

        tmp = jinja2.Template(template)
        render = tmp.render(**sap_audit.__dict__)
        print(render)


if __name__ == "__main__":

    sap_r = SAP_report()
