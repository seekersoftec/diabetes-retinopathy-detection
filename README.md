# Seeing Clearly: A Software Project for Early Diabetic Retinopathy Detection 🚀
 
Diabetic retinopathy (DR), a silent yet devastating complication of diabetes, threatens vision for millions worldwide. To address the critical need for early detection, this software development project aims to create an automated and cost-effective system for classifying DR in retinal images. This innovative tool, leveraging the power of machine learning and artificial intelligence, promises to significantly improve early DR detection, enabling timely intervention and safeguarding vision. By bridging the gap in accessible diagnosis, the project aspires to empower individuals with diabetes and alleviate healthcare burdens, ultimately contributing to improved health outcomes and a brighter future for individuals and communities.

### Technologies Used

- Python
- Fast API
- Dropzone 

### Introduction: Structuring of API

- `/:` Contains all the API related Code Base.
  - `manage.py:` Only entry point for API. Contains no logic.
  - `.env:` Most important file for your api and contains global configs. Avoid using application/variable level configs here.
  - `application:` It contains all your api related codes and test modules. I prefer keeping application folder at global.
  - `logs`: Logs is self-explanatory. FYI it will not contain any configuration information, just raw logs. Feel free to move according to your comfort but not inside the application folder.
  - `models:` As a part of Machine-Learning/ Deep-Learning app you might need to add model files here or if you have huge files on cloud add symlinks if possibles.
  - `resources:` To store any documentation, application related csv/txt/img files etc.
  - `settings:` Logger/DataBase/Model global settings files in yaml/json format.

  - `application:`
    - `main:` priority folder of all your application related code.
      - `🏗 infrastructure:` Data Base and ML/DL models related backbone code
      - `📮 routers:` API routers and they strictly do not contain any business logic
      - `📡 services:` All processing and business logic for routers here at service layer
      - `⚒ utility:`
        - `config_loader` Load all application related config files from settings directory
        - `logger` Logging module for application
        - `manager` A manager utility for Data Related Task which can be common for different services
      - `🐍 config.py:` Main config of application, inherits all details from .env file
    - `test:` Write test cases for your application here.
    - `initializer.py:` Preload/Initialisation of Models and Module common across application. Preloading model improves inferencing.
  
### Running Locally ? 📍

Run Command **uvicorn manage:app --host 0.0.0.0 --port 8000**
Then go to: localhost:8000 or 127.0.0.1:8000 on your browser

### Docker Support 🐳

```bash
    docker build -t drd-api-image  .
    docker run -d --name drd-api -p 8000:8000 drd-api-image
```

### Sample Demo App ~ Powered by Streamlit ⚡️

Always good to have an interface to show a quick demo 😁.
`Note: manage.py runs the streamlit app as a subprocess. feel free to move it as per your need.`

### API Request

```bash
curl --request POST \
  --url http://localhost:8000/api/v1/image-classify \
  --header 'Content-Type: multipart/form-data' \
  --form 'file=@/datasets/1.jpg'
```

### API Response 

```json
{
	"data": {
		"label": 1,
		"class": "Referable",
		"confidence": "91.60%",
		"filename": "1.jpg"
	}
}
```

### Resources

- https://www.techscience.com/cmc/v67n2/41339/html
- https://github.com/99sbr/fastapi-template


