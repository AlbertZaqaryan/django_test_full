function updateLanguage() {
    var language = document.getElementById('language-selector').value;
    var url = '/update-language/';
    var data = {'language': language};
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            console.log('Language preference updated successfully!');
        } else {
            console.error('Error updating language preference:', xhr.statusText);
        }
    };
    xhr.onerror = function() {
        console.error('Error updating language preference:', xhr.statusText);
    };
    xhr.send(JSON.stringify(data));
}