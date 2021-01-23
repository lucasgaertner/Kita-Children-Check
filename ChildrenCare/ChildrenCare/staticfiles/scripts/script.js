function setHeader(){
    var currenturl = window.location.href;
    var header = str.substring(currenturl.lastIndexOf("/") + 1, str.length);
    alert(header);
}