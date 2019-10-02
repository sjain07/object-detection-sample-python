import os, requests
from tqdm import tqdm

pathToAnnotations = './annotations/json'
pathToImages = './images'
model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')

for root, dirs, files in os.walk(pathToAnnotations, topdown=False):
    for name in tqdm(files):
        annotation = open(os.path.join(root, name), "r")
        filePath = os.path.join(root, name)
        imageName, ext = name.split(".")
        imagePath = os.path.join(pathToImages, imageName + '.jpg')
        #jsonData = annotation.read().replace(" ","")
        jsonDict = jsonData.loads()
        jsonDict[0]["name"] = "car"
        jsonData = jsonDict.dumps()
        url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/UploadFile/'
        data = {'file' :open(imagePath, 'rb'),  'data' :('', '[{"filename":"' + imageName+".jpg" + '", "object": '+ jsonData+'}]'),   'modelId' :('', model_id)}       
        response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)
        if response.status_code > 250 or response.status_code<200:
            print(response.text), response.status_code

print("\n\n\nNEXT RUN: python ./code/train-model.py")