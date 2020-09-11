from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from url_id import RetornaIdUrl

authenticator = IAMAuthenticator('{API key}')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url('{Your Set Service URL}')


class CheckProfilePic:

    def verifica_imagem(self, url):
        self._classes = visual_recognition.classify(
            url=RetornaIdUrl.retorna_url_img_pelo_id(url),
            threshold='0.0',
            classifier_ids='{Your CustomModel ID}').get_result()
        self._dicionario_score = dict(self._classes, indent=2)
        return float(self._dicionario_score['images'][0]['classifiers'][0]['classes'][0]['score'])
