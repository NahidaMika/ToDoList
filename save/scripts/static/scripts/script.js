var key = "$2a$10$yRFiQAvPGDisjoej/1ZLQ.buogMci3M3DB6xkpFYlduVOX4p71l0i";

var jsonTextArea = document.getElementById("json");

window.onload = set_none("", "json");
window.onload = set_none("Not completed", "status");
window.onload = set_none("", "task");

jsonTextArea.onchange = () => {
    console.log(jsonTextArea.value);
    };


function post() { // Not in use
    let req = new XMLHttpRequest();
    req.onreadystatechange = () => {
    if (req.readyState == XMLHttpRequest.DONE){
    console.log(req.responseText);
    if (req.status == 200) {
        saveToFile("ToDoListWeb.json", JSON.stringify(req.responseText), "application/json");
    }
    }
    };

    req.open("POST", "https://api.jsonbin.io/v3/b", true);
    req.setRequestHeader("Content-Type","application/json");
    req.setRequestHeader("X-Master-Key", key);
    req.setRequestHeader("X-Bin-Name","ToDoList");
    req.setRequestHeader("X-Bin-Private","true");

    req.send('{"date": "2222-22-22","todo": [{"task": "Decirle a Cami", "status": "Not completed"},{"task": "Modify json with a checkbar", "status": "Not completed"},{"task": "Reload json while active", "status": "Not completed"},{"task": "Check http json maker", "status": "Not completed"},{"task": "Finish to-do list app", "status": "Not completed"}]}');


};

function update() { //Not in use
    let req = new XMLHttpRequest();
    req.onreadystatechange = () => {
    if (req.readyState == XMLHttpRequest.DONE){
    console.log(req.responseText);
    }
    };

    req.open("PUT", "https://api.jsonbin.io/v3/b/686490938a456b7966b9cc45", true);
    req.setRequestHeader("Content-Type","application/json");
    req.setRequestHeader("X-Master-Key", key);
    req.setRequestHeader("X-Bin-Name","ToDoList");
    req.setRequestHeader("X-Bin-Private","true");

    req.send('{"date": "2222-22-22","todo": [{"task": "Decirle a Cami", "status": "Not completed"},{"task": "Modify json with a checkbar", "status": "Not completed"},{"task": "Reload json while active", "status": "Not completed"},{"task": "Check http json maker", "status": "Not completed"},{"task": "Finish to-do list app", "status": "Not completed"}]}');
};

function update_with_user_input() {
    let req = new XMLHttpRequest();
    req.onreadystatechange = () => {
    if (req.readyState == XMLHttpRequest.DONE){
    console.log(req.responseText);
    alert("File updated successfully");
    }
    };

    req.open("PUT", "https://api.jsonbin.io/v3/b/686490938a456b7966b9cc45", true);
    req.setRequestHeader("Content-Type","application/json");
    req.setRequestHeader("X-Master-Key", key);
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

    req.open("GET", "https://api.jsonbin.io/v3/b/686490938a456b7966b9cc45", true);
    req.setRequestHeader("X-Master-Key", key);
    req.setRequestHeader("X-Bin-Meta","false");
    req.send();
};

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

function saveToFile(filename, content, mimeType = "text/plain") {
    // Create a Blob object from the content
    const blob = new Blob([content], { type: mimeType });

    // Create a URL for the Blob
    const url = URL.createObjectURL(blob);

    // Create a temporary anchor element
    const a = document.createElement("a");
    a.href = url;
    a.download = filename; // Set the desired filename

    // Programmatically click the anchor to trigger the download
    document.body.appendChild(a); // Append to body to ensure click works in all browsers
    a.click();

    // Clean up by revoking the URL and removing the anchor
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}