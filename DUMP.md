# DUMP

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
