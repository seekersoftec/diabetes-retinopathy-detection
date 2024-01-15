# Fast-API 🚀

### Why This ? 🤨

    Need Clean and Scalable Code Architecture for ML/DL and NLP driven micro-service based Projects ?

### **Introduction: Structuring of API**

- `api_template:` Contains all the API related Code Base.

  - `manage.py:` Only entry point for API. Contains no logic.
  - `.env:` Most important file for your api and contains global configs. Acoid using application/variable level configs here.
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

![Screenshot 2021-05-16 at 6 56 38 PM](https://user-images.githubusercontent.com/17409469/118399886-ea6acd80-b67c-11eb-88de-7dd5021d2bce.png)
Run Command **uvicorn manage:app --host 0.0.0.0 --port 8000**

### Docker Support 🐳

    docker build -t fastapi-image  .
    docker run -d --name fastapi-container -p 8000:8000 fastapi-image

### Sample Demo App ~ Powered by Streamlit ⚡️

![Screenshot 2021-05-16 at 6 56 19 PM](https://user-images.githubusercontent.com/17409469/118399165-80045e00-b679-11eb-9416-8b73936e9b83.png)
Always good to have an interface to show a quick demo 😁.
`Note: manage.py runs the streamlit app as a subprocess. feel free to move it as per your need. `

### What is new ?

- Form Support for Image Classification
  ![imgClassification](https://user-images.githubusercontent.com/17409469/142370743-c06a6156-f30e-487e-9004-2cabdb961af1.png)
- Cutelogs GUI Integration for Easy LogsView
  ![Logs](https://user-images.githubusercontent.com/17409469/142371199-c5ae36fa-7fd6-4b47-aea6-da728f7f8990.png)

```python
# Function to preprocess image for the model
# def preprocess_image(img_path):
#     img = Image.open(img_path)  # target_size=(HEIGHT, WIDTH)
#     img_array = np.asarray(img.resize((IMG_SIZE,) * 2, resample=Image.LANCZOS))
#     # img_array /= 255.0  # Normalize
#     img_array = img_array[..., :3] / 255.0
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = load_ben_color(img)
#     # image = np.asarray(image.resize(shape))
#     # image = np.array(image)[..., :3] / 255.0
#     # image = np.expand_dims(image, axis=0)
#     return np.asarray(img_array)

# Function to load BEN color
# def load_ben_color(file):
#     img = cv2.imread(file)
#     # gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = cv2.resize(file, (IMG_SIZE, IMG_SIZE))
#     img = cv2.addWeighted(img, 4, cv2.GaussianBlur(img, (0, 0), sigmaX), -4, 128)
#     return img

# img = preprocess_image(file_path)
# prediction = classifier_model.predict(img, 2)
```

```javascript
// type: "image/jpeg"
//     var reader = new FileReader();
// reader.onload = function (e) {
//     var base64data = e.target.result; // Base64 encoded image data

//     $.ajax({
//         url: "/api/v1/image-classify",
//         type: "POST",
//         data: {
//             file: base64data, // Submit encoded data
//         },
//         success: function (data) {
//             // Handle successful upload response
//             alert("Image uploaded successfully!");
//         },
//         error: function (error) {
//             // Handle upload error
//             alert("Error uploading image: " + error.responseText);
//         }
//     });
// };
//     reader.readAsDataURL(file); // Read image as Base64

// const form = new FormData();
// form.append("file", "/home/fortesenselabs/Tech/seekersoftec/Dr. Odigie-wares/datasets/DR dataset/1.jpg");

// const settings = {
//     "async": true,
//     "crossDomain": true,
//     "url": "http://localhost:8000/api/v1/image-classify",
//     "method": "POST",
//     "headers": {},
//     "processData": true,
//     "contentType": false,
//     "mimeType": "multipart/form-data",
//     "data": form
// };

// $.ajax(settings).done(function (response) {
//     console.log(response);
// });
```

**Drop me email for any queries on subir.verma48@gmail.com**
