let croppieInstance;
const input = document.getElementById("id_photo");
const imagePreview = document.getElementById("image-preview");
const croppedImageInput = document.getElementById("croppedImage");
const form = document.getElementById("athleteForm");

function displayImage(input) {
  if (input.files && input.files[0]) {
    const reader = new FileReader();
    reader.onload = function (e) {
      imagePreview.src = e.target.result;
      if (croppieInstance) {
        croppieInstance.destroy();
      }
      croppieInstance = new Croppie(imagePreview, {
        viewport: { width: 200, height: 200, type: "square" },
        boundary: { width: 300, height: 300 },
        url: e.target.result,
      });
    };
    reader.readAsDataURL(input.files[0]);
  }
}

form.addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent default form submission
  croppieInstance
    .result({ type: "base64", size: "viewport" })
    .then(function (base64) {
      croppedImageInput.value = base64;
      form.submit(); // Submit the form
    });
});
