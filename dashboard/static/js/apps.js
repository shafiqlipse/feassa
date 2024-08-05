let cropper;
let croppedImageBlob;

document.addEventListener("DOMContentLoaded", function () {
  const imageContainer = document.getElementById("image-container");
  const fileInput = document.getElementById("id_photo");

  imageContainer.addEventListener("click", function () {
    fileInput.click();
  });
});

document
  .getElementById("id_photo")
  .addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        const imagePreview = document.getElementById("image-preview");
        imagePreview.src = e.target.result;

        if (cropper) {
          cropper.destroy();
        }

        cropper = new Cropper(imagePreview, {
          aspectRatio: 1, // You can change this as needed
          viewMode: 1,
          minCropBoxWidth: 200,
          minCropBoxHeight: 200,
        });

        document.getElementById("crop-button").style.display = "block";
      };
      reader.readAsDataURL(file);
    }
  });

document.getElementById("crop-button").addEventListener("click", function () {
  if (cropper) {
    cropper.getCroppedCanvas().toBlob((blob) => {
      croppedImageBlob = blob;
      document.getElementById("image-preview").src = URL.createObjectURL(blob);
      cropper.destroy();
      cropper = null;
      document.getElementById("crop-button").style.display = "none";
    });
  }
});

document.querySelector("form").addEventListener("submit", function (e) {
  if (croppedImageBlob) {
    e.preventDefault();
    const formData = new FormData(this);
    formData.set("photo", croppedImageBlob, "cropped_image.png");

    fetch(this.action, {
      method: "POST",
      body: formData,
    }).then((response) => {
      if (response.ok) {
        window.location.href = '{% url "schools" %}';
      } else {
        console.error("Form submission failed");
      }
    });
  }
  // If there's no cropped image, let the form submit normally
});
function displayImage(input) {
  var reader = new FileReader();
  reader.onload = function (e) {
    document.getElementById("image-preview").src = e.target.result;
  };
  reader.readAsDataURL(input.files[0]);
}

//.tabs for profiles
// function displayImage2(input) {
//   var reader = new FileReader();
//   reader.onload = function (e) {
//     document.getElementById("image-previewg").src = e.target.result;
//   };
//   reader.readAsDataURL(input.files[0]);
// }

// //.tabs for profiles
// function displayImage1(input) {
//   var reader = new FileReader();
//   reader.onload = function (e) {
//     document.getElementById("image-previews").src = e.target.result;
//   };
//   reader.readAsDataURL(input.files[0]);
// }

// //.tabs for profiles
