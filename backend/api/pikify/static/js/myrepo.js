let selectedImages = []
function selectImage(url){
    if(selectedImages.includes(url, event)){
        selectedImages = selectedImages.filter(a => a !== url);
        event.target.parentNode.style.borderColor= "#333333"
    }
    else{
        selectedImages.push(url)
        event.target.parentNode.style.borderColor= "#FFA194"
    }  
}

document.querySelector("#deleteButton").addEventListener("click", deleteImages);

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

function deleteImages(e){
    e.preventDefault()
    console.log("here")
    console.log(csrftoken)
    fetch('/pikify/myrepo/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrftoken,
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(selectedImages)
    }).then(location.reload())  
}










