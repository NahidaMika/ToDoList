var ApiKey
var FileID 

var jsonTextArea = document.getElementById("json");

window.onload = Get_FileID();
window.onload = Get_APIKEY();
window.onload = set_none("", "json");
window.onload = set_none("Not completed", "status");
window.onload = set_none("", "task");

jsonTextArea.onchange = () => {
    console.log(jsonTextArea.value);
    };

function update_with_user_input() {
    let req = new XMLHttpRequest();
    req.onreadystatechange = () => {
    if (req.readyState == XMLHttpRequest.DONE){
    console.log(req.responseText);
    alert("File updated successfully");
    }
    };

    req.open("PUT", "https://api.jsonbin.io/v3/b/"+FileID, true);
    req.setRequestHeader("Content-Type","application/json");
    req.setRequestHeader("X-Master-Key", ApiKey);
    req.setRequestHeader("X-Bin-Name","ToDoList");
    req.setRequestHeader("X-Bin-Private","true");

    req.send(jsonTextArea.value);
};

function get() {
    let req = new XMLHttpRequest();
    req.onreadystatechange = () => {
    if (req.readyState == XMLHttpRequest.DONE){
    console.log(req.responseText);
    jsonTextArea.value = req.responseText
    }
    };

    req.open("GET", "https://api.jsonbin.io/v3/b/"+FileID, true);
    req.setRequestHeader("X-Master-Key", ApiKey);
    req.setRequestHeader("X-Bin-Meta","false");
    req.send();
};

function Get_FileID() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
    if (xhr.readyState == XMLHttpRequest.DONE){
    console.log(xhr.responseText);
    if (xhr.status == 200) {
        const ID = xhr.responseText;
        FileID = (ID);
        console.log(FileID);
        return FileID
    }
    }
    };

    xhr.open("GET", "http://127.0.0.1:5000/api-keys/FileID", true);
    xhr.send('');
}

function Get_APIKEY() {
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
    if (xhr.readyState == XMLHttpRequest.DONE){
    console.log(xhr.responseText);
    if (xhr.status == 200) {
        const key = xhr.responseText;
        ApiKey = (key);
        console.log(ApiKey);
        return ApiKey
    }
    }
    };

    xhr.open("GET", "http://127.0.0.1:5000/api-keys/JSONBIN", true);
    xhr.send('');
}

function set_none(value, id){
        var textarea = document.getElementById(id);
        textarea.value = value;
    }

function add_task() {
    var jsonSaveText1 = jsonTextArea.value;
    var jsonSaveText2 = jsonSaveText1.slice(0, jsonSaveText1.length - 1);
    var jsonSaveText3 = jsonSaveText2.slice(0, jsonSaveText2.length - 1);
    jsonTextArea.value = jsonSaveText3;


    jsonTextArea.value += ',{"task": "' + document.getElementById("task").value + '", "status": "' + document.getElementById("status").value + '"}]}';

}
