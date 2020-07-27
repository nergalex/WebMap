from flask import (Flask, request)
from flask_restful import (Api, Resource)
from flasgger import Swagger

# -------------- API --------------
# listener
application = Flask(__name__)
"""
application.config['SWAGGER'] = {
    'title': 'WebMap F5',
    'openapi': '3.0.2'
}
"""
api = Api(application)
swagger = Swagger(application)


class ApiExport(Resource):
    def get(self):
        """
        Export
        ---
        tags:
          - poc
        parameters:
          - name: f
            in: query
            required: true
            description: file type
            type: string
            default: json
          - name: bbox
            in: query
            required: true
            description: geo location
            type: string
            default: '2.336160547833903,48.85683241962956,2.3533266855292156,48.86193225878908'
          - name: size
            in: query
            required: true
            description: screen size
            type: string
            default: '1600,723'
          - name: imageSR
            in: query
            required: true
            description: image rendering
            type: integer
            default: 102113
          - name: bboxSR
            in: query
            required: true
            description: location in screen
            type: integer
            default: 4326
          - name: format
            in: query
            required: true
            description: requested format
            type: string
            enum: ['png32', 'jpg']
            default: png32
          - name: layerDefs
            in: query
            required: true
            description: layer definition
            type: string
            default: '{}'
          - name: layers
            in: query
            required: true
            description: layers
            type: string
            default: '1,2,3,4,7,8,9,10,9999'
          - name: transparent
            in: query
            required: true
            description: transparent
            type: string
            default: 'true'
          - name: callback
            in: query
            required: true
            description: callback
            type: string
            default: 'ags_jsonp.ags_jsonp_21_195424'
        definitions:
          extent:
            type: object
            properties:
              xmin:
                type: number
                format: double
              ymin:
                type: number
                format: double
              xmax:
                type: number
                format: double
              ymax:
                type: number
                format: double
              spatialReference:
                $ref: '#/definitions/spatialReference'
          spatialReference:
            type: object
            properties:
              wkid:
                type: integer
              latestWkid:
                type: integer
        responses:
          200:
            description: Returns an image
            schema:
              id: export
              type: object
              properties:
                href:
                  type: string
                width:
                  type: integer
                height:
                  type: integer
                extent:
                  $ref: '#/definitions/extent'
                scale:
                  type: number
                  format: double
        """
        msg = {
            "href": "https://my-app.dev/agsids/rest/directories/arcgisoutput/SIROCCO/SIROCARTE_MapServer/_ags_mapee4c9fa13681478794d0f4b720d2a3a6.png",
            "width": 1600,
            "height": 723,
            "extent": {
                "xmin": 260060.20259620514,
                "ymin": 6250603.3747053985,
                "xmax": 261971.12830333452,
                "ymax": 6251466.874259308,
                "spatialReference": {
                    "wkid":102113,
                    "latestWkid":3785
                }
            },
            "scale": 4513.988705381028
        }
        return msg, 201


class ApiIdentify(Resource):
    def get(self):
        """
        Identify
        ---
        tags:
          - poc
        parameters:
          - name: geometry
            in: query
            required: true
            description: json
            type: string
            default: '{x:2.354936010938151,y:48.85728066161469, spatialReference:{wkid:4326}}'
          - name: geometryType
            in: query
            required: true
            description: geometryType
            type: string
            default: esriGeometryPoint
          - name: mapExtent
            in: query
            required: true
            description: mapExtent
            type: string
            default: '{xmin:2.3287147356085613,ymin:48.85350400910461,xmax:2.3630470109991863,ymax:48.863703846006224, spatialReference:{wkid:4326}}'
          - name: tolerance
            in: query
            required: true
            description: tolerance
            type: integer
            default: 15
          - name: sr
            in: query
            required: true
            description: sr
            type: integer
            default: 4326
          - name: imageDisplay
            in: query
            required: true
            description: imageDisplay
            type: string
            default: '1600,723,96'
          - name: layers
            in: query
            required: true
            description: layers
            type: string
            default: 'visible:1,2,3,4,7,8,9,10'
          - name: returnGeometry
            in: query
            required: true
            description: returnGeometry
            type: string
            default: 'true'
          - name: callback
            in: query
            required: true
            description: callback
            type: string
            default: 'ags_jsonp.ags_jsonp_25_537217'
          - name: f
            in: query
            required: true
            description: file type
            type: string
            default: json
        responses:
          200:
            description: data
        """
        msg = {
            "results": [
                {
                    "layerId": 2,
                    "layerName": "OSR : Branchement neuf",
                    "displayFieldName": "ID_BAN",
                    "value": "75XXX4_9704_00014",
                    "attributes": {
                        "OBJECTID": "9093",
                        "ID_BAN": "75XXX_9704_00014",
                        "SCORE_NORMALISATION": "0.7625",
                        "SCORE_POSITION": "1_PntAdressePl",
                        "LIBELLE_NORMALISE": "XX Rue de la XX 75XXX Paris Xe Arrondissement (75XXX)",
                        "NUM_AFFAIRE": "XXXXXXXXXX",
                        "TITRE_CHANTIER": "RUE DE LA VERRERIE XX Emp: rue XXXXX XXXXX  PARIS XX FR",
                        "REGION": "PARIS",
                        "NATURE_CHANTIER": "Branchement neuf",
                        "AGENT_NOM": "NAME NAME",
                        "CODE_INSEE": "75104",
                        "CHANTIER_COMMUNE": "PARIS X",
                        "CHANTIER_RUE": "XX RUE DE LA XX",
                        "CHANTIER_NUMERO_RUE": "Null",
                        "DATE_DEBUT_PREVISIONNELLE": "Null",
                        "DATE_FIN_PREVISIONNELLE": "Null",
                        "DATE_OUVERTURE": "Null",
                        "DATE_FERMETURE": "Null",
                        "DATE_REFECTION_PREV": "Null",
                        "DATE_REFECTION_REAL": "Null",
                        "ETAT_AVANCEMENT": "Réalisée",
                        "AGENT_TELEPHONE": "Null",
                        "SHAPE": "Point",
                        "AGENT_EMAIL": "email@email.dev"
                    },
                    "geometryType": "esriGeometryPoint",
                    "geometry":
                        {
                            "x": 2.3549541979747688,
                            "y": 48.857269954426656,
                            "spatialReference": {
                                "wkid": 4326,
                                "latestWkid": 4326
                            }
                        }
                },
                {
                    "layerId": 4,
                    "layerName": "OSR : Branchement à supprimer",
                    "displayFieldName": "ID_BAN",
                    "value": "75XXX_9704_00014",
                    "attributes": {
                        "OBJECTID": "7483",
                        "ID_BAN": "75XXX_9704_00014",
                        "SCORE_NORMALISATION": "0.7625",
                        "SCORE_POSITION": "1_PntAdressePl",
                        "LIBELLE_NORMALISE": "XX Rue de la Verrerie 75XXX Paris Xe Arrondissement (75XXX)",
                        "NUM_AFFAIRE": "XXXXXXXXXX",
                        "TITRE_CHANTIER": "RUE DE LA VERRERIE XX Emp: rue 75XXX 75XXX  PARIS XX FR",
                        "REGION": "PARIS",
                        "NATURE_CHANTIER": "Branchement à supprimer",
                        "AGENT_NOM": "NAME NAME",
                        "CODE_INSEE": "75XXX",
                        "CHANTIER_COMMUNE": "PARIS X",
                        "CHANTIER_RUE": "XX RUE DE LA VERRERIE",
                        "CHANTIER_NUMERO_RUE": "Null",
                        "DATE_DEBUT_PREVISIONNELLE": "Null",
                        "DATE_FIN_PREVISIONNELLE": "Null",
                        "DATE_OUVERTURE": "Null",
                        "DATE_FERMETURE": "Null",
                        "DATE_REFECTION_PREV": "Null",
                        "DATE_REFECTION_REAL": "Null",
                        "ETAT_AVANCEMENT": "Prise en charge",
                        "AGENT_TELEPHONE": "Null",
                        "SHAPE": "Point",
                        "AGENT_EMAIL": "email@email.dev"
                    },
                    "geometryType": "esriGeometryPoint",
                    "geometry":
                        {
                            "x": 2.3549541979747688,
                            "y": 48.857269954426656,
                            "spatialReference":
                                {
                                    "wkid": 4326,
                                    "latestWkid": 4326
                                }
                        }
                }
            ]
        }
        return msg, 201


class ApiSpatial(Resource):
    def post(self):
        """
        Spatial request
        ---
        tags:
          - poc
        consumes:
          - application/json; charset=utf-8
        parameters:
          - in: body
            name: body
            schema:
              required:
                - geometry
                - geometryType
                - outFields
                - inSR
                - returnGeometry
                - f
                - returnCountOnly
                - outSR
                - returnIdsOnly
              properties:
                geometry:
                  $ref: '#/definitions/geometry'
                geometryType:
                  type: string
                  default: 'esriGeometryPolygon'
                outFields:
                  type: string
                  default: '*'
                inSR:
                  type: integer
                  default: 4326
                returnGeometry:
                  type: boolean
                  default: true
                f:
                  type: string
                  default: json
                returnCountOnly:
                  type: boolean
                  default: false
                outSR:
                  type: integer
                  default: 4326
                returnIdsOnly:
                  type: boolean
                  default: false
        definitions:
          geometry:
            type: object
            properties:
              rings:
                $ref: '#/definitions/rings'
              spatialReference:
                $ref: '#/definitions/spatialReference2'
          rings:
            type: array
            items:
              $ref: '#/definitions/rings2'
          rings2:
            type: array
            items:
              $ref: '#/definitions/rings3'
          rings3:
            type: integer
          spatialReference2:
            type: object
            properties:
              wkid:
                type: integer
        responses:
          200:
            description: data
        """
        return 200


api.add_resource(ApiExport, '/arcgis/rest/services/SIROCCO/SIROCARTE/MapServer/export/v2')
api.add_resource(ApiIdentify, '/arcgis/rest/services/SIROCCO/SIROCARTE/MapServer/identify')
api.add_resource(ApiSpatial, '/arcgis/rest/services/SIROCCO/SIROCARTE/MapServer/5/query')


# Start program
if __name__ == '__main__':
    print("Dev Portal: http://127.0.0.1:5000/apidocs/")
    application.run(
        host="0.0.0.0",
        use_reloader=True,
        port=5000
    )

