
let selectedImages = []

function selectImage(url){
    if(selectedImages.includes(url)){
        selectedImages = selectedImages.filter(e => e !== url);
    }
    else{
        selectedImages.push(url)
    }  
    console.log(selectedImages)
}

document.querySelector("#saveButton").addEventListener("click", saveImages);

// https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function saveImages(e){
    e.preventDefault()
    console.log("here")
    console.log(csrftoken)
    fetch('/pikify/search/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrftoken,
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(selectedImages)
    }).then(res => console.log(res))
    
}












